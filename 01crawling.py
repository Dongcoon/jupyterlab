# 크롤링 개요
# 웹에서 데이터를 수집하는 작업
# 크롤러 또는 스파이더라는 프로그램을 이용해서 웹 사이트등에서 데이터를 추출함
# crawling 또는 Scraping은 웹페이지의 내용에서 필요한 데이터를 추출하는 행위를 의미함
# 단, 데이터 추출을 위해 필요한 모든 일련의 과정 역시 크롤링에 포함하기도 함
# 크롤링을 제대로 하기 위해서는 웹이 작동하는 방식과 웹 표준기술을 잘 파악하고 있어야 함

### 설치할 패키지
# pip install requests
# pip install lxml
# pip install cssselect

# 라이브러리 import
import requests
from xml.etree import ElementTree
from lxml.html import fromstring
from lxml import html

# 크롤링 실습 1
# 크롤링 대성 : hanb.co.kr
# 한빛 출판네트워크 사이트의 '**새로나온책**' 페이지에서 '**도서명, 저자, 가격**' 들을 수집

# 크롤링할 대상 url 지정
url = 'https://www.hanbit.co.kr/store/books/new_book_list.html'

# 지정한 url에 get방식으로 접속해서 html 소스를 받아옴
# requests.get(접속할주소)
res = requests.get(url)

# 요청결과 확인
res.status_code

# 요청에 대한 응답헤더 확인
res.headers

# 응답으로 받은 소스 확인 (테스트 형식)
res.text[:500]

### CSS선택자나 xpath문법으로 필요한 요소 추출
# cssselect(css선택자)4
# xpath(xpath경로)

# 응답으로 받은 소스를 문서객체로 생성
doctree = html.fromstring(res.text)

# 도서제목 : 모든 p 요소들 중에서 클래스명이 book_tit인 요소
titles = doctree.cssselect('p.book_tit')

# 객체명.text_content : 객체의 텍스트노드 값을 추출
for title in titles:
    print(title.text_content())

# 도서저자 :
writers = doctree.cssselect('p.book_writer')

for writer in writers:
    print(writer.text_content())

# 도서가격 : 모든 span 요소들 중에서 클래스명이 price인 요소
prices = doctree.cssselect('span.price')

for price in prices:
    price = price.text_content()
    price = price.replace(',','')
    price = price.replace('원','')
    print(price)

### 추출한 데이터들을 리스트에 저장
books = []
titles = doctree.cssselect('p.book_tit')
writers = doctree.cssselect('p.book_writer')
prices = doctree.cssselect('span.price')
for i in range(len(titles)):
    book = []
    price = prices[i].text_content().replace(',', '').replace('원', '')
    book.append(titles[i].text_content())
    book.append(writers[i].text_content())
    book.append(int(price))
    books.append(book)

print(books)

### 리스트에 저장된 데이터들을 csv 파일에 저장
# 저장형식1 : "tit, 'writ','pri'
header = 'title,writer,price\n'

with open('data/newbooks.csv','a',encoding='utf-8') as f:
    f.write(header)
    for i in range(len(titles)):
        title, writer, price = titles[i].text_content(), writers[i].text_content(), prices[i].text_content().replace(',','').replace('원','')
        f.write(f'"{title}","{writer}",{price}\n')

# 저장형식2 : pandas
import pandas as pd
import pymysql

df = pd.DataFrame(books, columns = ['title','writer','price'])
df.to_csv('book_csv.csv',index=False,encoding='utf-8')

## 추출한 데이터들을 데이터베이스에 저장
url = 'bigdata.ccdt7ih2qkyl.ap-northeast-2.rds.amazonaws.com'
userid = 'admin'
passwd = 'Bigdata_2022'
dbname = 'bigdata'

conn = pymysql.connect(host=url,user=userid,password=passwd,
                       database=dbname,charset='utf8')

for i in range(len(books)):
    cur = conn.cursor()
    sql = 'insert into newbooks(title,writer,price) values(%s,%s,%s)'
    cur.execute(sql,books[i])
    conn.commit()

cur.close()
conn.close()


