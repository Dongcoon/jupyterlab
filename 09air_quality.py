# 죽음의 먼지, 잿빛 재앙, 은밀한 살인자 => 미세먼지
# 세계보건기구에 따르면 2014년, 전세계에서 약 700만 명이 미세먼지로 인해 조기 사망

# 1930년 벨기에의 뮤즈 벨리, 1948년 미국 펜실베이니아 주의 도노라,
# 1952년 런던 스모그 등 대규모 재난을 겪으며
# 대기오염이 건강에 막대한 피해를 끼칠 수 있다는 사실을 인지함함

# 먼지는 대기 중 떠다니거나 흩날려 내려오는 입자상의 물질을 의미
# 대기오염 물질에는 가스상 물질과 입자상 물질이 존재

# 미세먼지, 초미세먼지는 입자상 물질을 크기별로 세분화한 것
# 1990년대에는 입자의 지름이 50마이크로미터 이하인 총먼지(TSP)
# 2000년대에는 지름이 10마이크로미터 이하인 PM10,
# 2010년대에는 지름이 2.5마이크로미터 이하인 PM2.5로 나눔
# => 우리나라에서는 통상적으로 PM10을 미세먼지로, PM2.5를 초미세먼지로 번역해 옴

# 2016년, 2017년, 환경부에서는 해외의 용어와 국내의 용어를 맞추기 위해
# PM10을 부유먼지로 PM2.5를 미세먼지로 용어를 정비함
# 초미세먼지는 PM1 또는 PM0.1을 가리키는 말

# 미세먼지/초미세먼지 등급에 따른 이모지 출력
# 미세먼지 : ~30 ~80 ~150 151~
# 초미세먼지 : ~15 ~35 ~75 76~
# 😀 😐 😫 😱

# 시도별 실시간 대기오염정보 조회
# 지역을 입력하면 측정소명stationName, 측정일시dataTime,
# 미세먼지(PM10)농도pm10Value, 초미세먼지(PM25)농도pm25Value 출력
import requests
from bs4 import BeautifulSoup

url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
returnType = 'xml'
params = {'serviceKey':'GjgjTYLP10LmklhSDVDE6qQ8KZPc43DI%2BJ0iaotwuQpc5cFzNY19Uo269sO%2F5MQJ%2BGT6AmPGbn3prlagN3nf7A%3D%3D',
         'returnType':returnType,'sidoName':'전국','pageNo':1, 'numOfRows':10000, 'ver':'1.0'}

res = requests.get(url,params=params)
html = BeautifulSoup(res.text,'lxml')

# 초미세먼지, 미세먼지 정보 추출
for item in html.select('item'):
    if item.stationname.text == '마포구':
        pm10v = item.pm10value.text
        pm25v = item.pm25value.text
        print(item.stationname.text,item.datatime.text, pm10v,pm10(int(pm10v)),pm25v,pm25(int(pm25v)))

city, pm10_r, pm25_r = [],[],[]
for item in html.select('item'):
    city.append(item.stationname.text)
    pm10_r.append(item.pm10value.text)
    pm25_r.append(item.pm25value.text)

# 미세먼지, 초미세먼지 등급부여
# 미세먼지/초미세먼지 등급에 따른 이모지 출력
# 미세먼지 : 30, ~80, ~150, 151
# 초미세먼지 : 15, ~35, ~75, 76
# 😀 😐 😫 😱

def pm10(val):
    grade = '😀'
    if val <= 30:
        grade = '😀'
    elif 30 < val <= 80:
        grade = '😐'
    elif 80 < val <= 150:
        grade = '😫'
    else:
        grade = '😱'

    return grade


def pm25(val):
    grade = '😀'
    if val <= 15:
        grade = '😀'
    elif 15 < val <= 35:
        grade = '😐'
    elif 35 < val <= 75:
        grade = '😫'
    else:
        grade = '😱'
    return grade

# 대기오염정보를 JSON으로 불러오기
import json
returnType = 'json'
params = {'serviceKey':'GjgjTYLP10LmklhSDVDE6qQ8KZPc43DI%2BJ0iaotwuQpc5cFzNY19Uo269sO%2F5MQJ%2BGT6AmPGbn3prlagN3nf7A%3D%3D',
         'returnType':returnType,'sidoName':'전국','pageNo':1, 'numOfRows':10000, 'ver':'1.0'}

res = requests.get(url,params=params)

# 텍스트로 구성된 json 문자열을 객체로 변환
json_data = json.loads(res.text)

# json에서 객체의 속성 호출 : 객체명['속성명'], 객체명.속성명
for item in json_data['response']['body']['items']:
    if item['stationName'] == '마포구':
        pm10v = item['pm10Value']
        pm25v = item['pm25Value']
        print(item['stationName'], item['dataTime'], pm10v,pm10(int(pm10v)),pm25v,pm25(int(pm25v)))