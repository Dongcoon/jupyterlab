# 크롤링 실습 1
# 크롤링 대성 : hanb.co.kr
# 한빛 출판네트워크 사이트의 '새로나온책' 페이지에서 '도서명, 저자, 가격' 들을 수집
# 1 ~ 5 페이지 분량의 도서 정보 수집

import time
import requests
from xml.etree import ElementTree
from lxml.html import fromstring
from lxml import html

# 크롤링 관련 변수 정의
url = 'https://www.hanbit.co.kr/store/books/new_book_list.html'
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

# 추출한 데이터들을 리스트에 저장
books = []

for i in range(1,5+1):
    # 질의문자열을 위해 params 변수 정의
    param = {'page': i}
    # http header와 질의문자열을 이용해서 requests 모듈 호출
    res = requests.get(url, headers=header, params=param)
    doctree = html.fromstring(res.text)

    titles = doctree.cssselect('p.book_tit')
    writers = doctree.cssselect('p.book_writer')
    prices = doctree.cssselect('span.price')
    for i in range(len(titles)):
        book = []
        price = prices[i].text_content().replace(',','').replace('원','')
        book.append(titles[i].text_content())
        book.append(writers[i].text_content())
        book.append(int(price))
        books.append(book)
    time.sleep(2)  # 2초동안 잠시 대기
print(books)

# 리스트에 저장된 데이터들을 csv 파일에 저장
books = []
titles,writers,prices = [],[],[]

for i in range(1,5+1):
    # 질의문자열을 위해 params 변수 정의
    param = {'page': i}
    # http header와 질의문자열을 이용해서 requests 모듈 호출
    res = requests.get(url, headers=header, params=param)
    doctree = html.fromstring(res.text)

    docs = doctree.cssselect('p.book_tit')
    for title in docs:
        titles.append(title.text_content())
    docs = doctree.cssselect('p.book_writer')
    for writer in docs:
        writers.append(writer.text_content().replace(',','').replace('원',''))
    docs = doctree.cssselect('span.price')
    for price in docs:
        prices.append(price.text_content())
time.sleep(2)  # 2초동안 잠시 대기

header = 'title,writer,price\n'
with open('data/newbooks_page.csv','a',encoding='utf-8') as f:
    f.write(header)
    for i in range(len(titles)):
        title, writer, price = titles[i], writers[i], prices[i]
        f.write(f'"{title}","{writer}",{price}\n')

# 리스트에 저장된 데이터들을 JSON 파일에 저장
import json
from collections import OrderedDict

books = []
with open('data/newbooks_page.json', 'a', encoding='utf-8') as f:
    for i in range(len(titles)):
        book = OrderedDict()
        book['title'] = titles[i]
        book['writer'] = writers[i]
        book['price'] = prices[i]
        books.append(book)

    f.write(json.dumps(books, ensure_ascii=False))