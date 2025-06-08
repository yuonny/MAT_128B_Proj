import pickle

with open("tokensOld.pkl", "rb") as f:
    tokenized1 = pickle.load(f)

with open("tokensNew.pkl", "rb") as f:
    tokenized2 = pickle.load(f)
    
    
tokenized = tokenized1 + tokenized2
print(len(tokenized))