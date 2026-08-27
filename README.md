# 🇮🇳 India-Focused Free API Directory

<p align="center">
  <img src="https://img.shields.io/badge/APIs-50+-blue?style=for-the-badge&logo=fastapi" alt="APIs Count" />
  <img src="https://img.shields.io/badge/Health%20Check-Automated%20Daily-brightgreen?style=for-the-badge&logo=githubactions" alt="Daily Check" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License" />
  <img src="https://img.shields.io/badge/Maintained%3F-Yes-orange?style=for-the-badge" alt="Maintained" />
</p>

<p align="center">
  ⭐ <b>If you find this list helpful, please star the repository!</b> ⭐
</p>

---

![Health Check](https://github.com/OWNER/REPO/actions/workflows/health-check.yml/badge.svg)
![PR Validator](https://github.com/OWNER/REPO/actions/workflows/pr-validator.yml/badge.svg)
![Total APIs](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/OWNER/REPO/main/docs/badges/total.json)
![Reachable](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/OWNER/REPO/main/docs/badges/active.json)
![Avg Uptime](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/OWNER/REPO/main/docs/badges/uptime.json)

भारत-केंद्रित पब्लिक डेटा APIs और 100% फ्री डेवलपर यूटिलिटीज़ की एक सेल्फ-अपडेटिंग डायरेक्टरी।
हर एंट्री रोज़ाना ऑटोमेटेड हेल्थ-चेक से गुज़रती है — कोई भी टूटा हुआ लिंक ज्यादा देर तक लिस्ट में नहीं रहता।

🔴 **लाइव, सर्च करने लायक डैशबोर्ड:** `https://OWNER.github.io/REPO/` (GitHub Pages में `docs/` फोल्डर से enable करें)

> 🕒 **आखिरी अपडेट:** 2026-08-27T20:30:40.849786+00:00

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

### AI / ML

| API नाम | विवरण | ऑथेंटिकेशन | HTTPS | CORS | स्थिति |
|---|---|---|---|---|---|
| [Groq Cloud API](https://groq.com) | Llama3/Mistral पर सुपरफास्ट AI टेक्स्ट जेनरेशन — 100% फ्री टियर। | API Key (Free Tier) | ✅ | ✅ | 🟡 100.0% Key Reqd |
| [Hugging Face Serverless Inference](https://huggingface.co/docs/api-inference) | हज़ारों ओपन-सोर्स मॉडल्स (टेक्स्ट, ऑडियो, इमेज) को मुफ्त में रन करें। | API Key (Free) | ✅ | ✅ | 🔴 0.0% Down |
| [Ollama Local REST API](http://localhost:11434/api) ⓘ | अपने कंप्यूटर/सर्वर पर बिना इंटरनेट LLM रन करने का स्टैंडर्ड फॉर्मेट। | None (Localhost / Self-hosted) | ❌ | ❌ | ℹ️ Self-hosted (not checked) |
| [LibreTranslate](https://libretranslate.com) | भाषाओं का मुफ्त, ओपन-सोर्स अनुवाद API। | None / Self-hosted | ✅ | ✅ | 🔴 0.0% Down |
| [OpenRouter API](https://openrouter.ai) | एक ही API से 100+ LLM मॉडल्स (कई फ्री मॉडल्स सहित) तक पहुंच। | None (models list) / API Key (completions के लिए) | ✅ | ✅ | 🟢 100.0% Up |
| [Cohere API](https://cohere.com) | टेक्स्ट जेनरेशन, एम्बेडिंग्स और क्लासिफिकेशन के लिए फ्री ट्रायल टियर। | API Key (Free trial) | ✅ | ✅ | 🟡 100.0% Key Reqd |
| [Wit.ai (Meta NLU)](https://wit.ai) | Meta का फ्री नेचुरल लैंग्वेज अंडरस्टैंडिंग (intent/entity extraction) API। | API Key (Free — Facebook account से) | ✅ | ✅ | 🔴 0.0% Down |
| [Together AI](https://www.together.ai) | ओपन-सोर्स LLMs (Llama, Mixtral आदि) के लिए फ्री-क्रेडिट इन्फरेंस API। | API Key (Free credits on signup) | ✅ | ✅ | 🟡 100.0% Key Reqd |


<details><summary>ⓘ नोट्स देखें</summary>

- **Ollama Local REST API**: यह लोकल/सेल्फ-होस्टेड API है — पब्लिक इंटरनेट से पिंग नहीं हो सकती, इसलिए डेली हेल्थ-चेक में शामिल नहीं है।

</details>

### Developer Utilities & Mock Data

| API नाम | विवरण | ऑथेंटिकेशन | HTTPS | CORS | स्थिति |
|---|---|---|---|---|---|
| [JSONPlaceholder](https://jsonplaceholder.typicode.com) | टेस्टिंग और UI बनाने के लिए डमी पोस्ट, यूज़र्स और कमेंट्स। | None | ✅ | ✅ | 🟢 100.0% Up |
| [DummyJSON](https://dummyjson.com) | ई-कॉमर्स प्रोडक्ट्स, कार्ट और यूज़र डेटा का डमी मॉक। | None | ✅ | ✅ | 🟢 100.0% Up |
| [IPify](https://www.ipify.org) | यूज़र का पब्लिक IP एड्रेस पता करना। | None | ✅ | ✅ | 🟢 100.0% Up |
| [Open-Meteo Weather API](https://open-meteo.com) | बिना किसी API Key के सटीक मौसम और तापमान डेटा। | None | ✅ | ✅ | 🟢 100.0% Up |
| [Shields.io Badges](https://shields.io) | डायनामिक बैज और स्टेटस इमेज जनरेट करना (README badges आदि के लिए)। | None | ✅ | ✅ | 🟢 100.0% Up |
| [REST Countries](https://restcountries.com) | दुनिया के देशों की मुद्रा, राजधानी, झंडा और जनसंख्या डेटा। | None | ✅ | ✅ | 🟢 100.0% Up |
| [CoinGecko Simple Price API](https://www.coingecko.com/api) | लाइव क्रिप्टोकरेंसी और फॉरेक्स रेट्स (INR सहित)। | None (Free Demo Tier) | ✅ | ✅ | 🟢 100.0% Up |
| [ExchangeRate-API](https://open.er-api.com/v6/latest/USD) | अंतरराष्ट्रीय मुद्राओं की लाइव एक्सचेंज दरें। | None | ✅ | ✅ | 🟢 100.0% Up |
| [QR Code Generator (goqr.me)](https://api.qrserver.com) | किसी भी टेक्स्ट/लिंक से तुरंत QR कोड इमेज बनाना। | None | ✅ | ✅ | 🟢 100.0% Up |
| [Agify.io](https://agify.io) | नाम के आधार पर उम्र का अनुमान लगाने वाला डेटा। | None | ✅ | ✅ | 🟢 100.0% Up |
| [Universities List API](http://universities.hipolabs.com) | भारत और दुनिया भर के विश्वविद्यालयों की लिस्ट और डोमेन। | None | ❌ | ✅ | 🟢 100.0% Up |
| [Numbers API](http://numbersapi.com) | किसी भी नंबर के बारे में रोचक तथ्य, तारीख और गणित ट्रिविया। | None | ❌ | ✅ | 🔴 0.0% Down |
| [Cat Facts API](https://catfact.ninja) | बिल्लियों के बारे में रैंडम मज़ेदार तथ्य। | None | ✅ | ✅ | 🟢 100.0% Up |
| [Dog CEO API](https://dog.ceo/dog-api) | नस्ल के हिसाब से कुत्तों की रैंडम तस्वीरें (image URLs)। | None | ✅ | ✅ | 🟢 100.0% Up |
| [Advice Slip API](https://api.adviceslip.com) | रैंडम एक-लाइन सलाह/सुझाव जनरेट करना। | None | ✅ | ✅ | 🟢 100.0% Up |
| [JokeAPI](https://v2.jokeapi.dev) | प्रोग्रामिंग, डार्क और मिस्क जोक्स — कैटेगरी व फिल्टर के साथ। | None | ✅ | ✅ | 🟢 100.0% Up |
| [Open Trivia Database](https://opentdb.com) | क्विज़ ऐप्स के लिए हज़ारों वेरिफाइड ट्रिविया सवाल। | None | ✅ | ✅ | 🟢 100.0% Up |
| [Public Holiday API (Nager.Date)](https://date.nager.at) | किसी भी देश (भारत सहित) की सार्वजनिक छुट्टियों की लिस्ट। | None | ✅ | ✅ | 🔴 0.0% Down |
| [IPAPI - IP Geolocation](https://ipapi.co) | IP एड्रेस से जिओ-लोकेशन (शहर, देश, टाइमज़ोन) जानकारी निकालें। | None | ✅ | ✅ | 🟢 100.0% Up |
| [Random User Generator](https://randomuser.me) | टेस्टिंग के लिए फेक यूज़र प्रोफाइल्स (नाम, फोटो, पता) जनरेट करना। | None | ✅ | ✅ | 🟢 100.0% Up |
| [PokeAPI](https://pokeapi.co) | पोकेमॉन डेटा (स्टैट्स, मूव्स, टाइप्स) — API टेस्टिंग के लिए लोकप्रिय। | None | ✅ | ✅ | 🟢 100.0% Up |

### India Public Data

| API नाम | विवरण | ऑथेंटिकेशन | HTTPS | CORS | स्थिति |
|---|---|---|---|---|---|
| [India Post Pincode API](https://api.postalpincode.in) | भारत के किसी भी पिनकोड या डाकघर का विवरण खोजें। | None | ✅ | ✅ | 🟢 100.0% Up |
| [Indian Railway Train Route / Live Status](https://erail.in) ⓘ | ट्रेन शेड्यूल और स्टेशन कोड की जानकारी (unofficial open mirror)। | None / API Key (mirror dependent) | ✅ | ❌ | 🟢 100.0% Up |
| [data.gov.in Mandi Prices API](https://api.data.gov.in) | देशभर की मंडियों में फसलों का दैनिक भाव (Open Government Data)। | API Key (Free Gov Sign-up) | ✅ | ✅ | 🔴 0.0% Down |
| [eCourts Public Case Status](https://ecourts.gov.in) ⓘ | ज़िला और उच्च न्यायालयों के केस स्टेटस व कॉज़ लिस्ट का ओपन डेटा। | None / Scraping Endpoints | ✅ | ❌ | 🟢 100.0% Up |
| [ISRO Spacecraft / Launchers API](https://isro.vercel.app/api/spacecrafts) | इसरो के सभी सैटेलाइट और रॉकेट लॉन्च का पब्लिक डेटा। | None | ✅ | ✅ | 🟢 100.0% Up |
| [IFSC Code Lookup (Razorpay)](https://ifsc.razorpay.com) | बैंक की IFSC कोड डिटेल्स (ब्रांच, बैंक नाम, पता) निकालें। | None | ✅ | ✅ | 🟢 100.0% Up |
| [WAQI Air Quality Index API](https://aqicn.org/api) | भारत के शहरों सहित दुनिया भर का लाइव एयर क्वालिटी इंडेक्स (AQI)। | API Key (Free, instant) | ✅ | ✅ | 🟢 100.0% Up |
| [India States & Districts JSON](https://github.com/sab99r/Indian-States-And-Districts) | भारत के सभी राज्यों और ज़िलों की स्टैटिक JSON लिस्ट (community-maintained)। | None | ✅ | ✅ | 🟢 100.0% Up |


<details><summary>ⓘ नोट्स देखें</summary>

- **Indian Railway Train Route / Live Status**: यह ऑफिशियल भारतीय रेलवे API नहीं है, ओपन मिरर है — स्थिरता की गारंटी नहीं।
- **eCourts Public Case Status**: आधिकारिक पोर्टल है पर सीधी 'API' नहीं — ओपन मिरर/स्क्रैपिंग एंडपॉइंट पर निर्भर।

</details>

### Media, News & Fun

| API नाम | विवरण | ऑथेंटिकेशन | HTTPS | CORS | स्थिति |
|---|---|---|---|---|---|
| [NewsAPI.org](https://newsapi.org) | दुनिया भर (भारत सहित) के 80,000+ न्यूज़ सोर्सेज़ से हेडलाइन्स। | API Key (Free tier — dev use) | ✅ | ✅ | 🟡 100.0% Key Reqd |
| [TMDB (The Movie Database)](https://www.themoviedb.org/documentation/api) | फिल्मों, TV शोज़ और कलाकारों का विशाल, फ्री डेटाबेस। | API Key (Free) | ✅ | ✅ | 🟡 100.0% Key Reqd |
| [NASA APOD (Astronomy Picture of the Day)](https://api.nasa.gov) | नासा की रोज़ाना खगोलीय तस्वीर, विवरण के साथ। | API Key (DEMO_KEY से बिना साइन-अप टेस्ट कर सकते हैं) | ✅ | ✅ | 🟢 100.0% Up |
| [Chuck Norris Jokes API](https://api.chucknorris.io) | रैंडम Chuck Norris जोक्स — कैटेगरी फिल्टर के साथ। | None | ✅ | ✅ | 🟢 100.0% Up |
| [TVMaze API](https://www.tvmaze.com/api) | TV शोज़, एपिसोड्स, कास्ट और शेड्यूल का ओपन डेटा। | None | ✅ | ✅ | 🟢 100.0% Up |

### Security, Network & Public Tools

| API नाम | विवरण | ऑथेंटिकेशन | HTTPS | CORS | स्थिति |
|---|---|---|---|---|---|
| [Cloudflare 1.1.1.1 DNS over HTTPS](https://cloudflare-dns.com/dns-query) ⓘ | प्रोग्रामेटिक DNS रिकॉर्ड्स और डोमेन रिज़ॉल्यूशन। | None | ✅ | ✅ | 🔴 0.0% Down |
| [Have I Been Pwned (k-Anonymity Range Check)](https://haveibeenpwned.com/API/v3) | पासवर्ड लीक हुआ है या नहीं, सुरक्षित तरीके से (k-anonymity) जांचना। | None | ✅ | ✅ | 🟢 100.0% Up |
| [RoboHash](https://robohash.org) | किसी भी टेक्स्ट या आईडी से यूनीक रोबोट/मॉन्स्टर प्रोफाइल फोटो बनाना। | None | ✅ | ✅ | 🔴 0.0% Down |
| [Bored API](https://bored-api.appbrewery.com) | रैंडम टास्क्स और एक्टिविटीज़ का JSON डेटा (बोरियत दूर करने के लिए)। | None | ✅ | ✅ | 🟢 100.0% Up |
| [Open Library Books API](https://openlibrary.org/developers/api) | दुनिया भर की किताबों का ISBN, लेखक और पब्लिशर डेटा। | None | ✅ | ✅ | 🔴 0.0% Down |
| [SSL Labs API](https://www.ssllabs.com/projects/ssllabs-apis) | किसी भी डोमेन के SSL/TLS सर्टिफिकेट की डिटेल्ड सिक्योरिटी ग्रेडिंग। | None | ✅ | ✅ | 🟢 100.0% Up |
| [AbuseIPDB](https://www.abuseipdb.com) | किसी IP एड्रेस की abuse/spam रिपोर्ट्स और रिस्क स्कोर चेक करना। | API Key (Free tier) | ✅ | ✅ | 🟡 100.0% Key Reqd |
| [VirusTotal API](https://docs.virustotal.com/reference/overview) | फाइल/URL/IP को 70+ एंटीवायरस इंजनों से स्कैन कराना। | API Key (Free tier) | ✅ | ✅ | 🟡 100.0% Key Reqd |


<details><summary>ⓘ नोट्स देखें</summary>

- **Cloudflare 1.1.1.1 DNS over HTTPS**: रिक्वेस्ट में हेडर 'Accept: application/dns-json' ज़रूरी है।

</details>


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
