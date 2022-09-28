from urllib.parse import urljoin
import lxml as lxml
import pandas as pd
from pandas import DataFrame
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from urllib.request import urlopen
from selenium.webdriver.support.ui import Select
from pyparsing import results

url = "https://libraries.io/search?order=desc&page=1&platforms=Maven&sort=rank"
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")

site_title = soup.title.string
print(f"\nFrom {site_title}\n")

projects = soup.findAll(class_="project")

while True:
    for link in soup.select('div.project a[href]'):
        links = (link['href'])
        for project in projects:
            soup = [a.getText() for a in BeautifulSoup(requests.get(url).text, "lxml").select("div.project > h5 > a")]
            name = ("\n".join(soup))
        data = {'link': [links], 'names': [name]}
        df = pd.DataFrame(data)
        print(df)
    next_page = soup.select(class_="next")
    if next_page:
        next_url = next_page.get('href')
        url = urljoin(url, next_url)
    else:
        break
