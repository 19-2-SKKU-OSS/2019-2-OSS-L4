import time, os
import pandas as pd
from selenium import webdriver

class TrendCrawler:
    def __init__(self):
        self.data = None

    def crawling(self):
        save_dir = "data"
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)

        URL = 'https://news.naver.com/'

        driver = webdriver.Chrome()
        driver2 = webdriver.Chrome()
        driver.get(URL)

        categories = driver.find_elements_by_css_selector(".category_ranking > a")

        data_list = []


        for category in categories:
            category.click()
            articles = driver.find_elements_by_css_selector("#right\.ranking_contents > ul > li > a")
            for article in articles:
                driver2.get(article.get_attribute("href"))
                title = driver2.find_element_by_css_selector("#articleTitle").text
                content = driver2.find_element_by_css_selector("#articleBodyContents").text                
                
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
