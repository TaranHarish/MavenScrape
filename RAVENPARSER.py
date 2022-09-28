from urllib.parse import urljoin
import time
import bs4
import lxml as lxml
import pandas as pd
from pandas import DataFrame
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from urllib.request import urlopen
from pyparsing import results

url = "https://libraries.io/search?order=desc&page=1&platforms=Maven&sort=rank"
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")

site_title = soup.title.string
print(f"\nFrom {site_title}\n")

projects = soup.findAll(class_="project")


while True:
    for page in range(1, 300):
        url = f'https://libraries.io/search?order=desc&page={page}&platforms=Maven&sort=rank'
        for project in projects:
            for link in soup.select('div.project a[href]'):
                links = (link['href'])
                print(links)
        soup = [a.getText() for a in BeautifulSoup(requests.get(url).text, "lxml").select("div.project > h5 > a")]
        name = ("\n".join(soup))
        print(name)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

data = {'link': [links], 'names': [name]}
df = pd.DataFrame(data)
print(df)
