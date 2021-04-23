# Program scraps web pages

import requests
from bs4 import BeautifulSoup as bs

# url = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/"
# ele = 'h1'

# get all links on page
# for link in soup.find_all('a'):
#     print(link.get("href"))


def webScraper(url, ele):
    page = requests.get(url)

    soup = bs(page.content, 'html.parser')

    results = soup.find_all(ele)

    # get all main headings
    for headline in results:
        print(headline.text)

# webScraper(url, ele)