import gdown

url = "https://drive.google.com/uc?id=1_r2rvMzaa7Ugf2c-_gAP6BRV9JctMSdV"
output = "steam_reviews_eng_new.csv"
gdown.download(url, output, quiet=False)

url = "https://drive.google.com/uc?id=1ZsBrSz7ap5Hy_8DKLGLOYeDJDd4ANkeo"
output = "steam_games.csv"
gdown.download(url, output, quiet=False)