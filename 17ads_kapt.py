# 아파트 단지 정보에서 주차장 정보 추출
# 관련 사이트 : k-apt.go.kr
# 메인페이지 팝업창 닫기 => '단지정보' 클릭
# 2022.06, 서울, 서초구, 반포동 소재 모든 아파트에 대한 정보 추출
# 아파트명, 도로명주소, 주차장 정보
import requests as req
from bs4 import BeautifulSoup

# 아파트 이름
url = 'http://www.k-apt.go.kr/kaptinfo/getKaptInfo_poi.do'
params = {'bjd_code':'11650107','search_date':'202209'}

res = req.get(url, params=params)

res.text

# 우리단지 기본정보
url = 'http://www.k-apt.go.kr/kaptinfo/getKaptList.do'
params = {'bjd_code':'11650107','search_date':'202209'}

res = req.get(url, params=params)

res.text

# 관리시설정보
url = 'http://www.k-apt.go.kr/kaptinfo/getKaptInfo_detail.do'
params = {'kapt_code':'A10024254'}

res = req.get(url, params=params)

res.text

import json
html = BeautifulSoup(res.text, 'lxml')
aptinfo = json.loads(res.text)

# 주차정보 추출
aptinfo.get('resultMap_kapt').get('KAPTD_PCNT'), \
aptinfo.get('resultMap_kapt').get('KAPTD_PCNTU')

# 도로정보
aptinfo.get('resultMap_kapt_addrList')[1].get('KAPT_CODE'), \
aptinfo.get('resultMap_kapt_addrList')[1].get('ADDR')
