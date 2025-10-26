# ai/npnn.py
self.bh = np.zeros((1, hidden))
self.by = np.zeros((1, self.vocab_size))


def one_hot(self, idx):
v = np.zeros((1, self.vocab_size))
v[0, idx] = 1
return v


def softmax(self, x):
e = np.exp(x - np.max(x))
return e / e.sum(axis=1, keepdims=True)


def forward(self, inputs):
# inputs: list of indices
hs = [np.zeros((1,self.hidden))]
ys = []
ps = []
for t, idx in enumerate(inputs):
x = self.one_hot(idx)
h = np.tanh(x.dot(self.Wxh) + hs[-1].dot(self.Whh) + self.bh)
y = h.dot(self.Why) + self.by
p = self.softmax(y)
hs.append(h)
ys.append(y)
ps.append(p)
return hs, ys, ps


def sample(self, seed_char, length=200):
idx = self.char2i.get(seed_char, 0)
h = np.zeros((1,self.hidden))
out = seed_char
for _ in range(length):
x = self.one_hot(idx)
h = np.tanh(x.dot(self.Wxh) + h.dot(self.Whh) + self.bh)
y = h.dot(self.Why) + self.by
p = self.softmax(y)
idx = np.random.choice(range(self.vocab_size), p=p.ravel())
out += self.i2char[idx]
return out


def save(self, path):
params = { 'Wxh': self.Wxh.tolist(), 'Whh': self.Whh.tolist(), 'Why': self.Why.tolist(), 'bh': self.bh.tolist(), 'by': self.by.tolist(), 'chars': self.chars }
with open(path,'w',encoding='utf-8') as f:
json.dump(params,f)


def load(self, path):
with open(path,'r',encoding='utf-8') as f:
params = json.load(f)
self.chars = params['chars']
self.vocab_size = len(self.chars)
self.char2i = {c:i for i,c in enumerate(self.chars)}
self.i2char = {i:c for c,i in self.char2i.items()}
self.Wxh = np.array(params['Wxh'])
self.Whh = np.array(params['Whh'])
self.Why = np.array(params['Why'])
self.bh = np.array(params['bh'])
self.by = np.array(params['by'])
