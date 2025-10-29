import os
import json
import feedparser
from config import NEWS_FEED_URLS, HISTORY_FILE

# Ensure data folder exists
os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)

def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                data = f.read().strip()
                return json.loads(data) if data else []
        except json.JSONDecodeError:
            return []
    else:
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            f.write("[]")
        return []

def save_history(history):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)

def fetch_latest_articles(limit_per_feed=3):
    articles = []
    history = load_history()

    for url in NEWS_FEED_URLS:
        feed = feedparser.parse(url)
        for entry in feed.entries[:limit_per_feed]:
            if entry.title not in history:
                articles.append({
                    "title": entry.title,
                    "summary": entry.summary if "summary" in entry else "",
                    "link": entry.link
                })
                history.append(entry.title)

    save_history(history)
    return articles
