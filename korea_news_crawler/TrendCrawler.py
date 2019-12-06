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
            # 기사에서 제목과 내용, 상위댓글 5개 가져오기
            for article in articles:
                driver2.get(article.get_attribute("href"))
                title = driver2.find_element_by_css_selector("#articleTitle").text
                content = driver2.find_element_by_css_selector("#articleBodyContents").text                
                comments_elements = driver2.find_elements_by_css_selector(".u_cbox_list > li")
                comments = []
                for i, comment in enumerate(comments_elements):
                    if i == 5:
                        break
                    comments.append(comment.text)
                #spiLayer > div._reactionModule.u_likeit > ul > li.u_likeit_list.good > a > span.u_likeit_list_count._count
                like = driver2.find_element_by_css_selector("#spiLayer > div._reactionModule.u_likeit > ul > li.u_likeit_list.good > a > span.u_likeit_list_count._count").text
                hate = driver2.find_element_by_css_selector("#spiLayer > div._reactionModule.u_likeit > ul > li.u_likeit_list.angry > a > span.u_likeit_list_count._count").text
                reactions=[]
                reactions.append(like)
                reactions.append(hate)
                
                data = {}
                data['category'] = category.text
                data['title'] = title
                data['contents'] = content
                data['comments'] = comments
                data['reactions'] = reactions
                data_list.append(data)

        self.data = data_list

    def save_csv(self, save_path):
        df = pd.DataFrame(self.data)
        pd.DataFrame.to_csv(df, save_path)



if __name__ == "__main__":
    crawler = TrendCrawler()
    crawler.crawling()
    crawler.save_csv("data.csv")
