import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

BASE_MODEL = "openai-community/gpt2"
FINE_TUNED_MODEL = "lab_outputs/study_tip_gpt2"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("Using device:", device)

# Load testing data
test_df = pd.read_csv("data/test.csv")

# Load original GPT-2
print("\nLoading original GPT-2...")
base_tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)
base_model = AutoModelForCausalLM.from_pretrained(BASE_MODEL).to(device)
base_model.eval()

# Load fine-tuned GPT-2
print("\nLoading fine-tuned GPT-2...")
tuned_tokenizer = AutoTokenizer.from_pretrained(FINE_TUNED_MODEL)
tuned_model = AutoModelForCausalLM.from_pretrained(FINE_TUNED_MODEL).to(device)
tuned_model.eval()

# Generate a study tip
def generate_tip(model, tokenizer, topic):
    prompt = f"Topic: {topic}\nStudy tip:"

    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    with torch.inference_mode():
        output = model.generate(
            **inputs,
            max_new_tokens=45,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id
        )

    generated = output[0][inputs["input_ids"].shape[1]:]

    return tokenizer.decode(
        generated,
        skip_special_tokens=True
    ).strip()

# Evaluate both models
results = []

for topic in test_df["topic"]:

    print("\nTopic:", topic)

    base_tip = generate_tip(
        base_model, base_tokenizer, topic
    )

    tuned_tip = generate_tip(
        tuned_model, tuned_tokenizer, topic
    )

    print("Original GPT-2:", base_tip)
    print("Fine-tuned GPT-2:", tuned_tip)

    results.append({
        "topic": topic,
        "base_model_output": base_tip,
        "fine_tuned_model_output": tuned_tip
    })

# Save results
results_df = pd.DataFrame(results)

results_df.to_csv(
    "lab_outputs/evaluation_results.csv",
    index=False
)

print("\nEvaluation completed!")
print("Results saved to lab_outputs/evaluation_results.csv")