"""
7455204571726974338  --> 103,118,53,15,1,-89,-115,-126
3fn54QGnja05MjgzZDBkMDY2NDgwM2QzOTBkYWQ5ZDg3NTA1ZTgxZjdmZjY4NGEzYzZjYmM1ZDM=

python版本 base64
bArr[i2] = (byte) (255 & j2)  java byte强转对应 int_to_byte
负数的十进制 转 二进制    int_to_bin
"""
import ctypes
import string


def int_overflow(val):
    maxint = 2147483647
    if not -maxint-1 <= val <= maxint:
        val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
    return val


# 推荐使用这个
def unsinged_right_shift(x, y):
    x, y = ctypes.c_uint32(x).value, y % 32
    return ctypes.c_uint32(x >> y).value


def change_to_(j2):
    base_arr = [0 for i in range(8)]
    i2 = 7
    while i2 >= 0:
        base_arr[i2] = int_to_byte(255 & j2)
        j2 >>= 8
        i2 -= 1
    return base_arr


# 实现java的类型强转 (byte) 2093322535     # -256 ~ 255
def int_to_byte(target_int: int) -> int:
    if -128 <= target_int <= 127:
        return target_int
    cc = bin(target_int)
    byte_cc = cc[-8:]
    if byte_cc.startswith('1') and target_int < 0:
        return -(int(byte_cc, 2) - 256)
    if byte_cc.startswith('1') and target_int > 0:
        return int(byte_cc, 2) - 256
    if byte_cc.startswith('0') and target_int > 0:
        return int(byte_cc, 2)
    return -(int(byte_cc, 2))


base64_charset = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
def encode(base64_bytes):
    """
    将bytes类型编码为base64
    :param origin_bytes:需要编码的bytes
    :return:base64字符串
    """

    # 将每一位bytes转换为二进制字符串
    # base64_bytes = ['{:0>8}'.format(str(bin(b)).replace('0b', '')) for b in origin_bytes]

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


def int_to_bin(number, index, feature=True):
    """
    index为该数据位宽,number为待转换数据,
    feature为True则进行十进制转二进制，为False则进行二进制转十进制。
    """
    # 十进制转换为二进制
    if feature is True:
        if number >= 0:
            b = bin(number)
            b = '0' * (index+2 - len(b)) + b
        else:
            b = 2 ** index + number
            b = bin(b)
            # 注意这里算出来的结果是补码
            b = '1' * (index+2 - len(b)) + b
        b = b.replace("0b", "")
        b = b.replace("-", "")
        return b
    # 二进制转换为十进制
    elif feature is False:
        i = int(str(number), 2)
        # 如果是负数
        if i >= 2**(index-1):
            i -= (2**index-i)
            return i
        else:
            return i


if __name__ == '__main__':
    one_index = change_to_(-6167232042394742408)
    _sig3_48 = "8293c0c0120f87cbe9cac9c85bfb272de5ca97b3d6dbd5c3"
    for one in _sig3_48:
        one_index.append(ord(one))
    print(one_index)
    res = [int_to_bin(i, 8) for i in one_index]
    print(res)
    print(encode(res))
    # d = ""
    # for c in [49,54,54,53,53,53,52,55,55,50,52,50,49]:
    #     d += chr(c)
    # print(d)




