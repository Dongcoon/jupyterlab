# 크롤링 실습 5
# 크롤링 대상 : www.kyobobook.co.kr
# 교보문고 쇼핑몰 사이트에서 '베스트' 페이지에서
# '도서제목, 저자, 출판사, 출판일, 가격'들을 수집하세요
# 파일에 저장 : kyobobest.csv

# REST API 형식으로 베스트셀러 도서 정보 추출

url = 'https://product.kyobobook.co.kr/api/gw/pub/pdt/best-seller/online?page=1&per=20&period=001&dsplDvsnCode=000&dsplTrgtDvsnCode=001'

res = requests.get(url, headers=header)

res.text