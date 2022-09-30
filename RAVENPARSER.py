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
links = []
names = []

for page in range(1, 300):
    time.sleep(1)
    url = f'https://libraries.io/search?order=desc&page={page}&platforms=Maven&sort=rank'
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    print(url)
    for link in soup.select('div.project a[href]'):
        links.append(link['href'])
        name = link.getText()
        names.append(name)

data = {'link': links, 'names': names}
df = pd.DataFrame(data)
df.to_csv("Maven.csv")
