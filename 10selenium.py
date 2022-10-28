## selenium으로 스크레핑 하기
# 웹브라우저를 이용한 작업들을 자동화할 수 있도록 특수제작된 브라우저
# 또한, ajax를 이용한 동적 웹페이지를 크롤링하는데에도 사용
# requests, bs4로 스크래핑할 수 없는 동적 데이터를 포함하는 웹 페이지를 원격 조작이 가능한 웹브라우저를 이용해서 처리

## seleniumhq.org
# chromedriver.chromium.org
# ChromeDriver 98.0.4758.102 (2022-02-17)
# chromedriver_win32.zip => chromedriver.exe
# C:\Program Files\Google\Chrome\Application

# pip install selenium => selenium-4.1.0 (2022-02-17)

# 한빛미디어에서 전체도서목록 크롤링하기
# 도서명, 저자, 가격, 발행일 추출
from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://www.hanbit.co.kr/store/books/full_book_list.html'
headers = {'https://product.kyobobook.co.kr/api/gw/pub/pdt/best-seller/online?page=1&per=20&period=001&dsplDvsnCode=000&dsplTrgtDvsnCode=001'}

# selenium 초기화
chrome = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

# 지정한 url로 접속
chrome.get(url)

# 응답받은 웹소스를 bs4에 저장
html = BeautifulSoup(chrome.page_source,'lxml')

# selenium 종료
chrome.close()

# 도서명, 저자, 출판일, 가격 추출
titles,writers,regdate,prices = [],[],[],[]
books_len = int(len(html.select('td'))/5)


for i in range(0,books_len+2,5):
    titles.append(html.select('td')[i+1].text.replace(',',''))
    writers.append(html.select('td')[i+2].text)
    regdate.append(html.select('td')[i+3].text)
    prices.append(html.select('td')[i+4].text.replace(',','').replace('원',''))

#방식 2
# for title in html.select('.tbl_type_list td:nth-child(2)'): print(title.text)
# for writer in html.select('table tbody td:nth-child(3)'): print(writer.text)
# for writer in html.select('table tbody td:nth-child(3)'): print(writer.text)
# for rdg in html.select('table tbody td:nth-child(4)'): print(rdg.text)
# for price in html.select('table tbody td:nth-child(5)'): print(price.text)

# csv저장
header = '도서명,저자,출판일,가격\n'

with open('data/allbooks.csv','a',encoding='utf-8') as f:
    f.write(header)
    for i in range(len(titles)):
        title, writer = titles[i], writers[i]
        rdg, price =  regdate[i], prices[i]
        f.write(f' "{title}","{writer}","{regdate}","{price}"\n ')

# JSON
import json
from collections import OrderedDict

books = []

with open('data/allbook.json','a',encoding='UTF-8') as f:
    for i in range(len(titles)):
        book = OrderedDict()
        book['도서명'] = titles[i]
        book['저자'] = writers[i]
        book['출판일'] = regdate[i]
        book['가격'] = prices[i]
        books.append(book)
    f.write(json.dumps(books,ensure_ascii=False))

