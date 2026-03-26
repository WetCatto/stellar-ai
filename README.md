# Chat with John Benedict Pamat Supnet

A chatbot web app featuring **John Benedict Pamat Supnet** — a passionate biker from Mandug, exactly 5'11", obsessed with beauty queens, and deeply opinionated about everything else.

Built with Flask + Groq (free LLM API). Users just open the page and chat — no account or API key required on their end.

---

## Stack

- **Frontend** — Plain HTML/CSS/JS
- **Backend** — Python + Flask
- **LLM** — Groq API (free tier, `llama-3.3-70b-versatile`)

---

## Running Locally

**1. Clone the repo**
```bash
git clone https://github.com/your-username/stellar-ai.git
cd stellar-ai
```

**2. Get a free Groq API key**

Sign up at [console.groq.com](https://console.groq.com) — no credit card needed.

**3. Set up environment**
```bash
cp .env.example .env
# Open .env and paste your GROQ_API_KEY
```

**4. Install dependencies**
```bash
pip install -r requirements.txt
```

**5. Run**
```bash
python app.py
```

Open `http://localhost:5000` in your browser.

---

## Deploying for Free (Render.com)

1. Push this repo to GitHub
2. Go to [render.com](https://render.com) → **New Web Service** → connect your repo
3. Set the following in Render's environment variables:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```
4. Deploy — Render gives you a public URL to share

> **Note:** Render's free tier sleeps after 15 minutes of inactivity. The first message after idle may take ~30 seconds.

---

## Cost

| Who | Cost |
|-----|------|
| Users chatting | Free — no signup needed |
| You (hosting) | Free on Render free tier |
| You (API) | Free — Groq gives 6,000 requests/day |

---

## Project Structure

```
stellar-ai/
├── app.py            ← Flask backend
├── index.html        ← Chat UI
├── requirements.txt  ← Python dependencies
├── .env              ← Your API key (never commit this)
├── .env.example      ← Safe template to commit
├── .gitignore
└── README.md
```
