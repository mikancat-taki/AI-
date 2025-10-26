# ai/transformer.py
for _ in range(n_layer):
layer = {
'Wq': np.random.randn(n_embd, n_embd)*0.01,
'Wk': np.random.randn(n_embd, n_embd)*0.01,
'Wv': np.random.randn(n_embd, n_embd)*0.01,
'Wo': np.random.randn(n_embd, n_embd)*0.01,
'W1': np.random.randn(n_embd, 4*n_embd)*0.01,
'W2': np.random.randn(4*n_embd, n_embd)*0.01,
'ln1_a': np.ones((1,n_embd)), 'ln1_b': np.zeros((1,n_embd)),
'ln2_a': np.ones((1,n_embd)), 'ln2_b': np.zeros((1,n_embd))
}
self.layers.append(layer)
self.ln_f_a = np.ones((1,n_embd)); self.ln_f_b = np.zeros((1,n_embd))
self.head = np.random.randn(n_embd, vocab_size)*0.01


def layer_norm(self, x, a, b, eps=1e-5):
mu = x.mean(axis=-1, keepdims=True)
sigma = x.std(axis=-1, keepdims=True)
return a * (x - mu) / (sigma + eps) + b


def forward(self, idx):
# idx: (T,) token indices
T = len(idx)
x = self.tok_emb[idx] + self.pos_emb[:T]
# transformer blocks
for layer in self.layers:
x_ln = self.layer_norm(x, layer['ln1_a'], layer['ln1_b'])
q = x_ln.dot(layer['Wq'])
k = x_ln.dot(layer['Wk'])
v = x_ln.dot(layer['Wv'])
# scaled dot-product attention (naive)
scores = q.dot(k.T) / np.sqrt(self.n_embd)
# causal mask
mask = np.tril(np.ones((T,T)))
scores = np.where(mask==1, scores, -1e9)
att = softmax(scores)
a = att.dot(v)
x = x + a.dot(layer['Wo'])
# MLP
x_ln2 = self.layer_norm(x, layer['ln2_a'], layer['ln2_b'])
m = gelu(x_ln2.dot(layer['W1']))
m = m.dot(layer['W2'])
x = x + m
x = self.layer_norm(x, self.ln_f_a, self.ln_f_b)
logits = x.dot(self.head)
return logits




def softmax(x):
e = np.exp(x - np.max(x, axis=-1, keepdims=True))
return e / e.sum(axis=-1, keepdims=True)
