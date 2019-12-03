from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/Users/softhoon/Desktop/chromedriver')
driver.get("https://sports.news.naver.com/wfootball/record/index.nhn?category=epl")

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

L = soup.select("#wfootballTeamRecordBody > table > tbody")

for element in L:
    print(element.text)
