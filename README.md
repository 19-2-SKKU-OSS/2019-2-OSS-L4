# 2019-2-OSS-L4

## 0. Our Homepage 
* Link : https://19-2-skku-oss.github.io/2019-2-OSS-L4/
## 1. Our Team
* **신승훈 (소프트웨어학과, 2학년, softho0n)**

|title|contents|
|---|-----------------------------------|
|Language|C, C++, Java, Swift, Python|
|Role|Team Leader|

* **문성재 (소프트웨어학과, 2학년, LimeMun)**


|title|contents|
|---|-----------------------------------|
|Language|C, Java, Swift, Python|
|Role|Team Member|
* **김승태 (공학계열, 3학년, kim-seungtae)**

|title|contents|
|---|-----------------------------------|
|Language|C, C++, Python|
|Role|Team Member|
* **김예서 (유학동양학과, 4학년, yeeseo)**

|title|contents|
|---|-----------------------------------|
|Language|C, C++, Python, Java|
|Role|Team Member|
* **송일한 (신소재공학과, 3학년, xmilexx)**

|title|contents|
|---|-----------------------------------|
|Language|C, C++, Java, Swift, Python|
|Role|Team Leader|

## 2. Original Project
* Korean News Crawler (https://github.com/lumyjuwon/KoreaNewsCrawler)  
: 대량의 뉴스 데이터를 수집하기 위해 만들어진 뉴스 크롤러입니다.

## 3. Quick Start & Example

### User Python Installation
  * **KoreaNewsCrawler**

    ``` pip install KoreaNewsCrawler ```
    
### Method

* **set_category(category_name)**
 
 This method is setting categories that you want to crawl.  
 Categories that can be entered into parameters are politics, economy, society, living_culture, IT_science. 
 Multiple parameters can be entered.
  
* **set_date_range(startyear, startmonth, endyear, endmonth)**
  
 This method represents the duration of the news you want to collect.  
 Data is collected from startmonth to endmonth.
  
* **start()**
 
 This method is the crawl execution method.
  
### Example
```
from korea_news_crawler.articlecrawler import ArticleCrawler

Crawler = ArticleCrawler()  
Crawler.set_category("politics", "IT_science", "economy")  
Crawler.set_date_range(2017, 1, 2018, 4)  
Crawler.start()
```
 From January 2017 to April 2018, Parallel crawls will be conducted using multiprocessors for political, IT science, world, and economic category news.
   
## 4. How to Contribute
  
  * 언론사를 선택해 언론사 별로 크롤링을 할 수 있게한다.
  * 스포츠 뉴스란의 크롤링 파이썬 코딩
  * 종목별, 리그별 순위를 가져오는 기능을 추가한다.
  * 분야별 많이 본 뉴스 데이터로 csv파일을 만드는 기능을 추가한다.
  * 기간내에서 원하는 수의 뉴스를 읽어오는 기능을 추가한다.
  * 해외축구 시즌, 리그, 부문 입력하면 상위 20명 선수 출력기능
