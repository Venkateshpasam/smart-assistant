from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text):
    max_input = 1024
    inputs = text[:max_input]
    summary = summarizer(inputs, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']
