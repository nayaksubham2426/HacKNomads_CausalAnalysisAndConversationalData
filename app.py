from flask import Flask, request, jsonify
from flask_cors import CORS
from task1 import generate_explanation
from task2 import update_context

app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
    return "Causal Conversation Analysis Backend is running"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    message = data.get("message")


    result = generate_explanation(message)

    update_context(message, result["predicted_event"], result["supporting_cases"])

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True,port=5000)