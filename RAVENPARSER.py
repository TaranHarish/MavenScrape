import pandas as pd
from pandas import DataFrame
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from urllib.request import urlopen
from pyparsing import results

# The function of this code is to scrape through the Maven package listings on Library.io. It must return data in the
# form of a table with 3 columns and ~492,000 rows. Each row is a package of Maven, and the columns are split into
# number, name, and link back to the package's webpage.

url = "https://libraries.io/search?order=desc&platforms=Maven&sort=rank"
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")

response = requests.get(url)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")
site_title = soup.title.string
print(f"\nFrom {site_title}\n")

for i in web_page:
    results = soup.findAll(class_="project")
    button = webdriver.find_element_by_class_name("project")
    button.click()

# name variable that identifies the name
# link variable that contains link to the webpage
# number of rows
table = pd.DataFrame(#columns=name,link.number)
print(table)
