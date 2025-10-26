# ai/model_markov.py

class MarkovAI:
    def __init__(self):
        self.memory = []

    def generate_text(self, prompt: str) -> str:
        """
        ダミーのマルコフAIテキスト生成関数
        """
        self.memory.append(prompt)
        return f"[MarkovAI] {prompt} を受け取りました"
