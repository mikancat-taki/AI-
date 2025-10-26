import numpy as np

class TinyTransformer:
    def __init__(self, vocab_size=256, dim=32, context=16):
        self.Wq = np.random.randn(dim, dim)
        self.Wk = np.random.randn(dim, dim)
        self.Wv = np.random.randn(dim, dim)
        self.Wo = np.random.randn(dim, dim)
        self.emb = np.random.randn(vocab_size, dim)
        self.pos = np.random.randn(context, dim)

    def softmax(self, x):
        e = np.exp(x - np.max(x))
        return e / e.sum(axis=-1, keepdims=True)

    def forward(self, tokens):
        x = self.emb[tokens] + self.pos[:len(tokens)]
        q = x @ self.Wq
        k = x @ self.Wk
        v = x @ self.Wv
        att = self.softmax(q @ k.T / np.sqrt(k.shape[-1]))
        out = att @ v
        return np.mean(out @ self.Wo, axis=0)

    def generate(self, text):
        tokens = np.array([ord(c) % 255 for c in text[-16:]])
        rep = self.forward(tokens)
        idx = int(np.mean(rep) * 255) % 255
        return text + chr(idx)
