from datetime import datetime
from news.fetcher import fetch_latest_articles
from summarizer.summarizer import summarize_article
from telegram_bot.sender import send_to_telegram

def main():
    print("🚀 Starting Offline News Digest Bot...")
    articles = fetch_latest_articles()

    if not articles:
        print("✅ No new articles found.")
        return

    summaries = []
    for art in articles:
        summarized = summarize_article(art)
        summaries.append(f"📰 *{art['title']}*\n{summarized}\n🔗 {art['link']}\n")

    digest = "\n\n".join(summaries)
    header = f"🗞️ *Daily News Digest* ({datetime.now().strftime('%d %b %Y')})\n\n"
    final_message = header + digest

    print("📤 Sending to Telegram...")
    send_to_telegram(final_message)
    print("✅ Digest sent successfully!")

if __name__ == "__main__":
    main()
