#!/usr/bin/env python
# -*- coding: utf-8, euc-kr -*-

from time import sleep
from bs4 import BeautifulSoup
from multiprocessing import Process
from korea_news_crawler.exceptions import *
from korea_news_crawler.articleparser import ArticleParser
from korea_news_crawler.writer import Writer
import os
from urllib.request import urlopen
import platform
import calendar
import requests
import re


class CompanyList(object):
    def __init__(self):
        pass

    @staticmethod
    def get_url_data(url, max_tries=10):
        remaining_tries = int(max_tries)
        while remaining_tries > 0:
            try:
                return requests.get(url)
            except requests.exceptions:
                sleep(60)
            remaining_tries = remaining_tries - 1
        raise ResponseTimeout()

    def crawling(self, site):
        URL = ""
        ul_class = ""
        # 네이버 언론사 크롤링 
        if site == "네이버":
            URL = "https://news.naver.com/main/officeList.nhn"
            ul_class = "group_list"
        # 다음 언론사 크롤링
        elif site == "다음":
            URL = "https://media.daum.net/cp/"
            ul_class = "list_cp"
        url = urlopen(URL)
        document = BeautifulSoup(url, 'html.parser')
        
        # 모든 언론사 이름 추출
        for link in document.find_all("ul", {"class": ul_class}):
            for li in link.find_all("li"):
                print(li.find("a").get_text())


if __name__ == "__main__":
    Crawler = CompanyList()
    Crawler.crawling("다음");
