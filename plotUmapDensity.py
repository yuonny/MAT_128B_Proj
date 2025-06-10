import pickle
import numpy as np
from numpy.linalg import norm
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import csv
import seaborn as sns
from ot.sliced import sliced_wasserstein_distance

# load UMAP data
older_seasons_umap = np.load("umap_old.npy")
newer_seasons_umap = np.load("umap_new.npy")

def calc_density(reduced_vectors):
    xy = np.vstack([reduced_vectors[:, 0], reduced_vectors[:, 1]])
    density = gaussian_kde(xy)(xy)
    return density

#finding which point has the highest density 
def calc_max_density(density, reduced_vectors, token_file):
    max_idx = np.argmax(density)
    mode_point = reduced_vectors[max_idx]
    
    distances = norm(reduced_vectors - mode_point, axis=1)
    index = np.argmin(distances)
    
    with open(token_file, "rb") as f:
        tokenized = pickle.load(f)
    return tokenized[index]


def density_output(reduced_vectors, window_title):
    # this is how density is calculated 
    
    density = calc_density(reduced_vectors)

    fig = plt.figure(figsize=(10, 7))
    fig.canvas.manager.set_window_title(window_title)
    plt.scatter(reduced_vectors[:, 0], reduced_vectors[:, 1], alpha=0.6, c = density, label='2D Condensed Data Points')
    plt.title("UMAP of SpongeBob Dialogue")
    plt.xlabel("UMAP-1")
    plt.ylabel("UMAP-2")
    plt.legend()
    plt.tight_layout()

def plot_output(reduced_vectors):
    # Plot UMAP. Early Seasons will be gold. Later seasons can be blue to fit spongebob's color palette (Possibly?)
    plt.figure(figsize=(10, 7))
    plt.scatter(reduced_vectors[:, 0], reduced_vectors[:, 1], alpha=0.6, c = 'gold', label='2D Condensesed Data Points')
    plt.title("UMAP of SpongeBob Dialogue")
    plt.xlabel("UMAP-1")
    plt.ylabel("UMAP-2")
    plt.legend()
    plt.tight_layout()
    
def calc_wasserstein(old_script, new_script):
    sw_dist = sliced_wasserstein_distance(old_script, new_script,
                                         n_projections=100)
    return sw_dist

print(calc_wasserstein(older_seasons_umap, newer_seasons_umap))

print(calc_max_density(calc_density(older_seasons_umap), older_seasons_umap,"tokensOld.pkl"))
print(calc_max_density(calc_density(newer_seasons_umap),  newer_seasons_umap, "tokensNew.pkl"))

# plot_output(older_seasons_umap)
# plot_output(newer_seasons_umap)
# density_output(older_seasons_umap, "Older Seasons Transcript UMAP")
# density_output(newer_seasons_umap, "Newer Seasons Transcript UMAP")

plt.show()
