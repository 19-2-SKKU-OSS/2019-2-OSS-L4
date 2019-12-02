from selenium import webdriver
from bs4 import BeautifulSoup

year = str(input("시즌 입력 : "))
league = str(input("리그 입력 : "))
category = {'프리미어리그': 'epl', '라리가': 'primera', '분데스리가': 'bundesliga', '세리에A': 'seria', '리그1': 'ligue1', '에레디비시': 'eredivisie'}

team_counts = {'프리미어리그': 20, '라리가': 20, '분데스리가': 18, '세리에A': 20, '리그1': 20, '에레디비시': 18}

crawlerURL = "https://sports.news.naver.com/wfootball/record/index.nhn?category=" + category.get(league) + "&year=" + year + "&tab=team"

driver = webdriver.Chrome('/Users/softhoon/Desktop/chromedriver')
driver.get(crawlerURL)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

L = soup.select("#wfootballTeamRecordBody > table > tbody")
P = soup.select("#_currentYearButton > em")

print(P[0].text)

for i in range(1, team_counts.get(league) + 1):
    htmlSelect = "#wfootballTeamRecordBody > table > tbody > tr:nth-child(" + str(i) + ") > td.align_l > div > span"
    team = soup.select(htmlSelect)
    print('%d '%i,team[0].text)
