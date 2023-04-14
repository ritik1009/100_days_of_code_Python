import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
data = response.text
soup = BeautifulSoup(data,"html.parser")
movies = []
movie_names = soup.find_all(name="h3", class_='title')
for movie in movie_names:
    movies.append(movie.text)

with open('movies.txt', 'w') as f:
    for line in movies:
        try:
            f.write(f"{line}\n")
        except:
            print(line)
            pass
# Write your code below this line 👇


