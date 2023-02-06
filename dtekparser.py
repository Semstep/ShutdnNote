import logging
import requests
import urllib.parse
from typing import List
from bs4 import BeautifulSoup as bs
import json

COOCKA = r'incap_ses_689_2224657=LTT/A0nvXC0ZxSSrttKPCa/23GMAAAAAQIECCT/9OmufISMUssKZtA=='
RESP_TEXT_UNSUCCESS = 'Request unsuccessful. Incapsula incident'  # ID: 727000860105380165-252961049657415053'

class DtekSession:
    DTEK_URL = r'https://www.dtek-kem.com.ua'
    PAGE_ADDR = r'/ua/shutdowns'
    sess: requests.Session()
    resp: List[requests.Response]
    is_ok: bool = False

    def __init__(self):
        self.sess = requests.session()
        # self.logger = logging.getLogger()
        # self.logger(level=logging.INFO, filename="session.log", filemode="w",
        #                     format="%(asctime)s %(levelname)s %(message)s")
        super().__init__()

    def set_cookie(self, name: str = '', val: str = '', *, rawstr: str = '') -> requests.Session():
        # пока берем из браузера, если реквестсом, то 'request unsuccessful. incapsula incident id'
        # формат из браузера: incap_ses_689_2224657=vfTqI6LKnEjARQirttKPCS0W3GMAAAAA6C83W9Ll4txHMj4dBJ61fA==
        """
        Устанавливает значение куков взятых руками из браузера
        """
        if not rawstr:
            self.sess.cookies[name] = val

        nv = rawstr.split('=', 1)
        self.sess.cookies[nv[0]] = nv[1]

    def get_site_response(self):
        self.set_cookie(COOCKA)
        self.resp.append(self.sess.get(urllib.parse.urljoin(self.DTEK_URL, self.PAGE_ADDR)))
        if RESP_TEXT_UNSUCCESS in self.resp[-1].text:
            ...


class DtekParser:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_shutd_group(self):
        ...

    def get_rawdata_a(self):
        ...


