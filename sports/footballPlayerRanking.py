import time, os
import pandas as pd
from selenium import webdriver
# 홈 URL
year = str(input("시즌 입력 : "))
league = str(input("리그 입력(epl, 분데스리가, 세리에A, 리그1, 라리가) : "))
category = str(input("부문 입력(득점, 도움, 공격포인트 etc) : "))
leagueDic = {'epl' : 'epl', '분데스리가': 'bundesliga', '라리가': 'primera', '세리에A': 'seria', '리그1':'ligue1'}
categoryDic = {'득점':3, '도움':4, '공격포인트':5, '슈팅':6, '파울':7, '경고':8, '퇴장':9, '코너킥':10, '페널티킥':11, '오프사이트':12, '유효 슈팅':13, '유효슈팅':13, '경기수':14}

URL = 'https://sports.news.naver.com/wfootball/record/index.nhn?category=' + leagueDic[league] + '&tab=player&year=' + year


# 셀레니움으로 창 열기
driver = webdriver.Chrome()
driver.get(URL)


driver.find_element_by_css_selector('#wfootballPlayerRecordBody > table > thead > tr > th:nth-child(' + str(categoryDic[category]) +') > a').click()

ranks = driver.find_elements_by_css_selector('#wfootballPlayerRecordBody > table > tbody > tr > td.num > div')
players = driver.find_elements_by_css_selector('#wfootballPlayerRecordBody > table > tbody > tr > td.align_l > div > span.name')
teams = driver.find_elements_by_css_selector('#wfootballPlayerRecordBody > table > tbody > tr > td.align_l > div > span.team')
scores = driver.find_elements_by_css_selector('#wfootballPlayerRecordBody > table > tbody > tr > td.selected > div')


for i in range(1, 20):    
    rank = driver.find_element_by_css_selector('#wfootballPlayerRecordBody > table > tbody > tr:nth-child(' + str(i) + ') > td.num > div').text
    player = driver.find_element_by_css_selector('#wfootballPlayerRecordBody > table > tbody > tr:nth-child(' + str(i) + ') > td.align_l > div > span.name').text
    team = driver.find_element_by_css_selector('#wfootballPlayerRecordBody > table > tbody > tr:nth-child(' + str(i) + ') > td.align_l > div > span.team').text
    score = driver.find_element_by_css_selector('#wfootballPlayerRecordBody > table > tbody > tr:nth-child(' + str(i) + ') > td.selected > div').text
    print(rank, player, team, score)
rank = driver.find_element_by_css_selector('#wfootballPlayerRecordBody > table > tbody > tr.last > td.num > div').text
player = driver.find_element_by_css_selector('#wfootballPlayerRecordBody > table > tbody > tr.last > td.align_l > div > span.name').text
team = driver.find_element_by_css_selector('#wfootballPlayerRecordBody > table > tbody > tr.last > td.align_l > div > span.team').text
score = driver.find_element_by_css_selector('#wfootballPlayerRecordBody > table > tbody > tr.last > td.selected > div').text
print(rank, player, team, score)

driver.close()