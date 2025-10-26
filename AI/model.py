# model.py
import random

class SimpleAI:
    def __init__(self):
        self.memory = {}

    def train(self, text):
        words = text.split()
        for i in range(len(words)-1):
            key, next_word = words[i], words[i+1]
            self.memory.setdefault(key, []).append(next_word)

    def generate(self, start_word="こんにちは", length=20):
        if start_word not in self.memory:
            start_word = random.choice(list(self.memory.keys()))
        output = [start_word]
        for _ in range(length):
            next_words = self.memory.get(output[-1], [])
            if not next_words: break
            output.append(random.choice(next_words))
        return " ".join(output)
