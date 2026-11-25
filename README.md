# AI Study Tip Generator
### Generative AI Creative Solution – MCA Capstone Project

## 1. Project Overview

The AI Study Tip Generator is a Generative AI application that generates study tips based on academic topics entered by users.

The project uses the pretrained GPT-2 language model and fine-tunes its last Transformer block using a small custom dataset of study topics and corresponding study tips.

A Streamlit interface allows users to enter a topic and receive an AI-generated study suggestion.

## 2. Problem Statement

Students often need simple and actionable suggestions to help them study different academic subjects.

This project explores how a pretrained language model can be adapted to generate topic-related study tips through a simple web application.

## 3. Objectives

- Understand the working of a pretrained GPT-2 model.
- Prepare a custom study-tip dataset.
- Fine-tune GPT-2 on study-tip examples.
- Compare original and fine-tuned GPT-2 outputs.
- Develop an interactive application using Streamlit.
- Evaluate generated text for relevance, readability and usefulness.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.12 | Programming language |
| GPT-2 | Text generation |
| PyTorch | Deep learning framework |
| Hugging Face Transformers | Model loading and fine-tuning |
| Pandas | Dataset handling |
| Streamlit | Web application |
| Accelerate | Training support |
| Scikit-learn | Machine learning utilities |
| Matplotlib | Visualization |

## 5. Project Structure

```text
GenAI-Assignment-5/
│
├── data/
│   ├── train.csv
│   └── test.csv
│
├── lab_outputs/
│   ├── study_tip_gpt2/
│   ├── checkpoints/
│   ├── training_log.csv
│   └── evaluation_results.csv
│
├── app.py
├── gpt2_text_generation.py
├── evaluate.py
├── README.md
├── LAB_RECORD.md
├── requirements.txt
└── .gitignore
```

Note: The `.venv` folder is excluded from GitHub. The trained model folder is required to run the application without retraining.

## 6. Dataset

The project uses a manually prepared dataset.

- Training dataset: 15 topic and study-tip pairs.
- Testing dataset: 10 held-out academic topics.
- Training data is used for model adaptation.
- Testing topics are kept separate for evaluation.

The testing dataset contains topics such as Cloud Computing, Computer Architecture, Compiler Design, Data Mining and Information Security.

**Data source:** Manually prepared educational topic and study-tip examples for this academic demonstration.

## 7. Model and Fine-tuning

The project uses the pretrained GPT-2 model:

`openai-community/gpt2`

Model configuration:

- Training epochs: 3
- Batch size: 1
- Learning rate: 0.00002
- Maximum sequence length: 96 tokens
- Trainable layers: Last Transformer block and language-model head
- Execution environment: CPU

The fine-tuned model is saved in:

`lab_outputs/study_tip_gpt2/`

## 8. Application Features

- User-friendly Streamlit interface.
- Study topic input field.
- AI-generated study tips.
- Empty-input validation.
- Fine-tuned GPT-2 integration.
- Generated suggestions displayed in the browser.

## 9. How to Run the Project

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd GenAI-Assignment-5
```

### Step 2: Create a virtual environment

```powershell
py -3.12 -m venv .venv
```

### Step 3: Activate the environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 4: Install dependencies

First install CPU-only PyTorch:

```powershell
python -m pip install torch --index-url https://download.pytorch.org/whl/cpu
```

Then install the remaining dependencies:

```powershell
python -m pip install -r requirements.txt
```

### Step 5: Fine-tune GPT-2

```powershell
python gpt2_text_generation.py
```

This downloads GPT-2 if necessary, fine-tunes the model and saves the model files.

### Step 6: Evaluate both models

```powershell
python evaluate.py
```

The comparison is saved to:

`lab_outputs/evaluation_results.csv`

### Step 7: Run the Streamlit application

```powershell
streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

http://localhost:8501

**Note:** The fine-tuned model folder must exist before running the application. The first model download requires an internet connection.

## 10. Evaluation

The original and fine-tuned GPT-2 models are tested on the same 10 held-out topics.

The generated outputs are saved in:

`lab_outputs/evaluation_results.csv`

The evaluation criteria are:

- Relevance
- Readability
- Usefulness

Each criterion is scored from 0 to 2, giving a maximum score of 6 per model and topic.

## 11. Limitations

- The custom dataset contains only 15 training examples.
- GPT-2 can generate repetitive or unrelated text.
- Some generated tips may be incomplete or generic.
- Fine-tuning on a small dataset does not guarantee improved output quality.
- The model requires human review before its suggestions are used.
- CPU-based training and generation can take time.

## 12. Future Enhancements

- Increase the size and diversity of the training dataset.
- Improve the quality of generated study tips.
- Experiment with different language models.
- Add subject-wise study recommendations.
- Improve the user interface.
- Add user feedback and output-quality evaluation.

## 13. Responsible Use

The application is an educational demonstration. Generated study tips may contain inaccurate or irrelevant information. Users should review suggestions before relying on them.

## 14. Conclusion

The project demonstrates the use of a pretrained GPT-2 model, custom dataset preparation, model fine-tuning, text generation and Streamlit application development.

It provides practical experience with Generative AI and demonstrates both the capabilities and limitations of small-scale language-model adaptation.

---

**Course:** Generative AI and Its Applications  
**Course Code:** ETMMGA304  
**Project:** Assignment 5 – Generative AI Creative Solution  
**University:** K.R. Mangalam University