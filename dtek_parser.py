"""
https://stackoverflow.com/questions/74743249/cant-access-site-programmatically
"""
import requests
import urllib.parse
from bs4 import BeautifulSoup as bs
from get_dtek_cookie import showdic
from dtek_pickle_table import set_cookie

resp_err_text = 'Request unsuccessful. Incapsula incident ID: 689000950002755466-6069776676886470'
resp_ok_text = 'Офіційний сайт ДТЕК'
dtek_url = r'https://www.dtek-kem.com.ua'
outfile = open('test.txt', 'w')
s = requests.Session()

# s.cookies[r'incap_ses_689_2224657'] = r'g3yiYL2nzBOgRgSrttKPCc4A3GMAAAAAFyONVoVXdmQMv/hevwLYdA=='
# # s.cookies['visid_incap_2224657'] = '0U/cw1+IS1+3wORv6R5za5r922MAAAAAQUIPAAAAAADie8Y8jyxSMdOSW2ci9ZQm'
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
set_cookie(s, rawstr=r'incap_ses_763_2224657=LN4QCM9/sGWur1RZPbmWCtfG02MAAAAAY7Zf0vCukCz3wzNrFNDvAA==')
resp = s.get(urllib.parse.urljoin(dtek_url, '/ua/shutdowns'))
print(resp.status_code)
soup = bs(resp.content, 'lxml')
print(soup.prettify(), file=outfile)
print(soup.title)
if resp_ok_text not in soup.text:
    print('Cookie is invalid')
else:
    outfile.write(soup.text)
outfile.close()
# =============================================================================================

# import re
# import json
#
# d = soup.find_all(lambda tag: tag.name == 'script' and not tag.attrs)[-1].decode_contents()
# d_parsed = {}
# for i in re.findall(r'(?<=DisconSchedule\.)(\w+)(?:\s=\s)(.+)', d):
#     d_parsed[i[0]] = json.loads(i[1])
# d = d_parsed
# # print(len(d['streets']), sep='\n')
# print(d.keys(), sep='\n')
# csrf = soup.find('meta', {'name': 'csrf-token'})['content']
# print(csrf)
