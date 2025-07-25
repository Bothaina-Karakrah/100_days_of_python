from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

all_movies = soup.find_all("h3", class_="title")
movie_titles = [movie.text for movie in all_movies]
movie_titles.reverse()
print(movie_titles)

with open("movies.text", mode='w') as file:
    for movie in movie_titles:
        file.write(f'{movie}\n')
