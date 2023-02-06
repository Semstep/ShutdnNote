import serve
from pprint import pprint
import re
import json
def to_set(inp: list) -> set:
    res = set(inp)
    llen, slen = len(inp), len(res)
    if llen != slen:
        print(f'В списке есть {llen-slen} повторений')
    return res


def compare_street_tables(tbl_a_file, tbl_b_file) -> set:
    """
    Принимает 2 файла с названием улицы в каждой строке
    """
    with open(tbl_a_file, 'r') as f1:
        lst_a = [l.strip('\n').strip(" '").strip("',").strip() for l in f1.readlines()]
    with open(tbl_b_file, 'r') as f2:
        lst_b = [l.strip('\n').strip(" '").strip("',").strip() for l in f2.readlines()]

    set_a, set_b = to_set(lst_a), to_set(lst_b)
    set_res = set_a ^ set_b
    print(f'Нашлось {len(set_res)} различий')
    print(f'Список {"A" if len(set_a) > len(set_b) else "B"} длиннее на {len(set_res)}')
    print(*set_res, sep='\n')
    return set_res


# tbl = serve.unpicle('pickle\soupfind.bin')
# d_parsed = {}
# for i in re.findall(r'(?<=DisconSchedule\.)(\w+)(?:\s=\s)(.+)',tbl):
#     d_parsed[i[0]] = json.loads(i[1])
# d = d_parsed
# with open('logs\\testtbl01.txt', 'w') as f:
#     pprint(d, f)
# for i, k in enumerate(d.keys()):
#     fname = f'logs\\tbl_{k}.txt'
#     with open(fname, 'w') as f:
#         pprint(d[k], f)
#         print(f'table {k} created')
# print(len(d['streets']))
# with open(r'logs\bak\tbl_streets.txt', 'r') as fl:
#     strts_b = [l.strip('\n').strip(" '").strip("',").strip() for l in fl.readlines()]
# with open(r'logs\tbl_streets.txt') as fl:
#     strts_a = [l.strip('\n').strip(" '").strip("',").strip() for l in fl.readlines()]

compare_street_tables(r'logs\tbl_streets.txt', r'logs\bak\tbl_streets.txt')