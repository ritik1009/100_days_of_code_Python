import spotipy
import pprint
from spotipy.oauth2 import SpotifyClientCredentials
client_id = ""
client_secret = ""
redirect_uri = 'https://example.com'
scope = "playlist-modify-private" 
oaut = spotipy.oauth2.SpotifyOAuth(client_id=client_id,client_secret=client_secret,scope=scope,redirect_uri=redirect_uri)
sp = spotipy.client.Spotify(oauth_manager=oaut)
user_details = sp.current_user()
user_id = user_details['id']
print(user_details)
tracks_uri = []
#artist = 'sisqo'
#track_result = sp.search(q=q,type=type)
def spotify_song_list(name=[],date=''):
    for i in name:
        name = i
        year = date.split('-')[0]
        q = f'track: {name} year: {year}'
        type = 'track'
        track_result = sp.search(q=q, type=type)
        try:
            tracks_uri.append(track_result["tracks"]["items"][0]["uri"])
        except:
            pass
    return tracks_uri

def create_a_playlist(name):
    playlist = sp.user_playlist_create(user=user_id,name=name,public='False')
    return playlist['uri']

def add_tracks_playlist(playlist_id= '',tracks = ''):
    playlist_data = sp.user_playlist_add_tracks(user=user_id,playlist_id=playlist_id,tracks=tracks)
    return playlist_data
#print(sp.current_user())