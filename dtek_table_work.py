import serve
from pprint import pprint
import re
import json

tbl = serve.unpicle('pickle\soupfind.bin')
d_parsed = {}
for i in re.findall(r'(?<=DisconSchedule\.)(\w+)(?:\s=\s)(.+)',tbl):
    d_parsed[i[0]] = json.loads(i[1])
d = d_parsed
# with open('logs\\testtbl01.txt', 'w') as f:
#     pprint(d, f)
for i, k in enumerate(d.keys()):
    fname = f'logs\\tbl_{k}.txt'
    with open(fname, 'w') as f:
        pprint(d[k], f)
        print(f'table {k} created')
print(len(d['streets']))