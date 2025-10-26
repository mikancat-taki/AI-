# ai/memory.py
import json
from collections import deque


POSITIVE = ["うれ", "たの", "好き", "よかった", "楽しい", "最高"]
NEGATIVE = ["いや", "むか", "悲しい", "疲れ", "かなしい", "つら"]


class Memory:
def __init__(self, max_items=200, path='data/memory.json'):
self.history = deque(maxlen=max_items)
self.path = path
try:
with open(path,'r',encoding='utf-8') as f:
self.history.extend(json.load(f))
except Exception:
pass


def add(self, speaker, text):
item = { 'speaker': speaker, 'text': text }
self.history.append(item)
self._save()


def _save(self):
try:
with open(self.path,'w',encoding='utf-8') as f:
json.dump(list(self.history), f, ensure_ascii=False, indent=2)
except Exception:
pass


def get_recent(self, n=10):
return list(self.history)[-n:]


def emotion_score(self):
# naive heuristic
s = 0
for item in self.history:
text = item['text']
for p in POSITIVE:
if p in text:
s += 1
for q in NEGATIVE:
if q in text:
s -= 1
return max(-10, min(10, s))


def context_for_model(self, max_chars=500):
# return a short context string for model conditioning
out = ''
for item in self.get_recent(20):
out += f"{item['speaker']}: {item['text']}\n"
if len(out) > max_chars:
break
return out
