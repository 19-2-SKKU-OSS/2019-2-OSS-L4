from selenium import webdriver
from bs4 import BeautifulSoup

year = str(input("시즌 입력 : "))
league = str(input("리그 입력 : "))
category = {'동부지구': '#eastDivisionTeamRecordList_table', '중부지구': '#centerDivisionTeamRecordList_table', '서부지구': '#westDivisionTeamRecordList_table', '와일드카드': '#wildCardTeamRecordList_table'}

crawlerURL = "https://sports.news.naver.com/wbaseball/record/index.nhn?category=mlb&year=" + year + "&league=NL"

driver = webdriver.Chrome('/home/eelan/ChromeDriver/chromedriver')
driver.get(crawlerURL)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

P = soup.select("#_currentYearButton > em")

print(P[0].text)
## #eastDivisionTeamRecordList_table > tr:nth-child(1) > td.align_l > div > span
for i in range(1, 6):
    htmlSelect = category.get(league) + " > tr:nth-child(" + str(i) + ") > td.align_l > div > span"
    team = soup.select(htmlSelect)
    print('%d '%i,team[0].text)
