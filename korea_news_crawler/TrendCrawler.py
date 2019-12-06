import time, os
import pandas as pd
from selenium import webdriver

class TrendCrawler:
    def __init__(self):
        self.data = None

    def crawling(self):
        # 데이터 저장 디렉토리 생성
        save_dir = "data"
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)

        # 홈 URL
        URL = 'https://news.naver.com/'

        # 셀레니움으로 창 열기
        #driver는 url을 복사할 창, driver2는 복사된 링크로 들어가서 기사 내용 가져올 창
        driver = webdriver.Chrome()
        driver2 = webdriver.Chrome()
        driver.get(URL)
        #정치, 경제, IT 등
        categories = driver.find_elements_by_css_selector(".category_ranking > a")

        data_list = []

        
        for category in categories:
            category.click()
            articles = driver.find_elements_by_css_selector("#right\.ranking_contents > ul > li > a")
            # 기사에서 제목과 내용 가져오기
            for article in articles:
                driver2.get(article.get_attribute("href"))
                title = driver2.find_element_by_css_selector("#articleTitle").text
                content = driver2.find_element_by_css_selector("#articleBodyContents").text                
                # 데이터 딕셔너리 생성 후 data_list에 append
                data = {}
                data['category'] = category.text
                data['title'] = title
                data['contents'] = content
                data_list.append(data)

        self.data = data_list

    def save_csv(self, save_path):
        df = pd.DataFrame(self.data)
        pd.DataFrame.to_csv(df, save_path)



if __name__ == "__main__":
    crawler = TrendCrawler()
    crawler.crawling()
    crawler.save_csv("data.csv")
