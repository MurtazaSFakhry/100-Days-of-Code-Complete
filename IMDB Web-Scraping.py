from dataclasses import field
from urllib import response
from bs4 import BeautifulSoup
import requests
import re
import csv
import lxml
import pandas as pd
import seaborn as sns

url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
print(response)

movies = soup.select('td.titleColumn')
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

list = []

# Iterating over movies to extract
# each movie's details
for index in range(0, len(movies)):
    # Separating  movie into: 'place',
    # 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index)) + 1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index)) - (len(movie))]

    data = {"movie_title": movie_title,
            "year": year,
            "place": place,
            "star_cast": crew[index],
            "rating": ratings[index],
            "vote": votes[index],
            "link": links[index]}
    list.append(data)

for movie in list:
    # print(movie['place'], '-', movie['movie_title'], '('+movie['year'] +
    #       ') -', 'Starring:', movie['star_cast'], movie['rating'])

    field_names = ['movie_title', "year", "place", "star_cast", "rating", "vote", "link"]
    with open('movies.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(list)

print("successful")

import matplotlib.pyplot as plt

top_10_ratings = [float(movie['rating']) for movie in list[:10]]
top_10_titles = [movie['movie_title'] for movie in list[:10]]

plt.figure(figsize=(10, 6))
plt.bar(top_10_titles, top_10_ratings)
plt.xticks(rotation=90)
plt.xlabel('Movie')
plt.ylabel('Rating')
plt.title('Top 10 Movie Ratings')
plt.tight_layout()
plt.show()
