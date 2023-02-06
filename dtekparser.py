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

COOCKA = r'incap_ses_473_2224657=SRjrBviyXzxfRzkeyW+QBn5a4WMAAAAA2Vdz87vKQXS+IIp7ceuv7w=='
# COOCKA = '='
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
            return None

        logger.info(f'{self.LOG_REC_NAME}: request successful')
        return self.responses[-1]


class DtekParser:
    soup = None

    def __init__(self, response: requests.Response):
        super().__init__()
        try:
            self.soup = bs(response.content, 'lxml')
            logger.info('soup created')
        except():
            logger.error(f'parser: SOUP CREATION ERROR')

    def get_shutd_group(self):
        ...

    def get_rawdata_a(self):
        d = self.soup.find_all(lambda tag: tag.name == 'script' and not tag.attrs)[-1].decode_contents()
        with open(r'store\script_filtered.json', 'w') as fs:
            # fs.write(d)
            json.dump(d, fs)
            logger.info(f'filtered data stored in {fs.name}')

if __name__ == '__main__':
    ds = DtekSession()
    rsp = ds.get_site_response()
    if not rsp:
        raise Exception(IOError)
    dp = DtekParser(rsp)
    dp.get_rawdata_a()