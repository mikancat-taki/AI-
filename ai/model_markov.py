# ai/model_markov.py
import random

class MarkovAI:
    def __init__(self):
        self.chain = {}

    def train(self, text):
        words = text.split()
        for i in range(len(words) - 1):
            if words[i] not in self.chain:
                self.chain[words[i]] = []
            self.chain[words[i]].append(words[i + 1])

    def generate(self, prompt, length=20):
        words = prompt.split()
        if not words:
            return ""
        current = words[-1]
        result = words[:]
        for _ in range(length):
            next_words = self.chain.get(current)
            if not next_words:
                break
            current = random.choice(next_words)
            result.append(current)
        return ' '.join(result)
