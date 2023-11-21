
import time
import pandas as pd
import numpy as np

import requests
from bs4 import BeautifulSoup
from lxml import etree

def get_g20_news():
    url = 'https://timesofindia.indiatimes.com/topic/G20'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        dom=etree.HTML(str(soup))
        articles = soup.find_all('li', class_='article')

        g20_news = []
        
        title=''
        date=''
        link=''

        # for article in articles:
        #     title = article.find('span', class_='title').text.strip()
        #     date = article.find('span', class_='meta').text.strip()
        #     link = article.find('a')['href']

        news_item = {
            'title': title,
            'date': date,
            'link': link
        }

        g20_news.append(news_item)

        return g20_news

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    g20_news = get_g20_news()

    if g20_news:
        for i, news_item in enumerate(g20_news, 1):
            print(f"News {i}:")
            print(f"Title: {news_item['title']}")
            print(f"Date: {news_item['date']}")
            print(f"Link: {news_item['link']}")
            print("\n")
    else:
        print("No G20 news found.")
        
        
        
# from newspaper import Article

# url='https://www.hindustantimes.com/opinion/terms-of-trade-let-s-discuss-india-s-growth-forecast-101697111227702.html'

# art=Article(url)
# print(art.text)
