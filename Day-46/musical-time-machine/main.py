import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Custom function to create a playlist since the default one was acting up
def create_playlist_me(sp_client, name, public=False, description=""):
  return sp_client._post(
      "me/playlists",
      payload={"name": name, "public": public, "description": description},
  )

load_dotenv()

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = date.split("-")[0]

url = f"https://appbrewery.github.io/bakeboard-hot-100/{date}/"
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36'
}

# Scrape the top 100 songs
response = requests.get(url=url, headers=header)
response.raise_for_status()
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
top_entries = soup.find_all("div", class_="chart-entry__info")
top_tracks = []
for entry in top_entries:
    song = entry.find("h3", class_="chart-entry__title").getText()
    artist = entry.find("span", class_="chart-entry__artist").getText()
    top_tracks.append((song, artist))

print(top_tracks)

# Login to Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.environ["SPOTIFY_CLIENT_ID"],
    client_secret=os.environ["SPOTIFY_CLIENT_SECRET"],
    redirect_uri=os.environ["REDIRECT_URI"],
    scope="playlist-modify-private playlist-modify-public",
    show_dialog=True,
    cache_path="token.txt"
))

user_id = sp.current_user()["id"]
print(f"Logged in as Spotify User ID: {user_id}")

song_uris = []

# Search Spotify for each song
for song, artist in top_tracks:
    # Take the primary lead artist (removes "Featuring...", "Feat.", "With", etc.)
    primary_artist = (
        artist.split(" Featuring ")[0].split(" feat. ")[0].split(" with ")[0].split(" & ")[0]
    )

    query = f"{song} {primary_artist}"
    result = sp.search(q=query, type='track', limit=1)

    try:
        song_uris.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        # Fallback search if the exact artist match fails
        fallback_query = f"track:{song} year:{year}"
        fallback_result = sp.search(q=fallback_query, type='track', limit=1)
        try:
            song_uris.append(fallback_result["tracks"]["items"][0]["uri"])
        except IndexError:
            print(f"'{song}' doesn't exist on Spotify. Skipped.")

# Make a new playlist
playlist = create_playlist_me(
    sp_client=sp,
    name=f"{date} Billboard 100",
    public=False,
    description=f"Top 100 Billboard tracks from {date}",
)

playlist_id = playlist["id"]
print(f"Created playlist: {playlist['name']} (ID: {playlist_id})")

# Add the tracks to the playlist in batches
if song_uris:
    for i in range(0, len(song_uris), 100):
        batch = song_uris[i:i + 100]
        sp.playlist_add_items(playlist_id=playlist_id, items=batch)

    print(f"Successfully added {len(song_uris)} tracks to '{playlist['name']}'!")
else:
    print("No tracks were found to add.")