import train_and_save_umap
import numpy as np
from ot.sliced import sliced_wasserstein_distance
import matplotlib.pyplot as plt

def calc_wasserstein(old_script, new_script):
    sw_dist = sliced_wasserstein_distance(old_script, new_script,
                                         n_projections=100)
    return sw_dist


def calc_plot_change_over_time():
    old_tokens, old_model = train_and_save_umap.train_word2vec("old_seasons_tokens.pkl")
    # save newer seasons UMAP output
    new_tokens, new_model = train_and_save_umap.train_word2vec("new_seasons_tokens.pkl")


    x = np.arange(1, 31)
    dist_array = []
    for i in x:
        old_umap = train_and_save_umap.umap_upload(old_tokens, old_model, "umap_old.npy")
        new_umap = train_and_save_umap.umap_upload(new_tokens, new_model, "umap_new.npy")
            
        older_seasons_umap = np.load("umap_old.npy")
        newer_seasons_umap = np.load("umap_new.npy")
        dist_array.append(calc_wasserstein(older_seasons_umap, newer_seasons_umap))

    plt.title("Wasserstein Distance Calculation Over Iterations")
    plt.xlabel("Num Iteration") 
    plt.ylabel("Wasserstein Distance")
    plt.plot(x, dist_array, color ="blue") 


def calc_umap_diff(token_file, np_file, output_file_name, col , which_season):
    tokens, model = train_and_save_umap.train_word2vec(token_file)
    # save newer seasons UMAP output
    x = np.arange(1, 31)
    dist_array = []
    older_seasons_umap = np.load(np_file)
    for i in x:
        train_and_save_umap.umap_upload(tokens, model, output_file_name)       
        newer_seasons_umap = np.load(output_file_name)
        dist_array.append(calc_wasserstein(older_seasons_umap, newer_seasons_umap))
    
    plt.plot(x, dist_array, color = col, label=which_season) 

# calc_umap_diff("old_seasons_tokens.pkl", "umap_old.npy", "umap_old_new.npy", "blue", "Older Seasons")
# calc_umap_diff("new_seasons_tokens.pkl", "umap_new.npy", "umap_new_new.npy", "gold", "Newer Seasons")

# plt.title("Stability of UMAP projections under repeated runs")
# plt.xlabel("Run Iteration") 
# plt.ylabel("Wasserstein Distance")
# plt.legend()

calc_plot_change_over_time()


plt.show()