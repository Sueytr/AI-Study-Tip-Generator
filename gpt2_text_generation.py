
import pandas as pd
import torch
from pathlib import Path
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    Trainer,
    TrainingArguments,
    default_data_collator
)

# --------------------------------
# 1. Project configuration
# --------------------------------

MODEL_NAME = "openai-community/gpt2"
DATA_PATH = "data/train.csv"
OUTPUT_DIR = "lab_outputs/study_tip_gpt2"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("Using device:", device)

# --------------------------------
# 2. Load training dataset
# --------------------------------

df = pd.read_csv(DATA_PATH)
df = df.dropna(subset=["topic", "study_tip"])

print("Training examples:", len(df))

texts = [
    f"Topic: {row.topic}\nStudy tip: {row.study_tip}"
    for row in df.itertuples()
]

# --------------------------------
# 3. Load GPT-2 tokenizer
# --------------------------------

print("Loading GPT-2 tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
tokenizer.pad_token = tokenizer.eos_token

# --------------------------------
# 4. Tokenize dataset
# --------------------------------

class StudyTipDataset(torch.utils.data.Dataset):

    def __init__(self, texts, tokenizer):
        self.encodings = tokenizer(
            texts,
            truncation=True,
            padding="max_length",
            max_length=96,
            return_tensors="pt"
        )

    def __len__(self):
        return self.encodings["input_ids"].size(0)

    def __getitem__(self, index):

        input_ids = self.encodings["input_ids"][index]
        attention_mask = self.encodings["attention_mask"][index]

        labels = input_ids.clone()
        labels[attention_mask == 0] = -100

        return {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "labels": labels
        }


dataset = StudyTipDataset(texts, tokenizer)

print("Dataset prepared successfully!")

# --------------------------------
# 5. Load GPT-2 model
# --------------------------------

print("Loading GPT-2 model...")

model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

model.config.pad_token_id = tokenizer.pad_token_id

# Freeze all model parameters
for param in model.parameters():
    param.requires_grad = False

# Fine-tune the last Transformer block
for param in model.transformer.h[-1].parameters():
    param.requires_grad = True

# Fine-tune the language model head
for param in model.lm_head.parameters():
    param.requires_grad = True

model.to(device)

trainable = sum(
    p.numel() for p in model.parameters() if p.requires_grad
)

print("Trainable parameters:", trainable)

# --------------------------------
# 6. Training configuration
# --------------------------------

training_args = TrainingArguments(
    output_dir="lab_outputs/checkpoints",
    num_train_epochs=3,
    per_device_train_batch_size=1,
    learning_rate=2e-5,
    weight_decay=0.01,
    logging_steps=1,
    save_strategy="no",
    report_to="none",
    use_cpu=(device.type == "cpu"),
    dataloader_pin_memory=False
)

# --------------------------------
# 7. Fine-tune GPT-2
# --------------------------------

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    data_collator=default_data_collator
)

print("\nStarting GPT-2 fine-tuning...\n")

trainer.train()

# --------------------------------
# 8. Save fine-tuned model
# --------------------------------

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

model.save_pretrained(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)

print("\nFine-tuning completed successfully!")
print("Fine-tuned model saved at:", OUTPUT_DIR)

# --------------------------------
# 9. Save training results
# --------------------------------

history = trainer.state.log_history

pd.DataFrame(history).to_csv(
    "lab_outputs/training_log.csv",
    index=False
)

print("Training log saved successfully!")
