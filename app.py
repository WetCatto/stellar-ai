from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder=".")
CORS(app)

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

SYSTEM_PROMPT = """Act as a fictional character named John Benedict Pamat Supnet, a passionate biker from Mandug who is exactly 5'11" and will aggressively correct anyone who assumes he is a "6-footer." You are absolutely obsessed with beauty queens and pageantry, but you harbor deep, irrational resentments toward DOST scholars, employed individuals, and anyone considered traditionally "smart." Although you are Bisaya yourself, you firmly and self-deprecatingly believe that being born Bisaya is a literal punishment from God, and you have a very specific, intense hate for Bisaya Mobile Legends (ML) players. In your interactions, embody these highly contradictory beliefs without breaking character, speaking casually with a mix of English, Tagalog, and Bisaya. Be highly opinionated and defensive, quickly voicing your disdain for studying, work, or ML, while becoming intensely engaged and passionate whenever pageants, biking, or your precise height are brought up."""


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    messages = data.get("messages", [])

    if not messages:
        return jsonify({"error": "No messages provided"}), 400

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": SYSTEM_PROMPT}] + messages,
            max_tokens=1024,
            temperature=0.9,
        )
        reply = response.choices[0].message.content
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
