import binascii
import ctypes
import struct

SV = [0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee, 0xf57c0faf,
      0x4787c62a, 0xa8304613, 0xfd469501, 0x698098d8, 0x8b44f7af,
      0xffff5bb1, 0x895cd7be, 0x6b901122, 0xfd987193, 0xa679438e,
      0x49b40821, 0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa,
      0xd62f105d, 0x2441453, 0xd8a1e681, 0xe7d3fbc8, 0x21e1cde6,
      0xc33707d6, 0xf4d50d87, 0x455a14ed, 0xa9e3e905, 0xfcefa3f8,
      0x676f02d9, 0x8d2a4c8a, 0xfffa3942, 0x8771f681, 0x6d9d6122,
      0xfde5380c, 0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
      0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x4881d05, 0xd9d4d039,
      0xe6db99e5, 0x1fa27cf8, 0xc4ac5665, 0xf4292244, 0x432aff97,
      0xab9423a7, 0xfc93a039, 0x655b59c3, 0x8f0ccc92, 0xffeff47d,
      0x85845dd1, 0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1,
      0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391]


def binvalue(val, bitsize):
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise ("binary value larger than the expected size")
    while len(binval) < bitsize:
        binval = "0" + binval
    return binval


def string_to_bit_array(text):
    array = list()
    for char in text:
        binval = binvalue(char, 8)
        array.extend([int(x) for x in list(binval)])
    return array


def leftCircularShift(k, bits):
    bits = bits % 32
    k = k % (2 ** 32)
    upper = (k << bits) % (2 ** 32)
    result = upper | (k >> (32 - (bits)))
    return (result)


def blockDivide(block, chunks):
    result = []
    size = len(block) // chunks
    for i in range(0, chunks):
        result.append(int.from_bytes(block[i * size:(i + 1) * size], byteorder="little"))
    return result


def F(X, Y, Z):
    compute = ((X & Y) | ((~X) & Z))
    return compute


def G(X, Y, Z):
    return ((X & Z) | (Y & (~Z)))


def H(X, Y, Z):
    return (X ^ Y ^ Z)


def I(X, Y, Z):
    return (Y ^ (X | (~Z)))


def FF(a, b, c, d, M, s, t):
    result = b + leftCircularShift((a + F(b, c, d) + M + t), s)
    return (result)


def GG(a, b, c, d, M, s, t):
    result = b + leftCircularShift((a + G(b, c, d) + M + t), s)
    return (result)


def HH(a, b, c, d, M, s, t):
    result = b + leftCircularShift((a + H(b, c, d) + M + t), s)
    return (result)


def II(a, b, c, d, M, s, t):
    result = b + leftCircularShift((a + I(b, c, d) + M + t), s)
    return (result)


def fmt8(num):
    bighex = "{0:08x}".format(num)
    binver = binascii.unhexlify(bighex)
    result = "{0:08x}".format(int.from_bytes(binver, byteorder='little'))
    return (result)


def bitlen(bitstring):
    return len(bitstring) * 8


def unsinged_right_shift(x, y):
    x, y = ctypes.c_uint32(x).value, y % 32
    return ctypes.c_uint32(x >> y).value


def int_overflow(val):
    maxint = 2147483647
    if not -maxint-1 <= val <= maxint:
        val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
    return val


def rotl(n, t):
    return int_overflow(n << t) | unsinged_right_shift(n, 32-t)


def endian(n):
    if isinstance(n, int):
        return (0x00FF00FF & rotl(n, 8)) | (0xff00ff00 & rotl(n, 24))
    else:
        return [endian(x) for x in n]


def convert_int_array(input_int):
    result = []
    for num in input_int:
        packed = struct.pack('>I', num)
        byte_values = list(packed)
        result.extend(byte_values)
    return [b for b in result]


def to_hex_string(n):
    t = []
    for number in n:
        t.append(hex(number >> 4)[2:])
        t.append(hex(number & 15)[2:])
    return ''.join(t)


def md5sum(msg_list):
    msg = bytes(msg_list)
    msgLen = bitlen(msg) % (2 ** 64)
    msg = msg + b'\x80'
    zeroPad = (448 - (msgLen + 8) % 512) % 512
    zeroPad //= 8
    msg = msg + b'\x00' * zeroPad + msgLen.to_bytes(8, byteorder='little')
    print(msg)
    msgLen = bitlen(msg)
    iterations = msgLen // 512
    A = 0x67452301
    B = 0xefcdab89
    C = 0x98badcfe
    D = 0x10325476

    for i in range(0, iterations):
        a = A
        b = B
        c = C
        d = D
        block = msg[i * 64:(i + 1) * 64]
        M = blockDivide(block, 16)
        a = FF(a, b, c, d, M[0], 7, SV[0])
        d = FF(d, a, b, c, M[1], 12, SV[1])
        c = FF(c, d, a, b, M[2], 17, SV[2])
        b = FF(b, c, d, a, M[3], 22, SV[3])
        a = FF(a, b, c, d, M[4], 7, SV[4])
        d = FF(d, a, b, c, M[5], 12, SV[5])
        c = FF(c, d, a, b, M[6], 17, SV[6])
        b = FF(b, c, d, a, M[7], 22, SV[7])
        a = FF(a, b, c, d, M[8], 7, SV[8])
        d = FF(d, a, b, c, M[9], 12, SV[9])
        c = FF(c, d, a, b, M[10], 17, SV[10])
        b = FF(b, c, d, a, M[11], 22, SV[11])
        a = FF(a, b, c, d, M[12], 7, SV[12])
        d = FF(d, a, b, c, M[13], 12, SV[13])
        c = FF(c, d, a, b, M[14], 17, SV[14])
        b = FF(b, c, d, a, M[15], 22, SV[15])

        a = GG(a, b, c, d, M[1], 5, SV[16])
        d = GG(d, a, b, c, M[6], 9, SV[17])
        c = GG(c, d, a, b, M[11], 14, SV[18])
        b = GG(b, c, d, a, M[0], 20, SV[19])
        a = GG(a, b, c, d, M[5], 5, SV[20])
        d = GG(d, a, b, c, M[10], 9, SV[21])
        c = GG(c, d, a, b, M[15], 14, SV[22])
        b = GG(b, c, d, a, M[4], 20, SV[23])
        a = GG(a, b, c, d, M[9], 5, SV[24])
        d = GG(d, a, b, c, M[14], 9, SV[25])
        c = GG(c, d, a, b, M[3], 14, SV[26])
        b = GG(b, c, d, a, M[8], 20, SV[27])
        a = GG(a, b, c, d, M[13], 5, SV[28])
        d = GG(d, a, b, c, M[2], 9, SV[29])
        c = GG(c, d, a, b, M[7], 14, SV[30])
        b = GG(b, c, d, a, M[12], 20, SV[31])

        a = HH(a, b, c, d, M[5], 4, SV[32])
        d = HH(d, a, b, c, M[8], 11, SV[33])
        c = HH(c, d, a, b, M[11], 16, SV[34])
        b = HH(b, c, d, a, M[14], 23, SV[35])
        a = HH(a, b, c, d, M[1], 4, SV[36])
        d = HH(d, a, b, c, M[4], 11, SV[37])
        c = HH(c, d, a, b, M[7], 16, SV[38])
        b = HH(b, c, d, a, M[10], 23, SV[39])
        a = HH(a, b, c, d, M[13], 4, SV[40])
        d = HH(d, a, b, c, M[0], 11, SV[41])
        c = HH(c, d, a, b, M[3], 16, SV[42])
        b = HH(b, c, d, a, M[6], 23, SV[43])
        a = HH(a, b, c, d, M[9], 4, SV[44])
        d = HH(d, a, b, c, M[12], 11, SV[45])
        c = HH(c, d, a, b, M[15], 16, SV[46])
        b = HH(b, c, d, a, M[2], 23, SV[47])

        a = II(a, b, c, d, M[0], 6, SV[48])
        d = II(d, a, b, c, M[7], 10, SV[49])
        c = II(c, d, a, b, M[14], 15, SV[50])
        b = II(b, c, d, a, M[5], 21, SV[51])
        a = II(a, b, c, d, M[12], 6, SV[52])
        d = II(d, a, b, c, M[3], 10, SV[53])
        c = II(c, d, a, b, M[10], 15, SV[54])
        b = II(b, c, d, a, M[1], 21, SV[55])
        a = II(a, b, c, d, M[8], 6, SV[56])
        d = II(d, a, b, c, M[15], 10, SV[57])
        c = II(c, d, a, b, M[6], 15, SV[58])
        b = II(b, c, d, a, M[13], 21, SV[59])
        a = II(a, b, c, d, M[4], 6, SV[60])
        d = II(d, a, b, c, M[11], 10, SV[61])
        c = II(c, d, a, b, M[2], 15, SV[62])
        b = II(b, c, d, a, M[9], 21, SV[63])
        A = (A + a) % (2 ** 32)
        B = (B + b) % (2 ** 32)
        C = (C + c) % (2 ** 32)
        D = (D + d) % (2 ** 32)
    numbers = [A, B, C, D]
    result_array = endian(numbers)
    output_bytes = convert_int_array(result_array)
    end_s = to_hex_string(output_bytes)
    return end_s


def bytes_to_words(n):
    t = [0] * ((len(n) + 3) // 4)
    for r in range(len(n)):
        e = r * 8
        temp_t = n[r]
        if isinstance(temp_t, str):
            temp_t = 0
        t[e // 32] |= temp_t << (24 - e % 32)
    return t


byte_array1 = [65, 115, 105, 97, 47, 83, 104, 97, 110, 103, 104, 97, 105, 55, 48, 98, 99, 56, 102, 52, 98, 55, 50, 97, 56, 54, 57, 50, 49, 52, 54, 56, 98, 102, 56, 101, 56, 52, 52, 49, 100, 99, 101, 53, 49, 52, 56, 48, 48, 48, 95, 50, 95, 49, 95, 48, 95, 50, 95, 101, 120, 112, 108, 105, 99, 105, 116, 95, 115, 112, 101, 97, 107, 101, 114, 115, 50, 52, 49, 54]
byte_array = ['Latin', 'Arabic', 'Devanagari', 'Cyrillic', 'Bengali/Assamese', 'Gurmukhi', 'Javanese', 'Telugu', 'Tamil', 'Malayalam', 'Burmese', 'Thai', 'Kannada', 'Gujarati', 'Lao', 'Odia', 'Ge-ez', 'Sinhala', 'Armenian', 'Khmer', 'Greek', 'Lontara', 'Hebrew', 'Tibetan', 'Georgian', 'Modern Yi', 'Mongolian', 'Tifinagh', 'Syriac', 'Thaana', 'Inuktitut', 'Cherokee']
result = bytes_to_words(byte_array)
print(result)


if __name__ == "__main__":
    # input_data = ['Latin', 'Arabic', 'Devanagari', 'Cyrillic', 'Bengali/Assamese', 'Gurmukhi', 'Javanese', 'Telugu', 'Tamil', 'Malayalam', 'Burmese', 'Thai', 'Kannada', 'Gujarati', 'Lao', 'Odia', 'Ge-ez', 'Sinhala', 'Armenian', 'Khmer', 'Greek', 'Lontara', 'Hebrew', 'Tibetan', 'Georgian', 'Modern Yi', 'Mongolian', 'Tifinagh', 'Syriac', 'Thaana', 'Inuktitut', 'Cherokee']
    input_data = 'Asia/Shanghai70bc8f4b72a86921468bf8e8441dce5148000_2_1_0_2_explicit_speakers2416'
    if isinstance(input_data, list):
        msg_list = bytes_to_words(input_data)
        msg_list = convert_int_array(msg_list)
    else:
        msg_list = list(bytearray(input_data.encode()))
    print("result: ", md5sum(msg_list=msg_list))


