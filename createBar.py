# import trainAndSaveUMAP
import numpy as np
from ot.sliced import sliced_wasserstein_distance
import matplotlib.pyplot as plt

def calc_wasserstein(old_script, new_script):
    sw_dist = sliced_wasserstein_distance(old_script, new_script,
                                         n_projections=100)
    return sw_dist

# old_tokens, old_model = trainAndSaveUMAP.train_word2vec("tokensOld.pkl")
# # save newer seasons UMAP output
# new_tokens, new_model = trainAndSaveUMAP.train_word2vec("tokensNew.pkl")



x = np.arange(1, 31)
dist_array = [4.5005460976909, 4.38074088751021, 4.756634262374873, 4.879584333228202, 4.542216174280199, 5.020978301883416, 4.531689846305764, 4.696584729039377, 4.671533048006248, 4.676448512198163, 4.816565251431661, 4.792064787597063, 4.8749170668889406, 4.777681240214229, 4.414049974813187, 4.859511923249291, 4.852048828727659, 4.926681277071333, 4.68639870187505, 4.708680492150278, 4.973525891589486, 4.433567703855261, 4.814273545229755, 4.841265173158863, 4.894217204457215, 4.771143020137498, 4.6130304970009774, 4.6405628011985565, 4.76394982929893, 4.55282873866392]
# for i in x:
#     old_umap = trainAndSaveUMAP.umap_upload(old_tokens, old_model, "umap_old.npy")
#     new_umap = trainAndSaveUMAP.umap_upload(new_tokens, new_model, "umap_new.npy")


#     older_seasons_umap = np.load("umap_old.npy")
#     newer_seasons_umap = np.load("umap_new.npy")
#     dist_array.append(calc_wasserstein(older_seasons_umap, newer_seasons_umap))

plt.title("Wasserstein Distance Calculation Over Iterations")
plt.xlabel("Num Iteration") 
plt.ylabel("Wasserstein Distance")
plt.plot(x, dist_array, color ="blue") 
plt.show()
