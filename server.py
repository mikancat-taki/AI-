from flask import Flask, render_template, request, jsonify
from ai.model_markov import MarkovAI
from ai.model_nn import SimpleNN
from ai.model_transformer import TinyTransformer
from ai.memory import MemoryModule

app = Flask(__name__)

# ===== AI モジュール初期化 =====
markov = MarkovAI()
nn = SimpleNN()
transformer = TinyTransformer()
memory = MemoryModule()

# ===== データ学習 =====
try:
    text = open("data/dataset.txt", encoding="utf-8").read()
    markov.train(text)
    nn.train_on_text(text)
    transformer.train(text)
except Exception as e:
    print("初期学習失敗:", e)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json["message"]
    memory.add_user_message(msg)
    response = markov.generate(msg)
    memory.add_bot_message(response)
    emotion = memory.get_emotion_state()
    return jsonify({
        "response": f"[{emotion}] {response}"
    })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
