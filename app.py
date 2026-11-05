
from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    words = text.split()
    return words

CORS(app, resources={
    r"/chat": {
        "origins": [
            "http://127.0.0.1:5500",
            "http://localhost:5500"
        ]
    }
})

@app.route("/")
def home():
    return send_from_directory(".", "index.html")
@app.route("/test-nlp", methods=["GET"])
def test_nlp():
    text = "HELLO! Welcome to SCSVMV University."
    words = preprocess_text(text)
    return jsonify({
        "original_text": text,
        "processed_words": words
    })

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "").lower()
    words = preprocess_text(message)

    if "admission" in words:
        reply = "Welcome to SCSVMV University! Please check the official university website for admission details."
    elif "course" in words or "courses" in words:
        reply = "SCSVMV offers various programmes. Please check the official university website for the latest course list."
    elif "exam" in words:
        reply = "For examination schedules and results, please check the official university examination section."
    elif "library" in words:
        reply = "The university library provides academic learning resources and reference materials."
    elif "hello" in words or "hi" in words:
        reply = "Hello! Welcome to SCSVMV University. How can I help you?"
    else:
        reply = "Sorry, I don't have that information yet. Please ask about admissions, courses, exams or library."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)

