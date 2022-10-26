# BeatutifulSoup
# www.crummy.com/software/BeautifulSoup
# 유명한 스크래핑/크롤링 패키지
# 주로 HTML과 XML파일에서 데이터 추출시 사용
# pip install beautifulsoup4

# pip install beautifulsoup4

# 크롤링 연습 6
# 네이버 증권에서 일본/미국/영국 환율 크롤링 하기
import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/'
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

res = requests.get(url, headers = header)

# bs4를 이용해서 DOM 계층구조로 변환
# BeautifulSoup(대상, 변환방식)
# bs4에서 제공하는 변환방식 : html.parser, lxml(추천)
html = BeautifulSoup(res.text,'lxml')
str(html)[:500]

# 변환된 문서객체 탐색
# 요소명 : 객체명.태그명
# 여러 요소 : 객체명.find_all('태그명')
# 여러 요소 : 객체명.select('선택자')

# 문서 제목 출력 1
html.title

# 문서 제목 출력 2
html.title.string

# 문서에서 p 요소 출력
html.p

# 문서에서 p 요소 출력(첫번째 p 요소 출력)
html.find_all('p')[:5]

# 문서에서 p 요소 출력
html.select('p')[:5]

# 문서 제목 출력 3
# html.select('title')[0].string
html.select('title')[0].text

# 환율정보 추출¶
country = html.select('div.group1 table.tbl_home tbody tr th a')
rate = html.select('div.group1 table.tbl_home tbody tr td')

country[0].text, rate[0].text,country[1].text, rate[2].text,country[2].text, rate[4].text