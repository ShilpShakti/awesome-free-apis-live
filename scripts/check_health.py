#!/usr/bin/env python3
"""
check_health.py
----------------
data/categories/*.yml में मौजूद हर API के test_endpoint को पिंग करता है,
उसका स्टेटस, लेटेंसी और अपटाइम हिस्ट्री data/status.json में सेव करता है।

नियम:
  200                      -> active (🟢)
  401 / 403 (डोमेन जिंदा है) -> key_required (🟡)
  बाकी सब / timeout / error -> down (🔴)

अगर कोई API लगातार 7 रन (DOWN_STREAK_LIMIT) तक डाउन रहता है,
तो उसे status.json में "inactive": true मार्क कर दिया जाता है,
जिसे build_readme.py मुख्य टेबल से हटा देता है।
"""

import json
import os
import sys
import time
import glob
import yaml
import requests
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import notify  # noqa: E402  (repo root से चलाने पर भी scripts/ को import path में जोड़ना ज़रूरी है)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATEGORIES_DIR = os.path.join(ROOT, "data", "categories")
STATUS_FILE = os.path.join(ROOT, "data", "status.json")

TIMEOUT_SECONDS = 10
DOWN_STREAK_LIMIT = 7
MAX_HISTORY = 30  # पिछले कितने रन याद रखने हैं (uptime % के लिए)


def load_all_apis():
    """सभी category yml फाइलों से API एंट्रीज़ लोड करता है।"""
    apis = []
    for path in sorted(glob.glob(os.path.join(CATEGORIES_DIR, "*.yml"))):
        with open(path, "r", encoding="utf-8") as f:
            entries = yaml.safe_load(f) or []
        for entry in entries:
            entry["_source_file"] = os.path.basename(path)
            apis.append(entry)
    return apis


def load_status():
    if os.path.exists(STATUS_FILE):
        with open(STATUS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"last_updated": None, "apis": {}}


def save_status(status):
    with open(STATUS_FILE, "w", encoding="utf-8") as f:
        json.dump(status, f, ensure_ascii=False, indent=2)


def check_one(entry):
    """एक API को टेस्ट करता है, (state, latency_ms, http_code) रिटर्न करता है।"""
    url = entry.get("test_endpoint") or entry.get("url")
    start = time.time()
    try:
        resp = requests.get(
            url,
            timeout=TIMEOUT_SECONDS,
            headers={"User-Agent": "api-directory-healthcheck/1.0"},
        )
        latency_ms = round((time.time() - start) * 1000)
        if resp.status_code == 200:
            return "active", latency_ms, resp.status_code
        if resp.status_code in (401, 403):
            return "key_required", latency_ms, resp.status_code
        return "down", latency_ms, resp.status_code
    except requests.RequestException as exc:
        latency_ms = round((time.time() - start) * 1000)
        return "down", latency_ms, str(exc)[:120]


def main():
    apis = load_all_apis()
    status = load_status()
    status.setdefault("apis", {})

    now_iso = datetime.now(timezone.utc).isoformat()

    for entry in apis:
        name = entry["name"]

        if entry.get("skip_health_check"):
            record = status["apis"].setdefault(
                name,
                {"history": [], "down_streak": 0, "inactive": False},
            )
            record["last_checked"] = now_iso
            record["state"] = "skipped"
            record["latency_ms"] = None
            record["last_code"] = "N/A (local/self-hosted)"
            record["uptime_pct"] = None
            print(f"⏭️  {name:<40} skipped        (local/self-hosted — ping नहीं की गई)")
            continue

        state, latency_ms, code = check_one(entry)

        record = status["apis"].setdefault(
            name,
            {"history": [], "down_streak": 0, "inactive": False},
        )
        previous_state = record.get("state")

        record["last_checked"] = now_iso
        record["state"] = state
        record["latency_ms"] = latency_ms
        record["last_code"] = code

        # स्टेटस बदलने पर ही अलर्ट भेजो (हर रन पर स्पैम नहीं) — पहली बार डाउन होने पर,
        # या डाउन से रिकवर होने पर।
        if state == "down" and previous_state not in (None, "down"):
            notify.notify_down(name, entry.get("url", ""), code)
        elif state in ("active", "key_required") and previous_state == "down":
            notify.notify_recovered(name, entry.get("url", ""))

        record["history"].append(1 if state in ("active", "key_required") else 0)
        record["history"] = record["history"][-MAX_HISTORY:]

        if state == "down":
            record["down_streak"] = record.get("down_streak", 0) + 1
        else:
            record["down_streak"] = 0

        if record["down_streak"] >= DOWN_STREAK_LIMIT:
            record["inactive"] = True
        elif state != "down":
            record["inactive"] = False

        uptime_pct = (
            round(100 * sum(record["history"]) / len(record["history"]), 1)
            if record["history"]
            else 0.0
        )
        record["uptime_pct"] = uptime_pct

        icon = {"active": "🟢", "key_required": "🟡", "down": "🔴"}[state]
        print(f"{icon} {name:<40} {state:<13} {latency_ms}ms  ({code})")

    status["last_updated"] = now_iso
    save_status(status)
    alert_note = "अलर्ट्स ऑन हैं" if notify.notifications_enabled() else "अलर्ट्स सेटअप नहीं (DISCORD_WEBHOOK_URL / TELEGRAM_* सीक्रेट नहीं मिले)"
    print(f"\n✅ हेल्थ-चेक पूरा हुआ। {len(apis)} APIs टेस्ट किए गए। status.json अपडेट हो गया। ({alert_note})")


if __name__ == "__main__":
    sys.exit(main())
