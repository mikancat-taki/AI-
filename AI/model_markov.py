# ai/model_markov.py

class MarkovAI:
    def __init__(self):
        # 必要なら初期データや辞書をここで用意
        self.memory = []

    def generate_text(self, prompt):
        """
        ダミーの文章生成関数。
        本来はマルコフ連鎖などのアルゴリズムで生成します。
        """
        # ここでは単純に入力を返すだけ
        self.memory.append(prompt)
        return f"[MarkovAI] {prompt} を受け取りました"
