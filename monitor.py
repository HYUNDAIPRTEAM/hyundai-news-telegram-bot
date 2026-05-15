import requests
import feedparser
from urllib.parse import quote
from datetime import datetime
from zoneinfo import ZoneInfo

KST = ZoneInfo("Asia/Seoul")

# 텔레그램 설정
BOT_TOKEN = "8888421467:AAEB9TC5IS0Ag81C4lIpmMZrUTDWfZi8hfU"
CHAT_ID = "8656367638"

# 키워드
KEYWORDS = ["현정은", "현대엘리베이터", "현대무벡스"]

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, data=payload)

def get_google_news(query):
    url = f"https://news.google.com/rss/search?q={quote(query)}&hl=ko&gl=KR&ceid=KR:ko"

    feed = feedparser.parse(url)

    return feed.entries[:5]

# 현재 시간
now = datetime.now(KST).strftime("%Y-%m-%d %H:%M")

message = f"📢 HYUNDAI NEWS MONITORING\n업데이트 시간: {now}\n\n"

for kw in KEYWORDS:

    message += f"\n🔍 {kw}\n"

    news = get_google_news(kw)

    for entry in news:

        title = entry.title
        link = entry.link

        message += f"\n• {title}\n{link}\n"

# 텔레그램 발송
send_telegram(message)

print("텔레그램 전송 완료")
