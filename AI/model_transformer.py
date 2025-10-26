class TinyTransformer:
    def __init__(self):
        self.trained = False
    def train(self, text):
        self.trained = True
    def generate(self, text):
        return "（Transformer応答）"
