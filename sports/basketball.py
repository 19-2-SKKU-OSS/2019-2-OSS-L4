from selenium import webdriver
from bs4 import BeautifulSoup

year = str(input("시즌 입력 : "))
league = str(input("리그 입력 : "))
category = { '동부': 'EAST', '서부': 'WEST'}

crawlerURL = "https://sports.news.naver.com/basketball/record/index.nhn?category=nba&year=" + year + "&conference=" + category.get(league)  
driver = webdriver.Chrome('/Users/softhoon/Desktop/chromedriver')
driver.get(crawlerURL)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

L = soup.select("#wfootballTeamRecordBody > table > tbody")
P = soup.select("#_currentYearButton > em")

print(P[0].text)
#team_MIL
#team_MIL
for i in range(1, 16):
    htmlSelect = "#regularTeamRecordList_table > tr:nth-child(" + str(i) + ") > td.tm > div > span"
    team = soup.select(htmlSelect)
    print('%d '%i,team[0].text)
