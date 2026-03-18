"""
https://match.yuanrenxue.cn/match/1
"""
import execjs
import time
import json
from curl_cffi import requests
from loguru import logger


hexcase = 0
b64pad = ""
chrsz = 16

def safe_add(x, y):
    return (x + y) & 0xFFFFFFFF

def bit_rol(num, cnt):
    return ((num << cnt) | (num >> (32 - cnt))) & 0xFFFFFFFF

def str2binl(s):
    bin = []
    mask = (1 << chrsz) - 1
    for b in range(0, len(s) * chrsz, chrsz):
        index = b >> 5
        while len(bin) <= index:
            bin.append(0)
        char_code = ord(s[b // chrsz]) & mask
        bin[index] |= (char_code << (b % 32))
        bin[index] &= 0xFFFFFFFF
    return bin

def binl2hex(binarray):
    hex_tab = "0123456789abcdef" if not hexcase else "0123456789ABCDEF"
    hex_str = ""
    for i in range(len(binarray) * 4):
        word = binarray[i >> 2]
        high = (word >> ((i % 4) * 8 + 4)) & 0x0F
        low = (word >> ((i % 4) * 8)) & 0x0F
        hex_str += hex_tab[high] + hex_tab[low]
    return hex_str

def md5_cmn(h, e, d, c, g, f):
    h &= 0xFFFFFFFF
    e &= 0xFFFFFFFF
    d &= 0xFFFFFFFF
    c &= 0xFFFFFFFF
    f &= 0xFFFFFFFF
    tmp = safe_add(e, h)
    tmp2 = safe_add(c, f)
    tmp3 = safe_add(tmp, tmp2)
    rolled = bit_rol(tmp3, g)
    return safe_add(rolled, d)

def md5_ff(a, b, c, d, x, s, t):
    tmp = ((b & c) | ((~b) & d)) & 0xFFFFFFFF
    return md5_cmn(tmp, a, b, x, s, t)

def md5_gg(a, b, c, d, x, s, t):
    tmp = ((b & d) | (c & (~d))) & 0xFFFFFFFF
    return md5_cmn(tmp, a, b, x, s, t)

def md5_hh(a, b, c, d, x, s, t):
    tmp = (b ^ c ^ d) & 0xFFFFFFFF
    return md5_cmn(tmp, a, b, x, s, t)

def md5_ii(a, b, c, d, x, s, t):
    tmp = (c ^ (b | (~d))) & 0xFFFFFFFF
    return md5_cmn(tmp, a, b, x, s, t)

def core_md5(x, bit_len):
    # 填充：先补一个 1，再补 0，最后附加 32 位长度
    index = bit_len >> 5
    while len(x) <= index:
        x.append(0)
    x[index] |= 0x80 << (bit_len % 32)
    x[index] &= 0xFFFFFFFF

    pos = (((bit_len + 64) >> 9) << 4) + 14
    while len(x) <= pos:
        x.append(0)
    x[pos] = bit_len

    # 确保总字数是 16 的倍数（原算法隐含此要求）
    while len(x) % 16 != 0:
        x.append(0)

    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325476

    for i in range(0, len(x), 16):
        aa, bb, cc, dd = a, b, c, d

        # 第一轮
        a = md5_ff(a, b, c, d, x[i+0], 7, -680976936)
        d = md5_ff(d, a, b, c, x[i+1], 12, -389564586)
        c = md5_ff(c, d, a, b, x[i+2], 17, 606105819)
        b = md5_ff(b, c, d, a, x[i+3], 22, -1044525330)
        a = md5_ff(a, b, c, d, x[i+4], 7, -176418897)
        d = md5_ff(d, a, b, c, x[i+5], 12, 1200080426)
        c = md5_ff(c, d, a, b, x[i+6], 17, -1473231341)
        b = md5_ff(b, c, d, a, x[i+7], 22, -45705983)
        a = md5_ff(a, b, c, d, x[i+8], 7, 1770035416)
        d = md5_ff(d, a, b, c, x[i+9], 12, -1958414417)
        c = md5_ff(c, d, a, b, x[i+10], 17, -42063)
        b = md5_ff(b, c, d, a, x[i+11], 22, -1990404162)
        a = md5_ff(a, b, c, d, x[i+12], 7, 1804660682)
        d = md5_ff(d, a, b, c, x[i+13], 12, -40341101)
        c = md5_ff(c, d, a, b, x[i+14], 17, -1502002290)
        b = md5_ff(b, c, d, a, x[i+15], 22, 1236535329)

        # 第二轮
        a = md5_gg(a, b, c, d, x[i+1], 5, -165796510)
        d = md5_gg(d, a, b, c, x[i+6], 9, -1069501632)
        c = md5_gg(c, d, a, b, x[i+11], 14, 643717713)
        b = md5_gg(b, c, d, a, x[i+0], 20, -373897302)
        a = md5_gg(a, b, c, d, x[i+5], 5, -701558691)
        d = md5_gg(d, a, b, c, x[i+10], 9, 38016083)
        c = md5_gg(c, d, a, b, x[i+15], 14, -660478335)
        b = md5_gg(b, c, d, a, x[i+4], 20, -405537848)
        a = md5_gg(a, b, c, d, x[i+9], 5, 568446438)
        d = md5_gg(d, a, b, c, x[i+14], 9, -1019803690)
        c = md5_gg(c, d, a, b, x[i+3], 14, -187363961)
        b = md5_gg(b, c, d, a, x[i+8], 20, 1163531501)
        a = md5_gg(a, b, c, d, x[i+13], 5, -1444681467)
        d = md5_gg(d, a, b, c, x[i+2], 9, -51403784)
        c = md5_gg(c, d, a, b, x[i+7], 14, 1735328473)
        b = md5_gg(b, c, d, a, x[i+12], 20, -1921207734)

        # 第三轮
        a = md5_hh(a, b, c, d, x[i+5], 4, -378558)
        d = md5_hh(d, a, b, c, x[i+8], 11, -2022574463)
        c = md5_hh(c, d, a, b, x[i+11], 16, 1839030562)
        b = md5_hh(b, c, d, a, x[i+14], 23, -35309556)
        a = md5_hh(a, b, c, d, x[i+1], 4, -1530992060)
        d = md5_hh(d, a, b, c, x[i+4], 11, 1272893353)
        c = md5_hh(c, d, a, b, x[i+7], 16, -155497632)
        b = md5_hh(b, c, d, a, x[i+10], 23, -1094730640)
        a = md5_hh(a, b, c, d, x[i+13], 4, 681279174)
        d = md5_hh(d, a, b, c, x[i+0], 11, -358537222)
        c = md5_hh(c, d, a, b, x[i+3], 16, -722881979)
        b = md5_hh(b, c, d, a, x[i+6], 23, 76029189)
        a = md5_hh(a, b, c, d, x[i+9], 4, -640364487)
        d = md5_hh(d, a, b, c, x[i+12], 11, -421815835)
        c = md5_hh(c, d, a, b, x[i+15], 16, 530742520)
        b = md5_hh(b, c, d, a, x[i+2], 23, -995338651)

        # 第四轮
        a = md5_ii(a, b, c, d, x[i+0], 6, -198630844)
        d = md5_ii(d, a, b, c, x[i+7], 10, 11261161415)
        c = md5_ii(c, d, a, b, x[i+14], 15, -1416354905)
        b = md5_ii(b, c, d, a, x[i+5], 21, -57434055)
        a = md5_ii(a, b, c, d, x[i+12], 6, 1700485571)
        d = md5_ii(d, a, b, c, x[i+3], 10, -1894446606)
        c = md5_ii(c, d, a, b, x[i+10], 15, -1051523)
        b = md5_ii(b, c, d, a, x[i+1], 21, -2054922799)
        a = md5_ii(a, b, c, d, x[i+8], 6, 1873313359)
        d = md5_ii(d, a, b, c, x[i+15], 10, -30611744)
        c = md5_ii(c, d, a, b, x[i+6], 15, -1560198380)
        b = md5_ii(b, c, d, a, x[i+13], 21, 1309151649)
        a = md5_ii(a, b, c, d, x[i+4], 6, -145523070)
        d = md5_ii(d, a, b, c, x[i+11], 10, -1120210379)
        c = md5_ii(c, d, a, b, x[i+2], 15, 718787259)
        b = md5_ii(b, c, d, a, x[i+9], 21, -343485551)

        a = safe_add(a, aa)
        b = safe_add(b, bb)
        c = safe_add(c, cc)
        d = safe_add(d, dd)

    return [a, b, c, d]

def hex_md5(s):
    return binl2hex(core_md5(str2binl(s), len(s) * chrsz))




headers = {
    "Host": "match.yuanrenxue.cn",
    "user-agent": "yuanrenxue",
    "referer": "https://match.yuanrenxue.cn/match/1",
}
# 更换Cookies
cookies = {
    "sessionid": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
}

def js_from_file(file_name):
    with open(file_name, 'r', encoding='UTF-8') as file:
        result = file.read()
    return result
context1 = execjs.compile(js_from_file('./js_match_1.js'))


def one_handler():
    url = "https://match.yuanrenxue.cn/api/question/1"
    end_num = 0
    for page in range(1, 6):
        logger.info(f"开始第{page}页数据")
        t = (int(time.time()) * 1000) + 100000000
        result1 = context1.call("hex_md5", str(t))
        m = f"{result1}丨{str(t)[:10]}"
        params = {
            "page": str(page),
            "pageSize": "10",
            "kw": "",
            "m": m
        }
        response = requests.get(url, headers=headers, cookies=cookies, params=params)
        data_info_list = json.loads(response.text).get("data")
        sum_total = sum(data_info_list)
        logger.info(f"第{page}页数据为{sum_total}")
        end_num += sum_total
    logger.info(end_num)


def two_handler():
    url = "https://match.yuanrenxue.cn/api/question/1"
    end_num = 0
    for page in range(1, 6):
        logger.info(f"开始第{page}页数据")
        t = (int(time.time()) * 1000) + 100000000
        result1 = hex_md5(str(t))
        m = f"{result1}丨{str(t)[:10]}"
        params = {
            "page": str(page),
            "pageSize": "10",
            "kw": "",
            "m": m
        }
        response = requests.get(url, headers=headers, cookies=cookies, params=params)
        data_info_list = json.loads(response.text).get("data")
        sum_total = sum(data_info_list)
        logger.info(f"第{page}页数据为{sum_total}")
        end_num += sum_total
    logger.info(end_num)


if __name__ == '__main__':
    two_handler()





