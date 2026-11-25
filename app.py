from pathlib import Path

import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# --------------------------------
# 1. Application configuration
# --------------------------------

st.set_page_config(
    page_title="AI Study Tip Generator",
    page_icon="📚",
    layout="centered"
)

MODEL_FOLDER = Path("lab_outputs/study_tip_gpt2")

# --------------------------------
# 2. Load fine-tuned GPT-2
# --------------------------------

@st.cache_resource
def load_model():

    tokenizer = AutoTokenizer.from_pretrained(
        str(MODEL_FOLDER)
    )

    model = AutoModelForCausalLM.from_pretrained(
        str(MODEL_FOLDER)
    )

    model.eval()

    return tokenizer, model


# --------------------------------
# 3. Application interface
# --------------------------------

st.title("📚 AI Study Tip Generator")

st.write(
    "Generate AI-powered study tips for different academic topics."
)

st.info(
    "This application uses a fine-tuned GPT-2 model. "
    "Generated suggestions should be reviewed before use."
)

# Check model availability
if not (MODEL_FOLDER / "config.json").exists():

    st.error(
        "Fine-tuned model not found. "
        "Please run gpt2_text_generation.py first."
    )

    st.stop()


# --------------------------------
# 4. User input
# --------------------------------

topic = st.text_input(
    "Enter your study topic",
    placeholder="Example: Machine Learning",
    max_chars=120
)

# --------------------------------
# 5. Generate study tip
# --------------------------------

if st.button("Generate Study Tip", type="primary"):

    if not topic.strip():

        st.warning("Please enter a study topic first.")

    else:

        try:

            with st.spinner("Generating your study tip..."):

                tokenizer, model = load_model()

                prompt = (
                    f"Topic: {topic.strip()}\n"
                    "Study tip:"
                )

                inputs = tokenizer(
                    prompt,
                    return_tensors="pt"
                )

                with torch.inference_mode():

                    output = model.generate(
                        **inputs,
                        max_new_tokens=45,
                        do_sample=False,
                        repetition_penalty=1.2,
                        no_repeat_ngram_size=3,
                        pad_token_id=tokenizer.eos_token_id
                    )

                generated_tokens = output[
                    0, inputs["input_ids"].shape[1]:
                ]

                tip = tokenizer.decode(
                    generated_tokens,
                    skip_special_tokens=True
                ).strip()

            st.subheader("Your Study Tip")

            if tip:

                st.success(tip)

            else:

                st.warning(
                    "No useful tip was generated. "
                    "Try another topic."
                )

        except Exception as error:

            st.error(f"Generation failed: {error}")


# --------------------------------
# 6. Footer
# --------------------------------

st.divider()

st.caption(
    "MCA Generative AI Capstone Project | "
    "Powered by GPT-2 and Streamlit"
)