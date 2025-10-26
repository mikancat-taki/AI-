from flask import Flask, request, jsonify
from ai.model_markov import MarkovAI  # ここが ai/に変更済みで正しい

app = Flask(__name__)
ai_model = MarkovAI()  # インスタンス作成

@app.route('/')
def index():
    return "AIサーバー稼働中"

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')
    if not prompt:
        return jsonify({"error": "promptが必要です"}), 400
    
    result = ai_model.generate(prompt)  # MarkovAI の generate メソッドを呼ぶ
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
