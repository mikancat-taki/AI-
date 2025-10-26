# server.py
from flask import Flask, request, jsonify
from ai.model_markov import MarkovAI
from ai.model_transformer import TransformerAI

app = Flask(__name__)

# インスタンス化
markov_ai = MarkovAI()
transformer_ai = TransformerAI()

@app.route('/')
def index():
    return "AI Server is running."

@app.route('/markov', methods=['POST'])
def run_markov():
    data = request.json
    text = data.get('text', '')
    result = markov_ai.generate(text)
    return jsonify({"result": result})

@app.route('/transformer', methods=['POST'])
def run_transformer():
    data = request.json
    text = data.get('text', '')
    result = transformer_ai.generate(text)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
