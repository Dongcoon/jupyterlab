# 아파트 단지 정보에서 주차장 정보 추출
# 관련 사이트 : k-apt.go.kr
# 메인페이지 팝업창 닫기 => '단지정보' 클릭
# => 2022.06, 서울, 강남구, 삼성동, 아이파크삼성동 클릭

import time
from bs4 import BeautifulSoup

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
services = Service(ChromeDriverManager().install())  # 드라이버 자동설치
chrome = webdriver.Chrome(service=services, options=options)

url = 'http://www.k-apt.go.kr/'

chrome.get(url)

chrome.maximize_window() # 창 최대로 키우기
time.sleep(3)

## 팝업창 닫기
# 1
chrome.find_element(By.CSS_SELECTOR,'.fas').click()
time.sleep(1)

# 2
chrome.find_element(By.CSS_SELECTOR,'#layerPopup20211208 button').click()
time.sleep(1)

# 3
chrome.execute_script('closePopupLayer("#layerPopup20211208")')
time.sleep(1)

## 우리단지 기본정보로 이동

# 우리단지 기본정보 클릭
chrome.find_element(By.CSS_SELECTOR,'.wp220 li:nth-child(1) a').click()

# 1
# 단지정보 클릭
chrome.find_element(By.CSS_SELECTOR,'#nav li:first-child a').click()
time.sleep(1)

# 2
# 단지정보 클릭
chrome.find_element(By.XPATH,'//a[@title="단지정보"]').click()
time.sleep(1)

## 검색할 단지정보 설정
syear = '2022년'
smonth = '06월'
ssido = '서울특별시'
sgugun = '강남구'
sdong = '삼성동'

year = Select(chrome.find_element(By.NAME,'searchYYYY'))
year.select_by_visible_text(syear)
time.sleep(1)

month = Select(chrome.find_element(By.NAME,'searchMM'))
month.select_by_visible_text(smonth)
time.sleep(1)

sido = Select(chrome.find_element(By.NAME,'combo_SIDO'))
sido.select_by_visible_text(ssido)
time.sleep(2)

gugun = Select(chrome.find_element(By.NAME,'combo_SGG'))
gugun.select_by_visible_text(sgugun)
time.sleep(2)

dong = Select(chrome.find_element(By.NAME,'combo_EMD'))
dong.select_by_visible_text(sdong)
time.sleep(1)

## 결과 목록 자동 스크롤
# 결과 목록 각 항목 높이 알아내기
elm = chrome.find_element(By.CSS_SELECTOR,'#mCSB_2_container ul li:nth-child(1)')
# 현재 화면에 출력된 결과목록 수 : 4
height = elm.size['height']
pos = '-' + str((idx - 4) * height) + 'px'
elm = chrome.find_element(By.CSS_SELECTOR,'#mCSB_2_container')
chrome.execute_script(
    f'arguments[0].style="position: relative; top: {pos}; left: 0px;"', elm)
time.sleep(1)

## 대상 항목 클릭
chrome.find_element(By.CSS_SELECTOR,f'#mCSB_2_container ul li:nth-child(1)').click()

## 관리시설 정보로 이동
chrome.find_element(By.CSS_SELECTOR,'ul.lnbNav li:nth-child(3) a').click()

## 주차대수 출력

## 아파트 목록 출력
# 1.
aname = []
html = BeautifulSoup(chrome.page_source, 'lxml')
for name in html.select('p.aptS_rLName'):
    name = name.text
    name = name.replace('<p class="aptS_rLName">','')
    name = name.replace('</p>','')
    aname.append(name)
print(aname)

# 2.
aname = []
html = BeautifulSoup(chrome.page_source, 'lxml')
for name in html.select('#mCSB_2_container ul li a p'):
    aname.append(name.text)
    print(name.text)

# 첫번째 아파트 클릭
chrome.find_element(By.CSS_SELECTOR,'#mCSB_2_container ul li:nth-child(1) a').click()

