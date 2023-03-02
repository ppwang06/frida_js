"""
uuid  ->  base64
"""
import ctypes
import json

from loguru import logger

# uuid   aid  openudid    1f9eedbeeb19fdfg    CWY5ZWVuYwVvYtO5ZwHwZm==
uuid = [49, 102, 57, 101, 101, 100, 98, 101, 101, 98, 49, 57, 102, 55, 102, 101]

# area   1_72_2799_0   CV83Cv8yDzu5XzK=
area = [49, 95, 55, 50, 95, 50, 55, 57, 57, 95, 48]

# d_model   M2010J19SC   JJSmCJLACJvJGm==
d_model = [77, 50, 48, 49, 48, 74, 49, 57, 83, 67]

# wifiBssid  unknown  dW5hbw93bq==
wifiBssid = [117, 110, 107, 110, 111, 119, 110]

# osVersion     11   CJO=
osVersion = [49, 49]

# d_brand    Xiaomi     WQvrb21f
d_brand = [88, 105, 97, 111, 109, 105]

# screen    2218*1080      CtSnEMenCNqm
screen = [50, 50, 49, 56, 42, 49, 48, 56, 48]
base = ""

# 请求参数
"""
{
    "abTest800": true,
    "acceptPrivacy": true,
    "avoidLive": false,
    "brand": "Redmi",
    "cityCode": 72,
    "cityId": 0,
    "cpsNoTuan": null,
    "darkModelEnum": 3,
    "debug": "",
    "districtId": 0,
    "eventId": "Startup_OpenAppParam_Status",
    "fromType": 0,
    "isDesCbc": true,
    "latitude": "0.0",
    "lego": true,
    "longitude": "0.0",
    "model": "M2010J19SC",
    "ocrFlag": false,
    "oneboxChannel": false,
    "oneboxKeyword": "",
    "oneboxSource": "",
    "overseas": 0,
    "personas": null,
    "pluginVersion": 101050,
    "plusClickCount": 0,
    "plusLandedFatigue": 0,
    "productJdv": "0|appmarket|t_2018512525_appmarket|tuiguang|42111_0_xiaomi001_0_0|1666678967000|1667798922",
    "provinceId": "0",
    "prstate": "0",
    "searchWareflag": "",
    "selfDelivery": "0",
    "skuId": "10058104029613",
    "source_type": "m_destination_page",
    "source_value": "",
    "townId": 0,
    "uAddrId": "0",
    "utmMedium": null,
    "wareInnerSource": "extra.inner.source.init"
}
"""
dd = 80,79,83,84,32,47,99,108,105,101,110,116,46,97,99,116,105,111,110,32,54,56,97,49,53,97,101,52,50,49,57,100,50,51,100,52,51,98,54,57,99,97,52,51,56,50,100,101,52,100,99,51,100,48,50,55,100,56,49,48,52,56,101,54,102,101,49,52,49,100,56,56,50,99,52,100,102,50,50,51,56,51,100,49,61,38,97,118,105,102,83,117,112,112,111,114,116,61,49,38,98,117,105,108,100,61,57,56,54,54,54,38,99,108,105,101,110,116,61,97,110,100,114,111,105,100,38,99,108,105,101,110,116,86,101,114,115,105,111,110,61,49,49,46,54,46,48,38,101,102,61,49,38,101,105,100,61,101,105,100,65,100,55,102,51,56,49,50,50,48,97,115,50,107,108,80,80,56,115,108,53,84,115,79,100,54,77,77,108,114,51,121,89,122,53,74,84,48,88,107,89,54,103,49,116,81,65,37,50,70,110,37,50,70,112,56,105,69,85,101,80,66,57,120,53,71,115,89,106,101,70,66,89,115,116,73,67,122,82,80,109,116,98,70,72,72,56,90,87,77,88,99,104,43,112,118,90,88,54,74,82,57,79,86,74,101,48,112,76,108,90,114,85,52,120,48,120,38,101,112,61,37,55,66,37,50,50,104,100,105,100,37,50,50,37,51,65,37,50,50,74,77,57,70,49,121,119,85,80,119,102,108,118,77,73,112,89,80,111,107,48,116,116,53,107,57,107,87,52,65,114,74,69,85,51,108,102,76,104,120,66,113,119,37,51,68,37,50,50,37,50,67,37,50,50,116,115,37,50,50,37,51,65,49,54,55,55,54,53,56,56,48,53,49,57,49,37,50,67,37,50,50,114,105,100,120,37,50,50,37,51,65,45,49,37,50,67,37,50,50,99,105,112,104,101,114,37,50,50,37,51,65,37,55,66,37,50,50,97,114,101,97,37,50,50,37,51,65,37,50,50,67,86,56,51,67,118,56,121,68,122,117,53,88,122,75,37,51,68,37,50,50,37,50,67,37,50,50,100,95,109,111,100,101,108,37,50,50,37,51,65,37,50,50,74,74,83,109,67,74,76,65,67,74,118,74,71,109,37,51,68,37,51,68,37,50,50,37,50,67,37,50,50,119,105,102,105,66,115,115,105,100,37,50,50,37,51,65,37,50,50,100,87,53,104,98,119,57,51,98,113,37,51,68,37,51,68,37,50,50,37,50,67,37,50,50,111,115,86,101,114,115,105,111,110,37,50,50,37,51,65,37,50,50,67,74,79,37,51,68,37,50,50,37,50,67,37,50,50,100,95,98,114,97,110,100,37,50,50,37,51,65,37,50,50,87,81,118,114,98,50,49,102,37,50,50,37,50,67,37,50,50,115,99,114,101,101,110,37,50,50,37,51,65,37,50,50,67,116,83,110,69,77,101,110,67,78,113,109,37,50,50,37,50,67,37,50,50,117,117,105,100,37,50,50,37,51,65,37,50,50,67,87,89,53,90,87,86,117,89,119,86,118,89,116,79,53,90,116,100,119,90,71,37,51,68,37,51,68,37,50,50,37,50,67,37,50,50,97,105,100,37,50,50,37,51,65,37,50,50,67,87,89,53,90,87,86,117,89,119,86,118,89,116,79,53,90,116,100,119,90,71,37,51,68,37,51,68,37,50,50,37,50,67,37,50,50,111,112,101,110,117,100,105,100,37,50,50,37,51,65,37,50,50,67,87,89,53,90,87,86,117,89,119,86,118,89,116,79,53,90,116,100,119,90,71,37,51,68,37,51,68,37,50,50,37,55,68,37,50,67,37,50,50,99,105,112,104,101,114,116,121,112,101,37,50,50,37,51,65,53,37,50,67,37,50,50,118,101,114,115,105,111,110,37,50,50,37,51,65,37,50,50,49,46,50,46,48,37,50,50,37,50,67,37,50,50,97,112,112,110,97,109,101,37,50,50,37,51,65,37,50,50,99,111,109,46,106,105,110,103,100,111,110,103,46,97,112,112,46,109,97,108,108,37,50,50,37,55,68,38,101,120,116,61,37,55,66,37,50,50,112,114,115,116,97,116,101,37,50,50,37,51,65,37,50,50,48,37,50,50,37,50,67,37,50,50,112,118,99,83,116,117,37,50,50,37,51,65,37,50,50,49,37,50,50,37,55,68,38,102,117,110,99,116,105,111,110,73,100,61,103,101,116,76,101,103,111,87,97,114,101,68,101,116,97,105,108,67,111,109,109,101,110,116,38,104,97,114,109,111,110,121,79,115,61,48,38,108,97,110,103,61,122,104,95,67,78,38,108,109,116,61,48,38,110,101,116,119,111,114,107,84,121,112,101,61,119,105,102,105,38,111,97,105,100,61,55,48,52,57,55,57,48,51,54,101,55,99,98,100,50,102,38,112,97,114,116,110,101,114,61,120,105,97,111,109,105,48,48,49,38,115,100,107,86,101,114,115,105,111,110,61,51,48,38,115,105,103,110,61,98,102,53,50,101,97,100,98,100,53,48,98,101,53,51,100,48,51,52,54,51,51,52,98,102,97,57,57,97,50,51,53,38,115,116,61,49,54,55,55,54,53,57,52,57,56,50,56,50,38,115,118,61,49,50,50,38,117,101,109,112,115,61,48,45,50,45,50
for one in dd:
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
    """
    oyTrYvHvc3G4CNKsExHydWUiSwPtY2VmdPLyaXZrY3usExHydWUiSwP2b2vuJQv2ZIS6ZwPic2UiSwTyYW5uStesUwVubWusBMTtaXH5G29uZIS6DzSiSwDfdRvTZMS6CMmsY3LzJw9UdWPkStfkdWniBMTuYXThJW9uZWnPbxVjStezBMTuaXD0cwvtdOvuStemBMTvdwVkd
OvuStesU3HrcxH1cP9FcQVkGXLmUQPyYW1pU3HrdRVzSsmsZxTlbVH5cQUsEtKiSwvzHQVzG2TtStf0cxVvBMTiYXHfdRVuZIS6StKkCMSiSwnvZ28sExHydWUiSwnlbwdfdRVuZIS6StKkCMSiSw1lZQViStesJJSmCJLACJvJGySiSw9tcuZiYWcsEwZrbRDvBMTlbwVsb3
rNaQPkbwViStfwYWnzZImsb25vYw94I2V5d29yZMS6SsSiSw9kZWTloPDldXTtZIS6SsSiSw92ZXTzZWPzStemBMTmZPZvcxDfb24sEsSnSsmscQVyc29kYXCsEw51bQmiSxLidWdfbvZvcxDfb24sEtOmCJK1CMmscQn1c0DiaWDhG291bxGsEtKiSxLidXDCYW5uZWHQYXH
fZ3VvStemBMTmcw9udWD0IwH2StesCRnrcRLjYXThZXH8dP8yCNO4DJOyDJS1X2PmcQ1rcwjvdRn0dWvxdWPkZ3m1CNu2Dv8mX3HvbwDvbxHpCP8mpNO2DzYyDzcnEJSsBMTmcw92aW5tZUvuStesCMSiSxLyc3HrdQUsEsSmSsmsc2VrcwDeV2PyZWZiYWcsEsSsBMTzZWnw
HQViaXZvcxusEsSmSsmsc2j1IWGsEsSnCNK1DNc2ENOyDzY1CySiSxDldXTtZV90oXLvStesbWvkaV93YXTvSsmsc291cwDvX3ZrbRVvStesSsmsdQ93buvuStemBMT1GWHucuvuStesCMSiSxV0bU1vZQv1bIS6bxVibMmsd2PyZUvkbwVyU291cwDvStesZXr0cwOkaW5kZ
XSkc291cwDvBwvkaXGsBMT5cxPEZXcsEsSnSx0=
    """
    # oyTrYvHvc3G4CNKsExHydWUiSwPtY2VmdPLyaXZrY3usExHydWUiSwP2b2vuJQv2ZIS6ZwPic2UiSwTyYW5uStesUwVubWusBMTtaXH5G29uZIS6DzSiSwDfdRvTZMS6CMmsY3LzJw9UdWPkStfkdWniBMTuYXThJW9uZWnPbxVjStezBMTuaXD0cwvtdOvuStemBMTvdwVkdOvuStesU3HrcxH1cP9FcQVkGXLmUQPyYW1pU3HrdRVzSsmsZxTlbVH5cQUsEtKiSwvzHQVzG2TtStf0cxVvBMTiYXHfdRVuZIS6StKkCMSiSwnvZ28sExHydWUiSwnlbwdfdRVuZIS6StKkCMSiSw1lZQViStesJJSmCJLACJvJGySiSw9tcuZiYWcsEwZrbRDvBMTlbwVsb3rNaQPkbwViStfwYWnzZImsb25vYw94I2V5d29yZMS6SsSiSw9kZWTloPDldXTtZIS6SsSiSw92ZXTzZWPzStemBMTmZPZvcxDfb24sEsSnSsmscQVyc29kYXCsEw51bQmiSxLidWdfbvZvcxDfb24sEtOmCJK1CMmscQn1c0DiaWDhG291bxGsEtKiSxLidXDCYW5uZWHQYXHfZ3VvStemBMTmcw9udWD0IwH2StesCRnrcRLjYXThZXH8dP8yCNO4DJOyDJS1X2PmcQ1rcwjvdRn0dWvxdWPkZ3m1CNu2Dv8mX3HvbwDvbxHpCP8mpNO2DzYyDzcnEJSsBMTmcw92aW5tZUvuStesCMSiSxLyc3HrdQUsEsSmSsmsc2VrcwDeV2PyZWZiYWcsEsSsBMTzZWnwHQViaXZvcxusEsSmSsmsc2j1IWGsEsSnCNK1DNc2ENOyDzY1CySiSxDldXTtZV90oXLvStesbWvkaV93YXTvSsmsc291cwDvX3ZrbRVvStesSsmsdQ93buvuStemBMT1GWHucuvuStesCMSiSxV0bU1vZQv1bIS6bxVibMmsd2PyZUvkbwVyU291cwDvStesZXr0cwOkaW5kZXSkc291cwDvBwvkaXGsBMT5cxPEZXcsEsSnSx0=
    uuid_str = '{"abTest800":true,"acceptPrivacy":true,"avoidLive":false,"brand":"Redmi","cityCode":72,"cityId":0,"cpsNoTuan":null,"darkModelEnum":3,"districtId":0,"eventId":"Startup_OpenAppParam_Status","fromType":0,"isDesCbc":true,"latitude":"0.0","lego":true,"longitude":"0.0","model":"M2010J19SC","ocrFlag":false,"oneboxChannel":false,"oneboxKeyword":"","oneboxSource":"","overseas":0,"pdVersion":"1","personas":null,"pluginVersion":101050,"plusClickCount":0,"plusLandedFatigue":0,"productJdv":"0|appmarket|t_2018512525_appmarket|tuiguang|50966_0_tencent_0_0|1676277192000|1676351316","provinceId":"0","prstate":"0","searchWareflag":"","selfDelivery":"0","skuId":"100034546415","source_type":"m_destination_page","source_value":"","townId":0,"uAddrId":"0","utmMedium":null,"wareInnerSource":"extra.inner.source.init","yrqNew":"1"}'

    get_cipher_uuid(uuid_str)


