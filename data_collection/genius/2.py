from selenium import webdriver
import json
import pandas as pd

with open("song_titles.json") as f:
    song_titles = json.load(f)

song_titles = {k.strip(): v for k, v in song_titles.items()}

def find_lyrics(driver, song_path):
    url = "https://genius.com" + song_path
    driver.get(url)
    
    lyrics = driver.find_element_by_class_name("lyrics").text
    
    return lyrics


driver = webdriver.Chrome()
df = pd.DataFrame(columns=["artist", "song_title", "song_path", "lyrics"])

index = 0
with open("start_index.txt", "r") as f:
    index = int(f.read())
    f.close()
    
artist_num = 0
for artist in song_titles:
    print(artist_num, artist)
    for title in song_titles[artist]:
        song_path = song_titles[artist][title]
        lyrics = find_lyrics(driver, song_path)
        
        df.loc[index] = [artist, title, song_path, lyrics]
        index += 1
        with open("start_index.txt", "w+") as f:
            f.write(str(index))
            f.locs()
    
    artist_num += 1
    break