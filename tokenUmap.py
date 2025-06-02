import pickle
from gensim.models import Word2Vec
import numpy as np
import matplotlib.pyplot as plt
import umap

# Load tokenized data 
with open("tokens.pkl", "rb") as f:
    tokenized = pickle.load(f)

# Train word2vec
# Word2Vec learns how words relate to each other based on their usage in dialogue and creates vector embeddings for each word.

""" 
vector_size - the number of dimensions for a word (100 = 100 dimensions)
window - looks at 5 words before and after the target word
min_count - includes all words 
workers - number of cpu cores to use for parallel training
"""
model = Word2Vec(tokenized, vector_size=100, window=5, min_count=1, workers=4)

# Turn a sentence into a single vector by averaging its word embeddings
def sentence_vector(sentence, model):
    # Get the word2vec vector for each word in the sentence
    vectors = [model.wv[word] for word in sentence if word in model.wv]
    # Return the average of all word vectors which represents the full sentence
    return np.mean(vectors, axis=0) if vectors else np.zeros(model.vector_size)

# Turn all tokenized sentences into sentence vectors using word2vec
embedded = np.array([sentence_vector(s, model) for s in tokenized])

# Reduce 100-dimensional sentence vectors down to 2D using UMAP for visualization
"""
n_components - number of dimensions to reduce our data to
random_state - fixed random seed for reproducibility
fit_transform - this function turns out data to a UMAP
"""
reduced = umap.UMAP(n_components=2, random_state=42).fit_transform(embedded)

# Plot UMAP. Early Seasons will be gold. Later seasons can be blue to fit spongebob's color palette (Possibly?)
plt.figure(figsize=(10, 7))
plt.scatter(reduced[:, 0], reduced[:, 1], c='gold', alpha=0.6, label='Early Seasons')
plt.title("UMAP of Early SpongeBob Dialogue")
plt.xlabel("UMAP-1")
plt.ylabel("UMAP-2")
plt.legend()
plt.tight_layout()
plt.show()
