import re
import nltk
import joblib
import gradio as gr

from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Load saved model
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

# Prediction
def predict_sentiment(text):
    cleaned = clean_text(text)
    vectorized = vectorizer.transform([cleaned])
    return model.predict(vectorized)[0]

# Gradio UI
demo = gr.Interface(
    fn=predict_sentiment,
    inputs=gr.Textbox(
        lines=4,
        placeholder="Enter tweet text here...",
        label="Tweet Text"
    ),
    outputs=gr.Label(label="Predicted Sentiment"),
    title="Tweet Sentiment Analysis",
    description="Sentiment classification using a pre-trained ML model."
)

demo.launch()
