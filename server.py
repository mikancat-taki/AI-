from flask import Flask, render_template, request, jsonify
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "ai"))

from ai.model_markov import MarkovAI
from ai.model_transformer import TransformerAI
from model_nn import SimpleNN
from model_transformer import TinyTransformer
from memory import MemoryModule
from emotion import EmotionModule

app = Flask(__name__)

markov = MarkovAI()
nn = SimpleNN()
transformer = TinyTransformer()
memory = MemoryModule()
emotion = EmotionModule()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]
    memory.remember(user_msg)
    emotion.update(user_msg)
    reply = markov.generate(user_msg, 10)
    reply += " | " + nn.predict(user_msg)
    reply += " | " + emotion.summary()
    reply += " | " + transformer.generate(user_msg)
    return jsonify({"reply": reply, "memory": memory.recall()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
