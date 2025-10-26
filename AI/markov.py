# ai/markov.py
import random
import re
from collections import defaultdict


class MarkovAI:
def __init__(self):
self.memory = defaultdict(list)


def train(self, text):
words = re.findall(r"\w+|[。.,!?]|\S", text, flags=re.UNICODE)
for i in range(len(words) - 1):
self.memory[words[i]].append(words[i+1])


def generate(self, seed=None, length=40):
if not self.memory:
return ""
if seed is None or seed not in self.memory:
seed = random.choice(list(self.memory.keys()))
out = [seed]
for _ in range(length - 1):
choices = self.memory.get(out[-1], None)
if not choices:
break
out.append(random.choice(choices))
return "".join(out)
