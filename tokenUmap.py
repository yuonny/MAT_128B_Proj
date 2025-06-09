import pickle
from gensim.models import Word2Vec
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import umap
import seaborn as sns
import csv
from ot.sliced import sliced_wasserstein_distance


# Load tokenized data 
with open("tokensOld.pkl", "rb") as f:
    tokenized1 = pickle.load(f)

with open("tokensNew.pkl", "rb") as f:
    tokenized2 = pickle.load(f)
    
    
#input is the tokenized vector (either new or old spongebob)
# output is the reduced UMAP vector   
def umap_upload(tokenized):

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
    return reduced


def density_output(reduced_vectors):
    # this is how density is calculated 
    xy = np.vstack([reduced_vectors[:, 0], reduced_vectors[:, 1]])
    density = gaussian_kde(xy)(xy)

    # Plot UMAP. Early Seasons will be gold. Later seasons can be blue to fit spongebob's color palette (Possibly?)
    plt.figure(figsize=(10, 7))
    plt.scatter(reduced_vectors[:, 0], reduced_vectors[:, 1], alpha=0.6, c = density, label='2D Condensesed Data Points')
    plt.title("UMAP of SpongeBob Dialogue")
    plt.xlabel("UMAP-1")
    plt.ylabel("UMAP-2")
    plt.legend()
    plt.tight_layout()
    
def calc_wasserstein(old_script, new_script):
    
    sw_dist = sliced_wasserstein_distance(old_script, new_script,
                                         n_projections=100)
    return sw_dist

    

print(calc_wasserstein(umap_upload(tokenized1),umap_upload(tokenized2)))

density_output(umap_upload(tokenized1))
density_output(umap_upload(tokenized2))

plt.show()
