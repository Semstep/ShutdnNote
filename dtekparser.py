import logging
import requests
import urllib.parse
from typing import List
from bs4 import BeautifulSoup as bs
import json

logger = logging.getLogger('parser')
logger.setLevel(logging.DEBUG)
loghandler = logging.FileHandler(r'logs\\' + logger.name + '.log')
loghandler.setFormatter(logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s"))
logger.addHandler(loghandler)

# COOCKA = r'incap_ses_689_2224657=LTT/A0nvXC0ZxSSrttKPCa/23GMAAAAAQIECCT/9OmufISMUssKZtA=='
COOCKA = '='
RESP_TEXT_UNSUCCESS = 'Request unsuccessful. Incapsula incident'  # ID: 727000860105380165-252961049657415053'

class DtekSession:
    DTEK_URL = r'https://www.dtek-kem.com.ua'
    PAGE_ADDR = r'/ua/shutdowns'
    sess: requests.Session()
    responses: List[requests.Response] = []
    is_ok: bool = False
    LOG_REC_NAME = 'DtekSession'

    def __init__(self):
        self.sess = requests.session()
        logger.debug('Session created')
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
        logger.debug(f'{self.LOG_REC_NAME}: cookie is {self.sess.cookies}')

    def get_site_response(self):
        self.set_cookie(rawstr=COOCKA)
        self.responses.append(self.sess.get(urllib.parse.urljoin(self.DTEK_URL, self.PAGE_ADDR)))
        if RESP_TEXT_UNSUCCESS in self.responses[-1].text:
            self.is_ok = False
            logger.error(f'{self.LOG_REC_NAME}: request REJECTED')
        else:
            logger.info(f'{self.LOG_REC_NAME}: request successful, {self.responses[-1].}')


class DtekParser:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_shutd_group(self):
        ...

    def get_rawdata_a(self):
        ...


if __name__ == '__main__':
    ds = DtekSession()
    ds.get_site_response()
