from selenium import webdriver
import json
import pandas as pd
import time

with open("song_titles.json") as f:
    song_titles = json.load(f)

song_titles = {k.strip(): v for k, v in song_titles.items()}

def find_lyrics(driver, song_path):
    url = "https://genius.com" + song_path
    driver.get(url)
    
    lyrics = driver.find_element_by_class_name("lyrics").text
    
    time.sleep(2)
    return lyrics


# DRIVER_PATH = "driver/chromedriver_mac"
# driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver = webdriver.Chrome()
df = pd.read_csv("df.csv")
artists = list(df['artist'])

index = 0
with open("start_index.txt", "r") as f:
    index = int(f.read())
    f.close()
    
artist_num = 0
for artist in song_titles:
    print(artist_num, artist)
    artist_num += 1
    if artist in artists:
        continue

    for title in song_titles[artist]:
        song_path = song_titles[artist][title]
        lyrics = find_lyrics(driver, song_path)
        
        df.loc[index] = [artist, title, song_path, lyrics]
        index += 1
        with open("start_index.txt", "w+") as f:
            f.write(str(index))
            f.close()

        df.to_csv("df.csv", index=False)