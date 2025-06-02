import pickle
from gensim.models import Word2Vec
import numpy as np
import matplotlib.pyplot as plt
import umap

# Step 1: Load tokenized data
with open("tokens.pkl", "rb") as f:
    tokenized = pickle.load(f)

# Step 2: Train Word2Vec
model = Word2Vec(tokenized, vector_size=100, window=5, min_count=1, workers=4)

# Step 3: Embed sentences by averaging word vectors
def sentence_vector(sentence, model):
    vectors = [model.wv[word] for word in sentence if word in model.wv]
    return np.mean(vectors, axis=0) if vectors else np.zeros(model.vector_size)

embedded = np.array([sentence_vector(s, model) for s in tokenized])

# Step 4: Run UMAP
reduced = umap.UMAP(n_components=2, random_state=42).fit_transform(embedded)

# Step 5: Visualize
plt.figure(figsize=(10, 7))
plt.scatter(reduced[:, 0], reduced[:, 1], alpha=0.6)
plt.title("UMAP of SpongeBob Dialogue")
plt.xlabel("UMAP-1")
plt.ylabel("UMAP-2")
plt.tight_layout()
plt.show()
