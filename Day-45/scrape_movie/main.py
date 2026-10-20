import requests
import requests_cache
from bs4 import BeautifulSoup

# Cache the page so testing doesn't keep hitting the archive
requests_cache.install_cache(cache_name="movies", expire_after=3600)

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
response.raise_for_status()
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

# Get all movie title tags
movie_tags = soup.find_all(name="h3", class_="title")

# Extract the text and reverse the list so it goes from 1 to 100
movies = [movie.getText() for movie in movie_tags]
movies.reverse()

# Save to a text file
with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")

print("Saved top 100 movies to movies.txt")