# https://www.crummy.com/software/BeautifulSoup/bs4/doc.ru/bs4ru.html -- тут по супу вроде неплохо
import requests
import urllib.parse
from bs4 import BeautifulSoup as bs
import pickle
from get_dtek_cookie import showdic
from pprint import pprint
import serve

# COOCKA = r'incap_ses_689_2224657=vfTqI6LKnEjARQirttKPCS0W3GMAAAAA6C83W9Ll4txHMj4dBJ61fA=='
# COOCKA = r'incap_ses_763_2224657=LN4QCM9/sGWur1RZPbmWCtfG02MAAAAAY7Zf0vCukCz3wzNrFNDvAA=='
COOCKA = r'incap_ses_689_2224657=LTT/A0nvXC0ZxSSrttKPCa/23GMAAAAAQIECCT/9OmufISMUssKZtA=='
LOGDIR = 'logs\\'
OUTFILE = 'test3.txt'
DTEK_URL = r'https://www.dtek-kem.com.ua'
PAGE_ADDR = r'/ua/shutdowns'
TITLE_OK = 'Офіційний сайт ДТЕК'
DEBUG_FILE = 'log.txt'
SOUP_DIR = 'pickle\\'
SOUP_FILE = 'soup.bin'
resp_ok_text = 'Офіційний сайт ДТЕК'


def make_headers(headers_file: str) -> dict:
    res = {}
    with open(headers_file, 'r') as hf:
        for hdr in hf.readlines():
            if not hdr or hdr == '\n':
                continue
            k, v = hdr.split(':')
            res[k.strip()] = v.strip()
    return res


def wrtlog(text: str, delim: str = '\n', isrewrite=False):
    mode = 'w' if isrewrite else 'a'
    with open(LOGDIR + DEBUG_FILE, mode, encoding='utf-8') as lf:
        lf.write(text + delim)


def set_cookie(sess: requests.Session(), name: str = '', val: str = '', *, rawstr: str = '') -> requests.Session():
    # пока берем из браузера, если реквестсом, то 'request unsuccessful. incapsula incident id'
    # формат из браузера: incap_ses_689_2224657=vfTqI6LKnEjARQirttKPCS0W3GMAAAAA6C83W9Ll4txHMj4dBJ61fA==
    """
    Устанавливает значение куков взятых из браузера
    """
    if not rawstr:
        sess.cookies[name] = val
        return sess.cookies
    nv = rawstr.split('=', 1)
    sess.cookies[nv[0]] = nv[1]
    return sess


NEED_DTEK_CONN = True

if __name__ == '__main__':
    if NEED_DTEK_CONN:
        sess = requests.Session()
        sess = set_cookie(sess, rawstr=COOCKA)  # иногда можно и без этого, хз когда
        resp = sess.get(urllib.parse.urljoin(DTEK_URL, PAGE_ADDR))  # , headers=make_headers('headers.txt'))
        print(resp.status_code)
        print(SOUP_DIR + SOUP_FILE)
        # print(resp.content)
        soup = bs(resp.content, 'lxml')
        if resp_ok_text not in soup.text:
            print('Cookie is invalid')
        else:
            print(soup.title)
            serve.pickle_put(soup, SOUP_DIR + SOUP_FILE)
            print(f'soup was pickled into {SOUP_DIR + SOUP_FILE}')
    else:
        soup = serve.unpicle(SOUP_DIR + SOUP_FILE)

print(soup.get_text())
