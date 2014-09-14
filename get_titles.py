__author__ = 'klabeau'

import requests
from bs4 import BeautifulSoup

r = requests.get("http://thetvdb.com/?tab=season&seriesid=71663&seasonid=2739&lid=7")
text = r.text
soup = BeautifulSoup(text)

print (soup.odd)