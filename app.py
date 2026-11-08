
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import re
import os

app = Flask(__name__)
CORS(app)


def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text.split()


@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/style.css")
def style():
    return send_from_directory(".", "style.css")


@app.route("/script.js")
def script():
    return send_from_directory(".", "script.js")


@app.route("/test-nlp", methods=["GET"])
def test_nlp():
    text = "HELLO! Welcome to SCSVMV University."

    return jsonify({
        "original_text": text,
        "processed_words": preprocess_text(text)
    })


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json(silent=True) or {}

    message = data.get("message", "").strip()

    if not message:
        return jsonify({
            "reply": "Please enter a question."
        }), 400

    words = preprocess_text(message)

    if "hello" in words or "hi" in words:
        reply = "Hello! Welcome to SCSVMV University. How can I help you?"

    elif "admission" in words or "admissions" in words:
        reply = "Welcome to SCSVMV University! Please check the official university website for admission details."

    elif "course" in words or "courses" in words:
        reply = "SCSVMV offers various programmes. Please check the official university website for the latest course list."

    elif "exam" in words or "exams" in words:
        reply = "Please check the university examination section for schedules and results."

    elif "library" in words:
        reply = "The university library provides academic learning resources."

    elif "fee" in words or "fees" in words:
        reply = "Please contact the university administration for the latest fee details."

    elif "contact" in words:
        reply = "Please visit the official SCSVMV University website for contact information."

    else:
        reply = "Sorry, I don't have that information yet. Ask about admissions, courses, exams or library."

    return jsonify({
        "reply": reply
    })


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=int(os.environ.get("PORT", 5000)),
        debug=True
    )
