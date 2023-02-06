import requests
import urllib.parse
from bs4 import BeautifulSoup as bs


# proxies = {
#    'http': 'http://127.0.0.1:8888',
#    'https': 'http://127.0.0.1:8888'
# }

def showdic(dic, name='', ofile=None):
    print(f'{"-" * 10} {name} {"-" * 10}', file=ofile)
    for k, v in dic.items():
        print(f'{k}: {v}', file=ofile)


OUTFILE = 'test3.txt'
DTEK_URL = r'https://www.dtek-kem.com.ua'
PAGE_ADDR = r'/ua/shutdowns'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

if __name__ == '__main__':
    sess = requests.Session()
    # responses = sess.get(urllib.parse.urljoin(DTEK_URL, PAGE_ADDR), proxies=proxies, verify=False) # для работы с фидлером
    resp = sess.get(urllib.parse.urljoin(DTEK_URL, PAGE_ADDR))
    with open(OUTFILE, 'a') as of:
        print('*' * 20)
        print(resp.request, file=of)
        showdic(resp.headers, of)
        print('=' * 30, file=of)
        showdic(resp.cookies, of)
        # print('-'*30, file=of)
        # print(responses.json(), file=of)
        print('', file=of)
        print(resp, file=of)

    print(sess.cookies.items()[0], sep='\n')
