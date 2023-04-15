import requests
from bs4 import BeautifulSoup
from spotify_ import spotify_song_list,create_a_playlist, add_tracks_playlist


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url)
data = response.text

soup = BeautifulSoup(data,"html.parser")
#print(soup.title)
song_list = []
song_name = soup.select("li .o-chart-results-list__item h3")
#print(song_name)
for song in song_name:
    #print(song.text)
    song_list.append(song.text.replace("\t",'').replace("\n",""))
#print("\n Song List -",song_list)

spotify_song_list = spotify_song_list(name = song_list,date=date)
playlist_name = f"{date} Billboard 100"
playlist_id = create_a_playlist(name=playlist_name)
print(playlist_id)

print(add_tracks_playlist(playlist_id=playlist_id,tracks=spotify_song_list))


