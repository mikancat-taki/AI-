from flask import Flask, request, jsonify
from ai.model_markov import MarkovAI

app = Flask(__name__)
ai_model = MarkovAI()

@app.route('/')
def index():
    return "AI Server is running!"

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400
    
    response = ai_model.generate_text(prompt)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
