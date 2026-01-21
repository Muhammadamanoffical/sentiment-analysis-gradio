# Sentiment Analysis using NLP and Gradio

This project implements a **Sentiment Analysis system** that classifies text into **Positive, Negative, or Neutral** sentiments using Natural Language Processing (NLP) techniques.  
The trained model is deployed as an interactive **Gradio web application** on **Hugging Face Spaces**.

---

## 🚀 Features
- Text preprocessing (cleaning, stopword removal)
- TF-IDF based feature extraction
- Logistic Regression sentiment classifier
- Interactive Gradio web interface
- Hugging Face deployment
- Pre-trained model loading (no retraining required)

---

## 📊 Dataset
The dataset contains social media text data with sentiment labels:
- **text** – input tweet/content
- **sentiment** – target label (Positive, Negative, Neutral)

Only the provided dataset was used for training and evaluation.

---

## 🧠 Model & Approach
- **Vectorization:** TF-IDF
- **Classifier:** Logistic Regression
- **Evaluation:** Train-test split
- **Deployment:** Gradio + Hugging Face Spaces

---

## 🖥️ Gradio Web App
Users can enter any text and instantly receive the predicted sentiment.

**Example Inputs:**
- *"I really love this product!"* → Positive
- *"This is the worst experience ever"* → Negative
- *"The meeting is scheduled for tomorrow"* → Neutral

---

