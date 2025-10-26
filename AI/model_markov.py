import random, re

class MarkovAI:
    def __init__(self):
        self.memory = {}
    def train(self, text):
        words = re.findall(r'\w+', text)
        for i in range(len(words)-1):
            key = words[i].lower()
            self.memory.setdefault(key, []).append(words[i+1])
    def generate(self, seed="こんにちは", length=15):
        seed = seed.lower()
        if seed not in self.memory:
            seed = random.choice(list(self.memory.keys()))
        result = [seed]
        for _ in range(length):
            nexts = self.memory.get(result[-1], [])
            if not nexts: break
            result.append(random.choice(nexts))
        return " ".join(result)
