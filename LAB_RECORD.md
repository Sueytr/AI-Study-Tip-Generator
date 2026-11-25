# LAB RECORD

## Assignment 5 – Generative AI Creative Solution
### Project: AI Study Tip Generator

**Course:** Generative AI and Its Applications  
**Course Code:** ETMMGA304  
**University:** K.R. Mangalam University  
**Project Type:** Generative AI Capstone

---

# 1. Aim

To develop an AI-based Study Tip Generator using a pretrained GPT-2 language model, fine-tune it using a custom study-tip dataset, evaluate its generated outputs and demonstrate the application through Streamlit.

# 2. Problem Definition

Students may need simple and actionable study suggestions for different academic topics.

The objective is to develop an application that accepts an academic topic and generates a study tip using a Generative AI language model.

# 3. Proposed Solution

The project uses GPT-2 for text generation.

The pretrained model is adapted using a custom dataset containing academic topics and their corresponding study tips.

The adapted model is integrated into a Streamlit application where users can enter topics and receive generated suggestions.

# 4. Dataset Preparation

A manually prepared dataset was created for the project.

| Dataset | Number of examples | Purpose |
|---|---:|---|
| Training dataset | 15 | Fine-tuning GPT-2 |
| Testing dataset | 10 | Evaluating generated outputs |

The training dataset contains topics such as:

1. Time Management
2. Python Programming
3. Mathematics
4. Machine Learning
5. Deep Learning
6. Database Management
7. Operating Systems
8. Computer Networks
9. Data Structures
10. Artificial Intelligence
11. Natural Language Processing
12. Cyber Security
13. Web Development
14. Software Engineering
15. Exam Preparation

The testing dataset contains separate topics that were not used for training:

- Cloud Computing
- Computer Architecture
- Compiler Design
- Data Mining
- Big Data Analytics
- Computer Graphics
- Software Testing
- Microservices
- Cyber Ethics
- Information Security

**Data source:** Manually prepared educational topic and study-tip examples for this academic demonstration.

# 5. Technologies and Libraries

| Technology | Application |
|---|---|
| Python 3.12 | Project implementation |
| GPT-2 | Text generation |
| PyTorch | Deep learning and model training |
| Hugging Face Transformers | Tokenization, model loading and fine-tuning |
| Pandas | Reading and processing CSV data |
| Streamlit | Web application interface |
| Accelerate | Training support |
| Matplotlib | Data visualization |
| Scikit-learn | Machine learning utilities |

# 6. Model Configuration

| Parameter | Value |
|---|---|
| Model | GPT-2 |
| Model identifier | openai-community/gpt2 |
| Training epochs | 3 |
| Batch size | 1 |
| Learning rate | 0.00002 |
| Maximum sequence length | 96 tokens |
| Trainable layers | Last Transformer block and language-model head |
| Execution device | CPU |
| Training examples | 15 |

# 7. Implementation Workflow

1. Define the user problem.
2. Prepare training and testing datasets.
3. Load the pretrained GPT-2 model and tokenizer.
4. Tokenize the training data.
5. Freeze the model parameters except the selected trainable layers.
6. Fine-tune GPT-2 using the training dataset.
7. Save the adapted model.
8. Generate outputs using the original and adapted models.
9. Compare outputs using held-out topics.
10. Develop the Streamlit application.
11. Test the application with different academic topics.

# 8. Training Results

The fine-tuning process completed successfully.

| Observation | Actual result |
|---|---|
| Training examples | 15 |
| Training epochs | 3 |
| Training steps | 45 |
| Training loss | Approximately 5.1719 |
| Model saved | Yes |
| Training log saved | Yes |
| Execution device | CPU |

**Saved model:** `lab_outputs/study_tip_gpt2/`

**Training log:** `lab_outputs/training_log.csv`

The training loss represents the model's error on the training data. It does not by itself establish the quality of generated study tips.

# 9. Evaluation Methodology

Both the original GPT-2 and fine-tuned GPT-2 were tested on the same 10 held-out topics.

The generated outputs were saved in:

`lab_outputs/evaluation_results.csv`

The evaluation criteria are:

- **Relevance:** How closely the generated tip relates to the given topic.
- **Readability:** How clear and understandable the generated text is.
- **Usefulness:** How practical and helpful the suggestion is for a student.

Each criterion is scored as follows:

| Score | Meaning |
|---|---|
| 0 | Poor |
| 1 | Partial |
| 2 | Strong |

Maximum score per model per topic: 6.

## Evaluation table

Review the complete generated outputs and enter the scores based on the criteria above.

| Topic | Model | Relevance | Readability | Usefulness | Total / 6 |
|---|---|---:|---:|---:|---:|
| Cloud Computing | Base | | | | |
| Cloud Computing | Adapted | | | | |
| Computer Architecture | Base | | | | |
| Computer Architecture | Adapted | | | | |
| Compiler Design | Base | | | | |
| Compiler Design | Adapted | | | | |
| Data Mining | Base | | | | |
| Data Mining | Adapted | | | | |
| Big Data Analytics | Base | | | | |
| Big Data Analytics | Adapted | | | | |
| Computer Graphics | Base | | | | |
| Computer Graphics | Adapted | | | | |
| Software Testing | Base | | | | |
| Software Testing | Adapted | | | | |
| Microservices | Base | | | | |
| Microservices | Adapted | | | | |
| Cyber Ethics | Base | | | | |
| Cyber Ethics | Adapted | | | | |
| Information Security | Base | | | | |
| Information Security | Adapted | | | | |

## Mean score calculation

Calculate the mean total score separately for each model:

**Mean total score = Sum of the 10 topic total scores / 10**

| Model | Sum of scores | Mean score out of 6 |
|---|---:|---:|
| Original GPT-2 | Pending | Pending |
| Fine-tuned GPT-2 | Pending | Pending |

The scores must be completed after reviewing the full outputs. No performance improvement is assumed in advance.

# 10. Output Observations

## Observation 1: Original GPT-2

For the Time Management prompt, the original GPT-2 generated:

"Use the time management tool to find the time you need to spend on your day."

The output was understandable but generic and repetitive.

## Observation 2: Fine-tuned GPT-2

For the Machine Learning topic, the application generated:

"Use the Machine Learning section of your course to learn more about machine-learning. This is a great way for students who are new to computer science..."

The output was related to the entered topic but was generic and incomplete.

## Observation 3: Information Security

The original GPT-2 generated a suggestion involving the Find button, while the fine-tuned model generated a VPN-related suggestion.

The adapted output repeated the same phrase several times.

## Observation 4: Microservices

The original model generated unrelated article text and sample code rather than a concise study tip.

This demonstrates that pretrained language models can sometimes produce text that is unrelated to the intended application.

## Observation 5: Cyber Ethics

The generated output included the generic sentence:

"Don't be afraid to ask questions."

The output was readable but did not provide a specific Cyber Ethics study suggestion.

# 11. Failure Analysis

One observed limitation was repetitive and partially irrelevant output.

For example, when testing Information Security, the fine-tuned model repeatedly generated:

"Use a VPN to avoid being tracked."

The Microservices output also included unrelated article text and code.

These observations demonstrate that the small training dataset did not provide enough diverse examples for reliable topic-specific generation.

Possible improvements include:

- Increasing the training dataset.
- Adding more diverse study-tip examples.
- Improving data quality.
- Experimenting with different training settings.
- Evaluating more prompts.
- Using suitable generation parameters to reduce repetitive output.

# 12. Application Demonstration

The application was developed using Streamlit.

## Main features

- Study topic input field.
- Generate Study Tip button.
- Fine-tuned GPT-2 model integration.
- Generated text display.
- Empty-input validation.
- Human-review disclosure.

## Application testing record

| Test | Expected behaviour | Result |
|---|---|---|
| Empty input | Display a warning | Pending confirmation |
| Machine Learning | Generate a study tip | Successful |
| Computer Networks | Generate a study tip | Pending confirmation |
| Time Management | Generate a study tip | Pending confirmation |

The Machine Learning test was successful. The remaining test results should be recorded after performing those tests in the browser.

# 13. Privacy, Bias and Limitations

## Privacy

The application processes the entered topic locally using the downloaded model. It does not require personal student information for its basic functionality.

## Bias

GPT-2 was pretrained on general internet text. Its generated suggestions may reflect biases or patterns present in its training data.

## Limitations

- Small training dataset.
- Repetitive generated text.
- Generic or incomplete suggestions.
- No guarantee of factual correctness.
- CPU-based execution can take time.
- Human review is necessary.

# 14. Conclusion

The project successfully demonstrates pretrained language-model loading, custom dataset preparation, GPT-2 fine-tuning, text generation, model evaluation and Streamlit application development.

The application generates study suggestions from user-provided academic topics.

The results also demonstrate that fine-tuning a large language model with a very small dataset has limitations, particularly in relevance, readability and usefulness.

# 15. Viva Questions and Answers

### Q1. Why did you select this dataset and model?

I selected GPT-2 because it is a pretrained autoregressive language model capable of generating text. I prepared a custom dataset of academic topics and study tips to adapt the model for an educational use case.

### Q2. What is GPT-2?

GPT-2 stands for Generative Pre-trained Transformer 2. It is a transformer-based language model that predicts the next token based on the previous tokens.

### Q3. What is fine-tuning?

Fine-tuning is the process of adapting a pretrained model to a specific task using a smaller task-specific dataset.

### Q4. What is a tokenizer?

A tokenizer converts text into smaller units called tokens that can be processed by a language model.

### Q5. Why did you use PyTorch?

PyTorch is a deep learning framework used to load, train and execute the GPT-2 model.

### Q6. Why did you use Streamlit?

Streamlit makes it possible to create an interactive web application using Python without building a separate frontend.

### Q7. What is the difference between the original and fine-tuned GPT-2?

The original model uses its pretrained parameters. The fine-tuned model has been further adapted using our custom study-tip examples.


### Q8. What is training loss?

Training loss measures the difference between the model's predicted next-token probabilities and the expected training tokens. A lower training loss generally indicates a better fit to the training data.

### Q9. Why did you use separate training and testing datasets?

The training dataset is used to adapt the model. The separate testing dataset helps evaluate its performance on topics it did not see during training.

### Q10. How did you evaluate the generated outputs?

I compared the original and fine-tuned GPT-2 outputs using relevance, readability and usefulness. Each criterion was scored from 0 to 2.

### Q11. What is one limitation of your project?

The training dataset contains only 15 examples. As a result, the fine-tuned model can generate repetitive, generic or incomplete suggestions.

### Q12. What is one future enhancement?

I would increase the size and diversity of the dataset and experiment with different language models and fine-tuning methods to improve output quality.

### Q13. Why is human review necessary?

Generative AI can produce inaccurate, incomplete or irrelevant text. A human should review the suggestions before students rely on them.

### Q14. What is an autoregressive language model?

An autoregressive language model generates text one token at a time by predicting the next token based on previously generated tokens.

### Q15. What is the role of Transformers?

The Hugging Face Transformers library provides pretrained models, tokenizers and training utilities that simplify working with GPT-2.

---

**End of Lab Record**
