# This exercise is not completed yet this about new library 'BeautifulSoup and requests' so learn it later and,
# complete this program.
"""
Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times
homepage.
"""

import requests
from bs4 import BeautifulSoup

# url = 'https://github.com/'
url = 'https://www.nytimes.com/'
# url = 'https://www.yellowpages.in/hyderabad/food-and-beverages/606286653'

r = requests.get(url)
r_html = r.text
# print(r_html)


soup = BeautifulSoup(r_html, "html.parser")
# f = soup.find_all('title')
# title = soup.find_all('a')  #.string
for n in soup.find_all('a'):
    print(n.text, n.get("href"))
    # n.get("href")

soup.prettify()



