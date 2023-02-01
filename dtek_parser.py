"""
https://stackoverflow.com/questions/74743249/cant-access-site-programmatically
"""
import requests
import urllib.parse
from bs4 import BeautifulSoup as bs

resp_err_text = 'Request unsuccessful. Incapsula incident ID: 689000950002755466-6069776676886470'
resp_ok_text = 'Офіційний сайт ДТЕК'
dtek_url = r'https://www.dtek-kem.com.ua'
outfile = open('test.txt', 'w')
s = requests.Session()

s.cookies['incap_ses_689_2224657'] = '9y9nNtrZ8BCKJ9KqttKPCbqx2mMAAAAAhYD2jb7rgG8QGHcOUD9Apw==' #  Из брэйва
# s.cookies['incap_ses_689_2224657'] = 'hNErZjEedSu+SdaqttKPCfLE2mMAAAAACfxY5JE3nLKw5o28+sFzuQ=='  # Из пайчарма инвалид
# s.cookies['incap_ses_689_2224657'] = 'k42CXYdZzAOPcNaqttKPCbPF2mMAAAAAAtRFs2nAp1M8wLzEOOhAaA==' # Из эджа норм
# 9kMnXYv85A9Nn9aqttKPCbTG2mMAAAAA59qnu11/f01mKuYnr9oeOw==  # Из брейва, тоже скорей всего норм
resp = s.get(urllib.parse.urljoin(dtek_url, '/ua/shutdowns'))
print(resp)
print(s.cookies.items()[0], sep='\n')
soup = bs(resp.content, 'lxml')
if resp_ok_text not in soup.text:
    print('Cookie is invalid')
    s.close()
else:
    outfile.write(soup.text)
s.close()
outfile.close()
# =============================================================================================

import re
import json

d = soup.find_all(lambda tag: tag.name == 'script' and not tag.attrs)[-1].decode_contents()
d_parsed = {}
for i in re.findall(r'(?<=DisconSchedule\.)(\w+)(?:\s=\s)(.+)', d):
    d_parsed[i[0]] = json.loads(i[1])
d = d_parsed
# print(len(d['streets']), sep='\n')
print(d.keys(), sep='\n')
csrf = soup.find('meta', {'name': 'csrf-token'})['content']
print(csrf)
