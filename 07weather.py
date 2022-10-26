# 기상청을 이용한 날씨 정보 출력
# weather.go.kr
# https://www.weather.go.kr/w/pop/rss-guide.do
# 지역을 입력하면 날씨를 출력

# RSS 서비스 이용하기
# Really Simple Syndication, Rich Site Summary
# 블로그처럼 컨텐츠 업데이트가 자주 일어나는 웹사이트에서, 업데이트된 정보를 쉽게 구독자들에게 제공하기 위해 XML을 기초로 만들어진 데이터 형식
# RSS서비스를 이용하면 업데이트된 정보를 찾기 위해 홈페이지에 일일이 방문하지 않아도 업데이트될 때마다 빠르고 편리하게 확인할 수 있음

import requests
from bs4 import BeautifulSoup

# 동네예보 > 중기예보 > 서울,경기
url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

res = requests.get(url, headers = headers)
html = BeautifulSoup(res.text, 'html.parser')

# 서울 지역 날씨 정보 출력
region = '서울'
whter = None

for loc in html.select('location'):
    if loc.city.text == region:
        whter = loc.data

whter.tmef.text, whter.wf.text, whter.tmn.text, whter.tmx.text, whter.rnst.text

# 동네예보 > 시간별 예보
# http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1144070000
# day : 0(오늘),1(내일), 2(모레)

# 동네예보 > 시간별 예보
url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1144070000'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

res = requests.get(url, headers = headers)
html = BeautifulSoup(res.text, 'html.parser')

day, temp = [], []
tmx, tmn, wfkor = [], [], []

mangwon2 = [day, temp, tmx, tmn, wfkor]

for i in range(len(html.select('data'))):
    day.append(html.select('data day')[i].text)
    temp.append(html.select('data temp')[i].text)
    tmx.append(html.select('data tmx')[i].text)
    tmn.append(html.select('data tmn')[i].text)
    wfkor.append(html.select('data wfkor')[i].text)
print(mangwon2)

# 현재시간 기준 다음날 9시의 날씨 정보 조회
whter = None
for data in html.select('data'):
    if data.day.text =='1' and data.hour.text == '9':
        whter = data
        break

whter.wfkor.text, whter.tmn.text, whter.tmx.text, whter.pop.text, whter.reh.text