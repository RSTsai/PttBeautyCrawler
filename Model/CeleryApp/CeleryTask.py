# 外部引用
import time
import logging
# 內部引用
from CeleryMain import app
from Model.Crawler.PttBeautyCrawlerModel import CrawlerAction


@app.task
def add(x, y):
    time.sleep(2)
    print(x + y)
    return x + y


@app.task
def PttCrawler(x, *args):
    CrawlerAction(x)
    return True
