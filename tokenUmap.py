import pickle
from gensim.models import Word2Vec
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import umap
import seaborn as sns
import csv


# Load tokenized data 
with open("tokensOld.pkl", "rb") as f:
    tokenized1 = pickle.load(f)

with open("tokensNew.pkl", "rb") as f:
    tokenized2 = pickle.load(f)
    
    
tokenized = tokenized1 + tokenized2


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

# this is how density is calculated 
xy = np.vstack([reduced[:, 0], reduced[:, 1]])
density = gaussian_kde(xy)(xy)

# Plot UMAP. Early Seasons will be gold. Later seasons can be blue to fit spongebob's color palette (Possibly?)
plt.figure(figsize=(10, 7))
plt.scatter(reduced[:, 0], reduced[:, 1], alpha=0.6, c = density, label='2D Condensesed Data Points')
plt.title("UMAP of SpongeBob Dialogue")
plt.xlabel("UMAP-1")
plt.ylabel("UMAP-2")
plt.legend()
plt.tight_layout()


# sns.scatterplot(x = reduced[:,0], y = reduced[:,1])
# plt.show()

# sns.kdeplot(x=reduced[:, 0], y=reduced[:, 1], cmap='plasma', fill=True, alpha=0.6)
# sns.kdeplot(x=reduced[:, 0], y=reduced[:, 1], color='white', alpha=0.4, linewidths=0.5)

plt.show()