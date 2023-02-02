import requests
import urllib.parse
from bs4 import BeautifulSoup as bs
from get_dtek_cookie import showdic

COOCKA = r'incap_ses_689_2224657=vfTqI6LKnEjARQirttKPCS0W3GMAAAAA6C83W9Ll4txHMj4dBJ61fA=='
LOGDIR = 'logs'
OUTFILE = 'test3.txt'
DTEK_URL = r'https://www.dtek-kem.com.ua'
PAGE_ADDR = r'/ua/shutdowns'
TITLE_OK = 'Офіційний сайт ДТЕК'
DEBUG_FILE = 'log.txt'


def wrtlog(text: str, delim: str='\n'):
    with open(LOGDIR+'\\' + DEBUG_FILE, 'a', encoding='utf-8') as lf:
        lf.write(text+delim)


def set_cookie(sess: requests.Session(), name: str='', val: str='',*, rawstr: str='') -> requests.Session():
    # пока берем из браузера, если реквестсом, то 'request unsuccessful. incapsula incident id'
    # формат из браузера: incap_ses_689_2224657=vfTqI6LKnEjARQirttKPCS0W3GMAAAAA6C83W9Ll4txHMj4dBJ61fA==
    """
    Устанавливает значение куков из браузера
    """
    if not rawstr:
        sess.cookies[name] = val
        return sess.cookies
    nv = rawstr.split('=', 1)
    sess.cookies[nv[0]] = nv[1]
    return sess


sess = requests.Session()
sess = set_cookie(sess, rawstr=COOCKA)
resp = sess.get(urllib.parse.urljoin(DTEK_URL, PAGE_ADDR))
print(resp.status_code)
showdic(resp.headers)

# https://www.crummy.com/software/BeautifulSoup/bs4/doc.ru/bs4ru.html -- тут по супу вроде неплохо