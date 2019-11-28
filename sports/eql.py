import requests
from bs4 import BeautifulSoup 

res = requests.get("https://sports.news.naver.com/wfootball/record/index.nhn?category=epl")

soup = BeautifulSoup(res.content, 'html.parser')

print(soup)
