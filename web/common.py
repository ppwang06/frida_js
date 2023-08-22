"""
python 与 js  函数之间转换
python                          js
int("BB", base=16)            parseInt

unsigned_right_shift          >>>
int_overflow（^）               ^
int_overflow（<<）              <<

charCodeAt                     ord（）

chr(72)                String.fromCharCode(72)
str.charAt(index)       str 取对应字符串
"""
import ctypes

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


# 推荐这个
def unsinged_right_shift(x, y):
    x, y = ctypes.c_uint32(x).value, y % 32
    return ctypes.c_uint32(x >> y).value