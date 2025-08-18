

import spotipy



from bs4 import BeautifulSoup
import requests

from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID="86a08f3dfe7041c18ea4d4aa23967dbd"
CLIENT_SECRET="bb6d67f18ee8470ab197dc6aa3ce879d"

ask_user=input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
header={
     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
 }
response=requests.get(f"https://www.billboard.com/charts/hot-100/{ask_user}",headers=header)
print("response code",response.status_code)
content=response.text
songs_list=[]
soup=BeautifulSoup(content,"lxml")
songs_name =soup.find_all(name="li",class_="o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-padding-l-050 lrv-u-padding-l-00@mobile-max u-max-width-397")
for name in songs_name:
    songs=name.select_one(selector="h3",class_="c-title  a-font-basic u-letter-spacing-0010 u-max-width-397 lrv-u-font-size-16 lrv-u-font-size-14@mobile-max u-line-height-22px u-word-spacing-0063 u-line-height-normal@mobile-max a-truncate-ellipsis-2line lrv-u-margin-b-025")
    songs_list.append(songs.getText().strip())


print(songs_list)

sp=spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private",
                                             redirect_uri="https://example.com/callback",
                                             client_id=CLIENT_ID,
                                             client_secret=CLIENT_SECRET,
                                             username="Rumi",
                                             show_dialog=True,
                                             cache_path="token.txt",

                                             ))
user_id=sp.current_user()["id"]

print(ask_user.split("-")[0])
uri_list=[f"spotipy:track:{songs} year:{ask_user.split("-")[0]}" for songs in songs_list]
print(uri_list)
uri_list=[]
for songs in songs_list:
    result=sp.search(q=f"track:{songs} year:{ask_user.split("-")[0]}",type="track")
    print(result)
    try:
        uri=result["tracks"]["items"][0]["uri"]
        uri_list.append(uri)
    except IndexError:
        print(f"{songs} doesn't found")
with open("token.txt") as token:
    tokens=token.read()[18:288]
    print(len(tokens))
    print(tokens)

body={
    "name":f"{ask_user} billboard 100",
    "public":False,
}
headers={
    "Authorization":f"Bearer {tokens} ",
    "Content-Type": "application/json"
}
# response=requests.get(url="https://api.spotify.com/v1/me",headers=headers)
# print(response.text)
sp.user_playlist_create(user="31hisri3j5x2bqhvkzprpjkvt4lm",name=f"{ask_user} billboard 100",public=False)
print("done")

sp.playlist_add_items(playlist_id="1QnJU5jOylbDVAPFT9mKL9",items=uri_list,position=None)
print("successful")