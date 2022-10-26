# 크롤링 실습 3
# jtbc news 사이트의 속보 페이지에서
# 제목, 기사미리보기, 카테고리, 기자명, 송고날짜를 추출
# title, preview, category, reporter, pdate
# 파일에 저장 : jtbcnews.json

# 리스트
import requests
from lxml import html

def to24h(time):
    # 2022-10-26 오전 11:56:00
    pd = time.split(' ')
    pt = pd[2].split(':')

    if (pd[1] == '오후') and (pt[0] != '12'):
        pt[0] = int(pt[0]) + 12

    elif (pd[1] == '오전') and (pt[0] == '12'):
        pt[0] = int(pt[0]) - 12

    time = f'{pd[0]} {pt[0]}:{pt[1]}:{pt[2]}'
    return time

url = 'https://news.jtbc.co.kr/section/list.aspx?scode='
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

news = [titles,contents,category,writers,regdate]
titles,contents,category,writers,regdate = [],[],[],[],[]

res = requests.get(url, headers=header, params=param)
doctree = html.fromstring(res.text)

docs = doctree.cssselect('dt.title_cr a')
for title in docs:
    tit = title.text_content()
    titles.append(tit)

docs = doctree.cssselect('dd.desc a')
for content in docs:
    cnt = content.text_content().strip().replace('   ','')
    contents.append(cnt)

docs = doctree.cssselect('span.location')
for ctg in docs:
    cate = ctg.text_content().replace('[JTBC','').replace(']','').replace('>','').strip()
    category.append(cate)

docs = doctree.cssselect('span.writer')
for writer in docs:
    wrt = writer.text_content().strip()
    writers.append(wrt)

docs = doctree.cssselect('span.date')
for rgd in docs:
    pdate = rgd.text_content().strip()
    regdate.append(to24h(pdate))
print(news)