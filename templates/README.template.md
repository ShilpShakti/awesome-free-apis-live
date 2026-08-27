# 🇮🇳 India-Focused Free API Directory

![Health Check](https://github.com/OWNER/REPO/actions/workflows/health-check.yml/badge.svg)
![PR Validator](https://github.com/OWNER/REPO/actions/workflows/pr-validator.yml/badge.svg)
![Total APIs](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/OWNER/REPO/main/docs/badges/total.json)
![Reachable](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/OWNER/REPO/main/docs/badges/active.json)
![Avg Uptime](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/OWNER/REPO/main/docs/badges/uptime.json)

भारत-केंद्रित पब्लिक डेटा APIs और 100% फ्री डेवलपर यूटिलिटीज़ की एक सेल्फ-अपडेटिंग डायरेक्टरी।
हर एंट्री रोज़ाना ऑटोमेटेड हेल्थ-चेक से गुज़रती है — कोई भी टूटा हुआ लिंक ज्यादा देर तक लिस्ट में नहीं रहता।

🔴 **लाइव, सर्च करने लायक डैशबोर्ड:** `https://OWNER.github.io/REPO/` (GitHub Pages में `docs/` फोल्डर से enable करें)

> 🕒 **आखिरी अपडेट:** {{LAST_UPDATED}}

## नई API कैसे जोड़ें?

देखें [CONTRIBUTING.md](CONTRIBUTING.md) — बस एक YAML एंट्री जोड़कर PR भेजिए,
बॉट खुद उसे टेस्ट करके वैलिडेट करेगा।

## स्थिति (Status) के निशान

| निशान | मतलब |
|---|---|
| 🟢 | Active — बिना key के काम कर रहा है |
| 🟡 | Active लेकिन API Key ज़रूरी है |
| 🔴 | अभी डाउन (हाल की चेक में fail हुआ) |
| ⚪ | अभी तक टेस्ट नहीं हुआ |

---

{{GENERATED_CONTENT}}

---

## ⚙️ ऑप्शनल सेटअप

**1. लाइव डैशबोर्ड (GitHub Pages)**
Repo → Settings → Pages → Source: "Deploy from a branch" → Branch: `main`, Folder: `/docs`.
इसके बाद `https://<username>.github.io/<repo>/` पर सर्च व फ़िल्टर करने लायक लाइव स्टेटस पेज दिखेगा।

**2. Down/Recovered अलर्ट्स (Discord / Telegram)**
Repo → Settings → Secrets and variables → Actions → New repository secret में कोई भी जोड़ें:

| Secret नाम | कहाँ से मिलेगा |
|---|---|
| `DISCORD_WEBHOOK_URL` | Discord चैनल → Edit Channel → Integrations → Webhooks |
| `TELEGRAM_BOT_TOKEN` | Telegram पर [@BotFather](https://t.me/BotFather) से नया बॉट बनाकर |
| `TELEGRAM_CHAT_ID` | अपने ग्रुप/चैनल की chat id ([@userinfobot](https://t.me/userinfobot) से पता करें) |

कोई भी सीक्रेट सेट न करें तो भी सब कुछ सामान्य रूप से चलेगा — बस अलर्ट्स नहीं भेजे जाएंगे।

---

## लाइसेंस

यह प्रोजेक्ट [MIT License](LICENSE) के तहत है।
