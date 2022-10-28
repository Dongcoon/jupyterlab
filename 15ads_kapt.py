# 아파트 단지 정보에서 주차장 정보 추출
# 관련 사이트 : k-apt.go.kr
# 메인페이지 팝업창 닫기 => '단지정보' 클릭
# 2022.06, 서울, 서초구, 반포동 소재 모든 아파트에 대한 정보 추출
# 아파트명, 도로명주소, 주차장 정보
import time
from bs4 import BeautifulSoup

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

# 저장할 정보
aptname, address, parl = [],[],[]

syear = '2022년'
smonth = '06월'
ssido = '서울특별시'
sgugun = '서초구'
sdong = '반포동'

## 함수
def select():
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

def scroll(idx):
    elm = chrome.find_element(By.CSS_SELECTOR, f'#mCSB_2_container ul li:nth-child({idx})')

    height = elm.size['height']
    pos = '-' + str((idx - 4) * height) + 'px'
    elm = chrome.find_element(By.CSS_SELECTOR, '#mCSB_2_container')
    chrome.execute_script(
        f'arguments[0].style="position: relative; top: {pos}; left: 0px;"', elm)
    time.sleep(1)

## 크롬 실행
options = webdriver.ChromeOptions()
services = Service(ChromeDriverManager().install())  # 드라이버 자동설치
chrome = webdriver.Chrome(service=services, options=options)

url = 'http://www.k-apt.go.kr/'

chrome.get(url)

chrome.maximize_window() # 창 최대로 키우기
time.sleep(2)

chrome.find_element(By.CSS_SELECTOR,'.fas').click()
time.sleep(1)
chrome.find_element(By.XPATH,'//a[@title="단지정보"]').click()

chrome.find_element(By.XPATH,'//a[@title="우리단지 기본정보"]').click()
time.sleep(3)

# 아파트 개수 산정
select()
html = BeautifulSoup(chrome.page_source, 'lxml')
aptnum = len(html.select('#mCSB_2_container ul li a p'))

## 반복시작
for apt in range(1, aptnum + 1):
    select()

    scroll(apt)

    # 아파트명 저장
    aptname.append(chrome.find_element(By.CSS_SELECTOR, f'#mCSB_2_container ul li:nth-child({apt}) a p').text)

    # 우리단지 기본정보 이동
    chrome.find_element(By.CSS_SELECTOR, f'#mCSB_2_container ul li:nth-child({apt})').click()
    time.sleep(2)

    # 도로명주소 저장
    address.append(chrome.find_element(By.ID, 'addrList_addr2').text)

    # 관리시설정보 이동
    chrome.find_element(By.CSS_SELECTOR, 'ul.lnbNav li:nth-child(3) a').click()
    time.sleep(2)

    # 주차장 정보 저장
    on = chrome.find_element(By.ID, 'kaptd_pcnt').text
    bot = chrome.find_element(By.ID, 'kaptd_pcntu').text
    tot = chrome.find_element(By.ID, 'kaptd_total_pcnt').text
    parl.append(f'지상: {on} | 지하: {bot} | 총 {tot}대')
    time.sleep(2)
    # 뺵
    chrome.back()
    time.sleep(2)
    chrome.back()

    time.sleep(2)

## 리스트 확인
aptname, address, parl

## 종료
chrome.close()