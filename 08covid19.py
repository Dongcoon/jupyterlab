# 코로나19 시·도발생 현황
# 지역별 코로나 확진자 수 조회
# 지역을 입력하면 코로나 확진자 수 정보 출력
# 시도명GUBUN, 전일대비 증감수INC_DEC, 총확진자수DEF_CNT, 등록일시분초CREATE_DT
import requests
from bs4 import BeautifulSoup

url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey=GjgjTYLP10LmklhSDVDE6qQ8KZPc43DI%2BJ0iaotwuQpc5cFzNY19Uo269sO%2F5MQJ%2BGT6AmPGbn3prlagN3nf7A%3D%3D&pageNo=1&numOfRows=100&startCreateDt=20220101'

res = requests.get(url)
res.text[:500]

## 코로나 19_2
url = 'http://apis.data.go.kr/1352000/ODMS_COVID_04/callCovid04Api?serviceKey=GjgjTYLP10LmklhSDVDE6qQ8KZPc43DI%2BJ0iaotwuQpc5cFzNY19Uo269sO%2F5MQJ%2BGT6AmPGbn3prlagN3nf7A%3D%3D&pageNo=1&numOfRows=500&apiType=xml&std_day=2022-01-01&gubun=서울'

res = requests.get(url)
res.text

# 보건복지부_코로나19 시도 발생현황
url = 'http://apis.data.go.kr/1352000/ODMS_COVID_04/callCovid04Api?serviceKey=GjgjTYLP10LmklhSDVDE6qQ8KZPc43DI%2BJ0iaotwuQpc5cFzNY19Uo269sO%2F5MQJ%2BGT6AmPGbn3prlagN3nf7A%3D%3D&pageNo=1&numOfRows=500&apiType=xml&std_day=2022-01-01&gubun=서울'

res = requests.get(url)
res.text

## 공공데이터활용지원센터_코로나19 예방접종 위탁의료기관 조회서비스
url = 'https://api.odcloud.kr/api/apnmOrg/v1/list?page=1&perPage=10&returnType=JSON&cond%5BorgZipaddr%3A%3ALIKE%5D=마포구&serviceKey=GjgjTYLP10LmklhSDVDE6qQ8KZPc43DI%2BJ0iaotwuQpc5cFzNY19Uo269sO%2F5MQJ%2BGT6AmPGbn3prlagN3nf7A%3D%3D'
res = requests.get(url)
html = BeautifulSoup(res.text,'lxml')
html.text

## 공공데이터활용지원센터_코로나19 예방접종 위탁의료기관 조회서비스
url = 'https://api.odcloud.kr/api/apnmOrg/v1/list?page=1&perPage=10&cond%5BorgZipaddr%3A%3ALIKE%5D=%EB%A7%88%ED%8F%AC%EA%B5%AC'
headers = {'accept': 'application/json','Authorization': 'Infuser GjgjTYLP10LmklhSDVDE6qQ8KZPc43DI+J0iaotwuQpc5cFzNY19Uo269sO/5MQJ+GT6AmPGbn3prlagN3nf7A=='}

res = requests.get(url, headers=headers)
res.text