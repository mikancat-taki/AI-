from flask import Flask, request, jsonify
from ai.model_markov import MarkovAI

app = Flask(__name__)
ai_model = MarkovAI()

# 例として事前学習
ai_model.train("こんにちは こんばんは さようなら またね")  

@app.route('/')
def index():
    return "AIサーバー稼働中"

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')
    if not prompt:
        return jsonify({"error": "promptが必要です"}), 400
    result = ai_model.generate(prompt)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
