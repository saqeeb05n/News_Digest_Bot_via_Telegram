# News Digest Bot via Telegram

A Telegram bot that fetches news articles via APIs, processes and summarizes them, and delivers the results to users on Telegram.

---

## Features

- Fetches news items from one or more news APIs.  
- Summarizes articles into concise messages.  
- Sends summarized news to Telegram channels or users.  
- Configurable via a configuration file (`config.py`).  
- Easy to deploy locally or on a cloud server.

---

## Tech Stack

- Python 3.x  
- Telegram Bot API (via `python-telegram-bot` or similar)  
- News API integration (e.g., NewsAPI, RSS feeds)  
- Natural language processing for summarization (simple heuristics or libraries)  
- Git and deployment scripts (optional)

---

## Prerequisites

Before you begin, make sure you have:

- Python 3.8 or newer  
- A Telegram Bot token (created via BotFather)  
- One or more news API keys (e.g., [NewsAPI.org](https://newsapi.org))  
- Git (if you plan to clone the repository)  

---

## Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/saqeeb05n/News_Digest_Bot_via_Telegram.git
   cd News_Digest_Bot_via_Telegram

2. **Install Python dependencies**

> pip install -r requirements.txt

3. **Configuration**

Open the config.py file in the project root.

Add or update the following configuration parameters:

TELEGRAM_TOKEN = "your-telegram-bot-token-here" 
NEWS_API_KEY = "your-newsapi-key-here" 
TARGET_CHAT_ID = "telegram-chat-id-or-channel-id" 

Save the configuration file.

4. **Run the bot**
  > python main.py
