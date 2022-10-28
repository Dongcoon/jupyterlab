# 크롤링 실습
# 크롤링 대상 : www.kyobobook.co.kr
# 교보문고 쇼핑몰 사이트에서 '베스트' 페이지에서 '도서제목, 저자, 출판사, 출판일, 가격'들을 수집하세요
# 파일에 저장 : kyobobest.csv
# pip install webdriver_manager

from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

url = 'https://product.kyobobook.co.kr/bestseller/online?period=001'

# selenium 초기화
options = webdriver.ChromeOptions()
services = Service(ChromeDriverManager().install())  # 드라이버 자동설치
chrome = webdriver.Chrome(service=services, options=options)
chrome.get(url)
html = BeautifulSoup(chrome.page_source,'lxml')
chrome.close()

# 도서정보 추출하기
titles,authors,publishers,pubdates,prices = [],[],[],[],[]
for title in html.select('span.prod_name'):
    title = title.text.replace(',','|')
    titles.append(title)
for bkinfo in html.select('span.prod_author'):
    author = bkinfo.text.split('·')[0]
    author = author.strip()
    authors.append(author)
for bkinfo in html.select('span.prod_author'):
    publisher = bkinfo.text.split('·')[1]
    publisher = publisher.strip()
    publishers.append(publisher)
for bkinfo in html.select('span.prod_author'):
    pubdate = bkinfo.text.split('·')[2]
    pubdate = pubdate.replace('출시','')
    pubdate = pubdate.replace('.','-')
    pubdate = pubdate.strip()
    pubdates.append(pubdate)
for price in html.select('span.price'):
    price = price.text.replace('원','')
    price = price.replace(',','')
    prices.append(price)
# CSV
header = '도서명,저자,출판사,출판일,가격\n'
with open('data/kyobo_books.csv','a',encoding='utf-8') as f:
    f.write(header)
    for i in range(len(titles)):
        title, writer = titles[i], authors[i]
        pbs, pbd, price =  publishers[i],pubdates[i], prices[i]
        f.write(f' "{title}","{writer}","{pbs}","{pbd}","{price}"\n ')