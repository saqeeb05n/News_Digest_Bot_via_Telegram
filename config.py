import os
from dotenv import load_dotenv

load_dotenv()

NEWS_FEED_URLS = [
    "https://rss.cnn.com/rss/edition_world.rss",
    "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
    "https://feeds.bbci.co.uk/news/science_and_environment/rss.xml"
]

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
    raise ValueError("TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID not set in .env")

SUMMARY_MAX_LEN = 40
SUMMARY_MIN_LEN = 10
HISTORY_FILE = "data/history.json"
