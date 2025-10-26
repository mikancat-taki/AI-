import numpy as np

class SimpleNN:
    def __init__(self, input_size=8, hidden_size=8, output_size=8):
        self.W1 = np.random.randn(input_size, hidden_size) * 0.1
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, output_size) * 0.1
        self.b2 = np.zeros((1, output_size))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def forward(self, x):
        h = self.sigmoid(np.dot(x, self.W1) + self.b1)
        out = self.sigmoid(np.dot(h, self.W2) + self.b2)
        return out

    def predict(self, text):
        vec = np.array([[ord(c) % 64 for c in text[:8]]]) / 64.0
        out = self.forward(vec)
        return "Emotion Score: {:.3f}".format(np.mean(out))
