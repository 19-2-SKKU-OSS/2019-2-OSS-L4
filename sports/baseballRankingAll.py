from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/home/eelan/ChromeDriver/chromedriver')
driver.get("https://sports.news.naver.com/wbaseball/record/index.nhn")

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
print('\n동부지구 순위\n')
L = soup.select("#eastDivisionTeamRecordList_table")

for i in range(1, 6):
    htmlSelect = "#eastDivisionTeamRecordList_table > tr:nth-child(" + str(i) + ") > td.align_l > div > span"
    team = soup.select(htmlSelect)
    print(team[0].text)


print('\n중부지구 순위\n')
L = soup.select("#centerDivisionTeamRecordList_table")

for i in range(1, 6):
    htmlSelect = "#centerDivisionTeamRecordList_table > tr:nth-child(" + str(i) + ") > td.align_l > div > span"
    team = soup.select(htmlSelect)
    print(team[0].text)

print('\n서부지구 순위\n')
L = soup.select("#westDivisionTeamRecordList_table")

for i in range(1, 6):
    htmlSelect = "#westDivisionTeamRecordList_table > tr:nth-child(" + str(i) + ") > td.align_l > div > span"
    team = soup.select(htmlSelect)
    print(team[0].text)
    
print('\n와일드카드 순위\n')
L = soup.select("#wildCardTeamRecordList_table")

for i in range(1, 6):
    htmlSelect = "#wildCardTeamRecordList_table > tr:nth-child(" + str(i) + ") > td.align_l > div > span"
    team = soup.select(htmlSelect)
    print(team[0].text)
