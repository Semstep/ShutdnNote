import requests
import urllib.parse
from bs4 import BeautifulSoup as bs

def showdic(dic, ofile=None):
    print(f'{dic}\n{"-" * 10}', file=ofile)
    for k, v in dic.items():
        print(f'{k}: {v}', file=ofile)

OUTFILE = 'test3.txt'
DTEK_URL = r'https://www.dtek-kem.com.ua'
PAGE_ADDR = r'/ua/shutdowns'

sess = requests.Session()
resp = sess.get(urllib.parse.urljoin(DTEK_URL, PAGE_ADDR))
with open(OUTFILE, 'w+') as of:
    print(resp.request, file=of)
    showdic(resp.headers, of)
    print('='*30, file=of)
    showdic(resp.cookies, of)
    # print('-'*30, file=of)
    # print(resp.json(), file=of)

print(sess.cookies.items()[0], sep='\n')

""" Заголовок запроса
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,
        application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7
cache-control: max-age=0
<тут всякие куки>
sec-ch-ua: "Chromium";v="108", "Opera";v="94", "Not)A;Brand";v="99"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: none
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0

Интересующее в заголовке ответа
incap_wrt_373=bnXbYwAAAADJRehaFwAI9QIQysOpsgUYmu3tngYgAijn6u2eBvDLpEzG85bhB4Mt4SKciNo=; HttpOnly; Path=/; SameSite=None; Secure; Max-Age=300
"""
"""
incap_ses_763_2224657=LN4QCM9/sGWur1RZPbmWCtfG02MAAAAAY7Zf0vCukCz3wzNrFNDvAA==
"""