# server.py
from flask import Flask, request, render_template, jsonify
from model import SimpleAI

app = Flask(__name__)
ai = SimpleAI()
ai.train(open("data/dataset.txt", encoding="utf-8").read())

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    response = ai.generate(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
