import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from articlecrawler import *

form_class = uic.loadUiType("mainview.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class, ArticleCrawler) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.click_button)
            
            
            
    def click_button(self):
        category_split = self.categoryline.text().split()
        starting_date_split = self.starting_date.text().split()
        closing_date_split = self.closing_date.text().split()
        if (self.num_article_line.text() == "default"):
            num_article = -1
        else:
            num_article = int(self.num_article_line.text())
            
        Crawler = ArticleCrawler()
        Crawler.set_category(category_split[0])
        Crawler.set_date_range(int(starting_date_split[0]), int(starting_date_split[1]), int(closing_date_split[0]), int(closing_date_split[1]))
        Crawler.set_count(num_article)
        Crawler.start()

        
        
        

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
