import pandas as pd 

df = pd.DataFrame(columns=["artist", "song_title", "song_path", "lyrics"])

df.to_csv("df.csv", index=False)