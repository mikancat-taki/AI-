# ai/model.py
import random
import re

class SimpleAI:
    def __init__(self):
        self.memory = {}

    def train(self, text):
        # 文を分割して単語のつながりを記録
        words = re.findall(r'\w+', text)
        for i in range(len(words) - 1):
            key = words[i].lower()
            next_word = words[i + 1]
            self.memory.setdefault(key, []).append(next_word)

    def generate(self, seed="こんにちは", length=20):
        seed = seed.lower()
        if seed not in self.memory:
            seed = random.choice(list(self.memory.keys()))
        result = [seed]
        for _ in range(length):
            next_words = self.memory.get(result[-1], [])
            if not next_words:
                break
            result.append(random.choice(next_words))
        return " ".join(result)
