import kagglehub

# Download latest version
path = kagglehub.dataset_download("mikhailgaerlan/spongebob-squarepants-completed-transcripts")

print("Path to dataset files:", path)