from transformers import pipeline
from config import SUMMARY_MAX_LEN, SUMMARY_MIN_LEN

print("Loading summarizer model...")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_article(article):
    text = f"{article['title']}. {article['summary']}"
    max_len = min(len(text), SUMMARY_MAX_LEN)
    try:
        summary = summarizer(text, max_length=max_len, min_length=SUMMARY_MIN_LEN, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"(Could not summarize) {article['title']}"
