"""
uuid  ->  base64
"""
import ctypes
from loguru import logger


c = [49, 102, 57, 101, 101, 100, 98, 101, 101, 98, 49, 57, 102, 55, 102, 101]
base = ""
for one in c:
    base += chr(one)
print(base)


def int_overflow(val):
    maxint = 2147483647
    if not -maxint-1 <= val <= maxint:
        val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
    return val


#  该方法后面为负数时  不对  不推荐
def unsigned_right_shift(n, i):
    # 如果js右移为0, 且数字小于0
    if i == 0 and n < 0:
        return n + 2 ** 32
    # 数字小于0，则转为32位无符号uint
    if n < 0:
        n = ctypes.c_uint32(n).value
    # 正常位移位数是为正数，但是为了兼容js之类的，负数就右移变成左移好了
    if i < 0:
        return -int_overflow(n << abs(i))
    return int_overflow(n >> i)


# 推荐使用这个
def unsinged_right_shift(x, y):
    x, y = ctypes.c_uint32(x).value, y % 32
    return ctypes.c_uint32(x >> y).value


def get_cipher_uuid(uuid: str):
    end_str = ""
    base_byte = ['K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7',
                 '8', '9', '+', '/']
    b_arr = [ord(i) for i in uuid]
    logger.info(f"dd:{b_arr}")
    i2 = 0
    while i2 <= len(b_arr)-1:
        b_arr2 = [0, 0, 0, 0]
        b2 = 0

        i3 = 0
        while i3 <= 2:
            i4 = i2 + i3
            if i4 <= len(b_arr) - 1:
                b_arr2[i3] = int_overflow(b2 | unsinged_right_shift(int_overflow(b_arr[i4] & 255), (i3 * 2) + 2))
                b2 = unsinged_right_shift(int_overflow(int_overflow((b_arr[i4] & 255) << (((2-i3) * 2) + 2)) & 255), 2)
            else:
                b_arr2[i3] = b2
                b2 = 64
            i3 += 1
        b_arr2[3] = b2

        i5 = 0
        while i5 <= 3:
            if b_arr2[i5] <= 63:
                end_str += base_byte[b_arr2[i5]]
            else:
                end_str += "="
            i5 += 1

        i2 += 3
    logger.info(f"最终结果为:{end_str}")


if __name__ == '__main__':
    uuid_str = "1f9eedbeeb19fdfg"
    get_cipher_uuid(uuid_str)


