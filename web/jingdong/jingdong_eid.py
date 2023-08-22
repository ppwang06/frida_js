"""
eid
"""
import json
import math
from urllib.parse import quote


def td_encrypt(encrypt_info):
    n = json.dumps(encrypt_info, separators=(",", ":"))
    n = quote(n).replace("%28", "(").replace("%27", "'").replace("%29", ")").replace("/", "%2F")
    start = 0
    end_str = ""
    base_code_table = "23IL<N01c7KvwZO56RSTAfghiFyzWJqVabGH4PQdopUrsCuX*xeBjkltDEmn89.- "
    while start < len(n):
        c = ord(n[start])
        start += 1
        _9c = False if start > len(n) - 1 else ord(n[start])
        start += 1
        _ba = False if start > len(n) - 1 else ord(n[start])
        start += 1

        aa = c >> 2
        bb = (c & 0x3) << 0x4 | _9c >> 0x4
        cc = (_9c & 0xf) << 0x2 | _ba >> 0x6
        dd = _ba & 0x3f
        if not _9c:
            cc = dd = 0x40
        elif not _ba:
            dd = 0x40
        end_str = end_str + base_code_table[aa] + base_code_table[bb] + base_code_table[cc] + base_code_table[dd]
    return end_str + "/"


if __name__ == '__main__':
    d = {
        "pin": "",
        "oid": "",
        "bizId": "JDLS-PHB",
        "fc": None,
        "mode": "strict",
        "p": "s",
        "fp": "8488daf22b83dbcea7a7d3920acdb1a2",
        "ctype": 1,
        "v": "3.1.1.0",
        "f": "3",
        "o": "ranking.m.jd.com/comLandingPage/comLandingPage",
        "qs": "contentId=6397&rankType=10&showhead=no",
        "jsTk": None,
        "qi": ""
    }
    print(td_encrypt(d))

