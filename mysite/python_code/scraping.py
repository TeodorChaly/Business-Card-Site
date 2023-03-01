import requests
from bs4 import BeautifulSoup

def run_scraping(string):
    #
    # url = "https://www.google.com/search?q="
    # if string.count(" ") >=1:
    #     print(" ! ")
    #     return "!"
    # print(string)
    # page = requests.get(url)
    #
    # soup = BeautifulSoup(page.content, "html.parser")
    # news_headlines = soup.find_all("h2", class_="news__headline")
    #
    # for headline in news_headlines:
    #     print(headline.get_text())
    return string*4