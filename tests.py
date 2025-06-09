import pickle

with open("tokensOld.pkl", "rb") as f1:
    tokenized1 = pickle.load(f1)

with open("tokensNew.pkl", "rb") as f2:
    tokenized2 = pickle.load(f2)
    
    
tokenized = tokenized1 + tokenized2
print(len(tokenized2))