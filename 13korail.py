# selenium으로 코레일에 로그인한 후 열차 예매하기

import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
services = Service(ChromeDriverManager().install())  # 드라이버 자동설치
chrome = webdriver.Chrome(service=services, options=options)

userid = '1370335512'
passwd = '1q2w3e!@#'
deptst = '서울'
arrvst = '목포'
dpyear = '2022'
dpmonth = '11'
dpday = '11'
dphour = '10 (오전10)'

# 코레일 메인 페이지 방문

url = 'https://www.letskorail.com/ebizprd/prdMain.do'

chrome.get(url)

chrome.maximize_window() # 창 최대로 키우기
time.sleep(3)

# 팝업창 닫기 : 자식창으로 제어를 넘긴 후 창을 닫음
chrome.switch_to.window(chrome.window_handles[1])
chrome.close()
time.sleep(3)

# 부모창으로 제어 이동
chrome.switch_to.window(chrome.window_handles[0])
time.sleep(1)

# 로그인 하기
# selenium에서 특정요소를 css선택자로 제어하려면 find_element함수 사용
# find_element(By.선택자유형,선택자)
# 셀레니엄에서 input 요소에 값을 입력하려면 send_keys함수사용

# 로그인 이미지 버튼 클릭
chrome.find_element(By.CSS_SELECTOR,'.gnb_list li:nth-child(2) a').click()
time.sleep(2)

# 아이디입력
uid = chrome.find_element(By.ID,'txtMember')
pwd = chrome.find_element(By.ID,'txtPwd')
uid.send_keys(userid)
pwd.send_keys(passwd)

chrome.find_element(By.CSS_SELECTOR,'ul.login_mem li.btn_login a').click()

time.sleep(3)

# 열차예매 페이지로 이동

# 경고창 닫기
# chrome.switch_to.alert.acept()
# time.sleep(1)

# 팝업창 닫기 : 자식창으로 제어를 넘긴 후 창을 닫음
chrome.switch_to.window(chrome.window_handles[1])
chrome.close()

# 부모창으로 제어 이동
chrome.switch_to.window(chrome.window_handles[0])
time.sleep(1)

# 승차권 메뉴 클릭
chrome.find_element(By.CSS_SELECTOR,'.lnb_m01 a').click()
time.sleep(1)

## 예약할 열차 정보 설정 및조회

# 종별 선택 - ktx
chrome.find_element(By.ID,'selGoTrainRa00').click()
time.sleep(1)

# 출발/도착역 선택
start = chrome.find_element(By.ID,'start')
start.clear()
start.send_keys(deptst)

get = chrome.find_element(By.ID,'get')
get.clear()
get.send_keys(arrvst)
time.sleep(1)

# 출발일 설정
syear = Select(chrome.find_element(By.ID,'s_year'))
syear.select_by_visible_text(dpyear)
time.sleep(1)

smonth = Select(chrome.find_element(By.ID,'s_month'))
smonth.select_by_visible_text(dpmonth)
time.sleep(1)

syear = Select(chrome.find_element(By.ID,'s_day'))
syear.select_by_visible_text(dpday)
time.sleep(1)

syear = Select(chrome.find_element(By.ID,'s_hour'))
syear.select_by_visible_text(dphour)
time.sleep(1)

# 조회하기 클릭
chrome.find_element(By.CSS_SELECTOR,'p.btn_inq a').click()


## 예약버튼 클릭
# 브라우져의 특정액션은 자바스크립트를 이용해서 처리
# selenium에서 자바스크립트를 실행하려면 excute_script함수 사용

# 조회화면 스크롤
chrome.execute_script('window.scrollTo(0,1080);')
time.sleep(1)

# 예약버튼 클릭

# 종료
chrome.close()
