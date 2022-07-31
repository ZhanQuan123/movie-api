import threading
import requests
import html
from bs4 import BeautifulSoup
import json

x = requests.get('https://soap2day.cloud/movies/page/1/')

soup = BeautifulSoup(html.unescape(x.text), 'html.parser')
amount = int(soup.find(id="pagination").find_all('a')[4].text)


movie = {}

def run(count):


    x = requests.get(f'https://soap2day.cloud/movies/page/{count}/')
    soup = BeautifulSoup(html.unescape(x.text), 'html.parser')
    for name in soup.find_all('h2'):
        mov = name
        if mov is not None:
            test = {
                    'image' : mov.parent.parent.img['data-src']
                }
            movie[mov.parent.parent.img['alt']] = test
            json_data = json.dumps(movie)
            print(json.dumps(movie, indent=4, sort_keys=True))






for x in range(amount):
    start = threading.Thread(target=run, args=(x + 1,))
    start.start()
    start.join()


with open("movie.json", "w") as outfile:
    json.dump(movie, outfile, indent=4)