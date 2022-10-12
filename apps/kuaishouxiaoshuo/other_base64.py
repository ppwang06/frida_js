"""
base64实现
"""

import base64
import string

# base 字符集

base64_charset = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'


def encode(origin_bytes):
    """
    将bytes类型编码为base64
    :param origin_bytes:需要编码的bytes
    :return:base64字符串
    """

    # 将每一位bytes转换为二进制字符串
    base64_bytes = ['{:0>8}'.format(str(bin(b)).replace('0b', '')) for b in origin_bytes]
    print(base64_bytes)

    resp = ''
    nums = len(base64_bytes) // 3
    remain = len(base64_bytes) % 3

    integral_part = base64_bytes[0:3 * nums]
    while integral_part:
        # 取三个字节，以每6比特，转换为4个整数
        tmp_unit = ''.join(integral_part[0:3])
        tmp_unit = [int(tmp_unit[x: x + 6], 2) for x in [0, 6, 12, 18]]
        # 取对应base64字符
        resp += ''.join([base64_charset[i] for i in tmp_unit])
        integral_part = integral_part[3:]

    if remain:
        # 补齐三个字节，每个字节补充 0000 0000
        remain_part = ''.join(base64_bytes[3 * nums:]) + (3 - remain) * '0' * 8
        # 取三个字节，以每6比特，转换为4个整数
        # 剩余1字节可构造2个base64字符，补充==；剩余2字节可构造3个base64字符，补充=
        tmp_unit = [int(remain_part[x: x + 6], 2) for x in [0, 6, 12, 18]][:remain + 1]
        resp += ''.join([base64_charset[i] for i in tmp_unit]) + (3 - remain) * '='

    return resp


def decode(base64_str):
    """
    解码base64字符串
    :param base64_str:base64字符串
    :return:解码后的bytearray；若入参不是合法base64字符串，返回空bytearray
    """
    if not valid_base64_str(base64_str):
        return bytearray()

    # 对每一个base64字符取下标索引，并转换为6为二进制字符串
    base64_bytes = ['{:0>6}'.format(str(bin(base64_charset.index(s))).replace('0b', '')) for s in base64_str if
                    s != '=']
    resp = bytearray()
    nums = len(base64_bytes) // 4
    remain = len(base64_bytes) % 4
    integral_part = base64_bytes[0:4 * nums]

    while integral_part:
        # 取4个6位base64字符，作为3个字节
        tmp_unit = ''.join(integral_part[0:4])
        tmp_unit = [int(tmp_unit[x: x + 8], 2) for x in [0, 8, 16]]
        for i in tmp_unit:
            resp.append(i)
        integral_part = integral_part[4:]

    if remain:
        remain_part = ''.join(base64_bytes[nums * 4:])
        tmp_unit = [int(remain_part[i * 8:(i + 1) * 8], 2) for i in range(remain - 1)]
        for i in tmp_unit:
            resp.append(i)

    return resp


def valid_base64_str(b_str):
    """
    验证是否为合法base64字符串
    :param b_str: 待验证的base64字符串
    :return:是否合法
    """
    if len(b_str) % 4:
        return False

    for m in b_str:
        if m not in base64_charset:
            return False
    return True


if __name__ == '__main__':
    s = '我的目标是星辰大海. One piece, all Blue'.encode()
    local_base64 = encode(s)
    print('使用本地base64加密：', local_base64)
    b_base64 = base64.b64encode(s)
    print('使用base64加密：', b_base64.decode())

    print('使用本地base64解密：', decode(local_base64).decode())
    print('使用base64解密：', base64.b64decode(b_base64).decode())

