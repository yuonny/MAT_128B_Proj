import pickle
import numpy as np
import umap
from gensim.models import Word2Vec

def train_word2vec(token_file):
    with open(token_file, "rb") as f:
        tokenized = pickle.load(f)

    model = Word2Vec(sentences=tokenized, vector_size=100, window=5, min_count=1, workers=1, seed=42)
    return tokenized, model

# input is the tokenized vector (either new or old spongebob)
# output is the reduced UMAP vector
def umap_upload(tokens, model, file_name):
    # Turn a sentence into a single vector by averaging its word embeddings
    def sentence_vector(sentence):
        # Get the word2vec vector for each word in the sentence
        vectors = [model.wv[word] for word in sentence if word in model.wv]

        # Return the average of all word vectors which represents the full sentence
        return np.mean(vectors, axis=0) if vectors else np.zeros(model.vector_size)

    # Turn all tokenized sentences into sentence vectors using word2vec
    embedded = np.array([sentence_vector(s) for s in tokens])

    # Reduce 100-dimensional sentence vectors down to 2D using UMAP for visualization
    """
    n_components - number of dimensions to reduce our data to
    random_state - fixed random seed for reproducibility
    fit_transform - this function turns out data to a UMAP
    """
    reduced = umap.UMAP(n_components=2, random_state = 42).fit_transform(embedded)

    # save UMAP output as a numpy file
    np.save(file_name, reduced)
    return reduced

# save older seasons UMAP output
old_tokens, old_model = train_word2vec("old_seasons_tokens.pkl")
old_umap = umap_upload(old_tokens, old_model, "umap_old.npy")

# save newer seasons UMAP output
new_tokens, new_model = train_word2vec("new_seasons_tokens.pkl")
new_umap = umap_upload(new_tokens, new_model, "umap_new.npy")
