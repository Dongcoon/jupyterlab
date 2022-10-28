# 크롤링 실습
# 크롤링 대상 : https://movie.daum.net/main
# 다음 영화 사이트에서 '영화명, 평점, 예매율'들을 수집하세요
# 파일에 저장 : movies.csv
# selenium
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

url = 'https://movie.daum.net/main'
options = webdriver.ChromeOptions()
services = Service(ChromeDriverManager().install())  # 드라이버 자동설치
chrome = webdriver.Chrome(service=services, options=options)

# 웹페이지 요소들이 다 로딩될때까지의 대기시간 설정
chrome.implicitly_wait(5)
chrome.get(url)
html = BeautifulSoup(chrome.page_source,'lxml')
chrome.close()

# 영화 정보 추출하기
titles,scores,rsvs = [],[],[]
for title in html.select('section.feature_home strong.tit_item a.link_txt'):
    title = title.text.replace(',','.')
    titles.append(title)
for sc in html.select('span.txt_append span.txt_num:nth-child(1)'):
    sc = sc.text.strip()
    scores.append(sc)
for rs in html.select('span.txt_append span.txt_num:nth-child(3)'):
    rs = rs.text.strip().replace('%','')
    rsvs.append(rs)


# CSV
header = '영화명,평점,예매율\n'
with open('data/movies.csv','a',encoding='utf-8') as f:
    f.write(header)
    for i in range(len(titles)):
        title, scr, rsv = titles[i], scores[i], rsvs[i]
        f.write(f' "{title}","{scr}","{rsv}"\n ')