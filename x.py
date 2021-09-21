from lxml import html
import requests
from pymongo import MongoClient

db = MongoClient(host='localhost', port=27017)
db = db.data_gb_4

url = 'https://lenta.ru/parts/news/'
response = requests.get(url)
root = html.fromstring(response.text)

path = "//*[@id='more']/"

for i in range(1, 20):
    name = root.xpath(path+"div["+str(i)+"]/div[2]/h3/a/text()")
    time = root.xpath(path+"div["+str(i)+"]/div[1]/text()")
    news_link = root.xpath(path+"div["+str(i)+"]/div[2]/h3/a/@href")
    if name:
        db.news.insert_one(
            {"name": name[0],
             "href": news_link[0],
             "time": time[0]}
        )
