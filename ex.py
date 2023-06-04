import requests
from bs4 import BeautifulSoup as bs4
import pandas as pd
import time
page_count = 5
name = ''



data = {}

for i in range(0,page_count+1):
    
    url = f'https://ge.movie/filter-movies?type=search&search={name}&page={i}'
    
    res = requests.get(url)
    res = bs4(res.text, "html.parser")

    movies = res.select('.popular-card')
    for movie in movies:
        title = movie.find("h2").text
        link = movie.find("a").get("href")
        img = movie.find("img").get("data-src")
        year = movie.find(class_="year").text
        imdb = "ranking: "+movie.find(class_="imdb").find("span").text
        
        title = "".join( title.split())
        data[title] = {
            "imdb":imdb,
            "year":year,
            "url":link,
            "img":img
        }
    
    # time.sleep(15)
    
    

df = pd.DataFrame(data).T
df.to_excel("result.xlsx",sheet_name="movies")
df.to_csv("result.csv")


print("data gathered!")