# 크롤링 실습 4
# jtbc news 사이트의 속보 페이지에서
# 제목, 기사미리보기, 카테고리, 기자명, 송고날짜를 추출
# title, preview, category, reporter, pdate
# 단, 2021-07-20부터 21-07-15까지의 뉴스를 대상으로 한다.

import requests
from lxml import html

url = 'https://news.jtbc.co.kr/section/list.aspx'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
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

titles,contents = [],[]
category,writers,regdate = [],[],[]
news = [titles,contents,category,writers,regdate]

for i in range(20210715,20210720+1):
# 질의문자열을 위해 params 변수 정의
    params = {'pdate': i}
    res = requests.get(url, headers=headers, params=params)
    doctree = html.fromstring(res.text)

    docs = doctree.cssselect('dt.title_cr a')
    for title in docs:
        tit = title.text_content().replace(',','|')
        titles.append(tit)

    docs = doctree.cssselect('dd.desc a')
    for content in docs:
        cnt = content.text_content().strip().replace('   ','').replace(',','|')
        contents.append(cnt)

    docs = doctree.cssselect('span.location')
    for ctg in docs:
        cate = ctg.text_content().replace('[','').replace(']','').replace('JTBC','').replace('연합','').replace('>','').strip().replace(',','|').replace('\t','').replace('\n','')
        category.append(cate)

    docs = doctree.cssselect('span.writer')
    for writer in docs:
        wrt = writer.text_content().strip().replace(',','|')
        writers.append(wrt)

    docs = doctree.cssselect('span.date')
    for rgd in docs:
        pdate = rgd.text_content().strip().replace(',','|')
        regdate.append(to24h(pdate))
print(news)

# csv
header = '제목,기사미리보기,카테고리,기자,날짜\t\n'
with open('data/JTBC_P.csv','a',encoding='utf-8') as f:
    f.write(header)
    for i in range(len(titles)):
        title, content, ctg, writer, rgd = titles[i],contents[i],category[i], writers[i], regdate[i]
        f.write(f'"{title}","{content}","{ctg}","{writer}",{rgd}\n')

# json
import json
from collections import OrderedDict

news = []

with open('data/JTBC_P.json','a',encoding='UTF-8') as f:
    for i in range(len(titles)):
        new = OrderedDict()
        new['제목'] = titles[i]
        new['기사미리보기'] = contents[i]
        new['카테고리'] = category[i]
        new['기자'] = writers[i]
        new['날짜'] = regdate[i]
        news.append(new)
    f.write(json.dumps(news,ensure_ascii=False))