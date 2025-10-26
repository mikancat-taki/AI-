import random
from collections import defaultdict

class MarkovAI:
    def __init__(self):
        self.model = defaultdict(list)

    def train(self, text):
        words = text.split()
        for i in range(len(words) - 1):
            self.model[words[i]].append(words[i + 1])

    def generate(self, start_word, length=20):
        if start_word not in self.model:
            start_word = random.choice(list(self.model.keys()))
        result = [start_word]
        for _ in range(length - 1):
            next_words = self.model.get(result[-1])
            if not next_words:
                break
            result.append(random.choice(next_words))
        return " ".join(result)
