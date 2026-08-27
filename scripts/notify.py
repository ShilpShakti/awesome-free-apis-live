#!/usr/bin/env python3
"""
notify.py
---------
जब कोई API 'down' हो जाती है (पहली बार) या 'down' से वापस 'active/key_required'
पर आती है (recovered), तो Discord webhook और/या Telegram bot पर अलर्ट भेजता है।

एनवायरनमेंट वेरिएबल्स (कोई भी सेट न हो तो वो चैनल चुपचाप स्किप हो जाता है):
  DISCORD_WEBHOOK_URL   -> Discord चैनल का incoming webhook URL
  TELEGRAM_BOT_TOKEN    -> Telegram बॉट का token (@BotFather से)
  TELEGRAM_CHAT_ID      -> जिस chat/group/channel में भेजना है

GitHub Actions में इन्हें Repo Settings -> Secrets and variables -> Actions
में जोड़ना होगा — कोड में कहीं भी hardcode नहीं है।
"""

import os
import requests

DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

TIMEOUT_SECONDS = 10


def _send_discord(message: str):
    if not DISCORD_WEBHOOK_URL:
        return
    try:
        requests.post(
            DISCORD_WEBHOOK_URL,
            json={"content": message},
            timeout=TIMEOUT_SECONDS,
        )
    except requests.RequestException as exc:
        print(f"⚠️ Discord अलर्ट भेजने में दिक्कत: {exc}")


def _send_telegram(message: str):
    if not (TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID):
        return
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        requests.post(
            url,
            json={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": message,
                "parse_mode": "Markdown",
                "disable_web_page_preview": True,
            },
            timeout=TIMEOUT_SECONDS,
        )
    except requests.RequestException as exc:
        print(f"⚠️ Telegram अलर्ट भेजने में दिक्कत: {exc}")


def notify_down(api_name: str, url: str, code):
    message = f"🔴 **{api_name}** डाउन हो गई है।\n{url}\nHTTP/Error: `{code}`"
    _send_discord(message)
    _send_telegram(message)


def notify_recovered(api_name: str, url: str):
    message = f"🟢 **{api_name}** वापस चालू हो गई है।\n{url}"
    _send_discord(message)
    _send_telegram(message)


def notifications_enabled() -> bool:
    return bool(DISCORD_WEBHOOK_URL or (TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID))
