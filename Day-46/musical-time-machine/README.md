# Day 46: Musical Time Machine

You type in a date, and the program scrapes the Billboard Hot 100 songs from that week and automatically creates a playlist for you on your Spotify account.

It uses BeautifulSoup to scrape the song and artist names, and the `spotipy` library to search for the tracks and build the playlist. The first time you run it, a browser window opens so you can log into Spotify and give the app permission. It saves a `token.txt` file so you don't have to log in every time. `token.txt` is in `.gitignore` so it stays private.

## Setup

You need to go to the Spotify Developer Dashboard, create an app, and get your keys. Set the Redirect URI in your Spotify app settings to `http://example.com`.

Create a file called `.env` in this folder:

```text
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
REDIRECT_URI=[http://example.com](http://example.com)
```
To run it: `python main.py`