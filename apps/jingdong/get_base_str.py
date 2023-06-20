"""
uuid  ->  base64
京东算法加密
"""
import base64
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
    b = uuid.encode('utf-8')
    b_arr = [x if x < 128 else x - 256 for x in b]
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
    return end_str


# 等价于 get_cipher_uuid
def get_cipher_uuid_new(uuid_str: str):
    raw_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    new_table = 'KLMNOPQRSTABCDEFGHIJUVWXYZabcdopqrstuvwxefghijklmnyz0123456789+/'
    dictionary_decode = str.maketrans(new_table, raw_table)  # 创建字符映射关系 用于base64decode
    dictionary_encode = dict(zip(dictionary_decode.values(), dictionary_decode.keys()))  # 创建一个与上面反向的映射关系用于base64encode

    result_b64 = base64.b64encode(uuid_str.encode()).decode()  # MTIzMTIzMTIz base64encode(v) 正常的123123进行base64以后的值
    new_result_b64 = result_b64.translate(dictionary_encode)  # EP8hEP8hEP8h base64encode(v,table) 换表以后base64以后的值
    # new_data = new_result_b64.translate(dictionary_decode)  # MTIzMTIzMTIz base64encode(v) 变回正常的值
    return new_result_b64


if __name__ == '__main__':
    # uuid_str = '{"abTest800":true,"acceptPrivacy":true,"avoidLive":false,"brand":"Redmi","cityCode":72,"cityId":0,"cpsNoTuan":null,"darkModelEnum":3,"districtId":0,"eventId":"Startup_OpenAppParam_Status","fromType":0,"isDesCbc":true,"latitude":"0.0","lego":true,"longitude":"0.0","model":"M2010J19SC","ocrFlag":false,"oneboxChannel":false,"oneboxKeyword":"","oneboxSource":"","overseas":0,"pdVersion":"1","personas":null,"pluginVersion":101050,"plusClickCount":0,"plusLandedFatigue":0,"productJdv":"0|direct|-|none|-|1677724626440|1677827410","provinceId":"0","prstate":"0","searchWareflag":"","selfDelivery":"0","skuId":"10062884946355","source_type":"m_destination_page","source_value":"","townId":0,"uAddrId":"0","utmMedium":null,"wareInnerSource":"extra.inner.source.init","yrqNew":"1"}'
    # # oyTrZQHyHwvidQVyStesCISiSwPydQvtbQVPc3DroIS6StOsBMTsdXTfZWHPoRLCYWTvbMS6SxHzYWT0ZXD0pQTrc2U2DRnuWO5iY21uoWSzZNLrHtr4J0HtoO4zoQvZWO5ipRHzYWT0ZXD0SsmsZQV2aWDvaWHUYWviStesEJusBMTvoRLlc2VuG291bxGsEsSmSsmsZxTlbxHPoRLfZRCsEsTQX251bQnpCMSiSwvjYWdvc2v6ZIS6oyTxcwvuIW1xStesDJCnoNUzCISiSwnfc3HTbWcsEsSzDJr4CzU4SsmsbQ9kZ0vjZyS6StUzCXq3CNqspImsaW5zZXT0GXT0aWDiZIS6StOsBMTfbxDvcxHJY2VkZIS6StOsBMTfbxDvcxHvZODldW50StesCMSiSwvzG29ycwVtdMS6StOsBMTgZRYsEsSmpQHfcwVtdRmjpQ5lbwV8BXmnDtqnDzO4Dtu4DNO4pNO2ENO3CJunDtcsBMThZXv3b3TuStes5fof5fWZ5ZMl5fw6SsmsbQ9tYWnEdW0sEsSmSsmsbwV3JWvuZQnvVQPxStesCISiSw5vd1ZvcxDfb24sEsSzSsmsb25vGw94JW9uStesCISiSw9yaWdkYWnJZWPyY2qsEsSnSsmsb3TfZ25rbPDvbQVtdMS6StOsBMTmYWdvStesCISiSxLrZ2VPbxHyYW5tZIS6StOsBMTmYWdvc2v6ZIS6StOmSsmscQ9mdWnrdQvlbvH5cQUsEsSyCJOsBMTmdwvuStesSsmsc2VrcwDeVwVyc2vlbuDlZQUsEsS5DzqmSsmsc2Vtb25uIW5zZWHNb3VkdMS6StKsBMTzaQ93U2rlcPHrYsS6SxvvcySiSxDeb3dJdQ9yZVHrYsS6StOsBMTzb3VyY2VIZWYsEvj7SwV2ZW50IWGsEsTJZWPyY2riaXD0X1DvYXTtaOTloMSiSxLrZ2VTZMS6SvDvYXTtaP9Gcw9udWD0JQvzdMSiSxL2IWGsEsSspIn7SwV2ZW50IWGsEsTJZWPyY2rpGXDzb2DfYXHfdwVXb3TuSsmsaXDOaXTvY3HJZWPyY2qsEsSmSsmscQPxZUvuStesU2VrcwDeX0PtdQv2aXH5SsmscRZTZMS6StY0ZtS1Ytu3D2DrDNHvCNvsDJOzYzVsEJdtCwHsZtdrSx1dBMTzdQ9tayS6StOsBMT2ZXSsEsSnCJqspG==
    # str3 = '{"addrFilter":"1","articleEssay":"1","buriedExpLabel":"tsabtest|base64|dXNlcmdyb3d0aF8xODcxN3xiYXNl|tsabtest","deviceidTail":"99","exposedCount":"0","frontExpids":"F_null_0","imagesize":{"gridImg":"531x531","listImg":"358x358","longImg":"531x708"},"insertArticle":"1","insertScene":"1","insertedCount":"0","isCorrect":"1","jdv":"0|direct|-|none|-|1681718698418|1681719167","keyword":"早教启智","localNum":"0","newMiddleTag":"1","newVersion":"3","oneBoxMod":"1","orignalSearch":"1","orignalSelect":"1","page":"1","pageEntrance":"1","pagesize":"10","populationType":"211","pvid":"","searchVersionCode":"9780","secondInsedCount":"0","showShopTab":"yes","showStoreTab":"1","sourceRef":[{"eventId":"Searchlist_SearchBox","pageId":"Search_ProductList","pvId":""},{"eventId":"Search_AssociativeWord","isDirectSearch":"0","pageId":"Search_Activity","pvId":"64f25b977ca44e09b513c5b97c2dbf7a"}],"stock":"1","ver":"118"}'
    # get_cipher_uuid(str3)
    # 使用方式
    body = {"addrFilter": "1", "articleEssay": "1", "buriedExpLabel": "tsabtest|base64|dXNlcmdyb3d0aF8xODcxN3xiYXNl|tsabtest", "deviceidTail": "64",
            "exposedCount": "172", "frontExpids": "F_null_0", "imagesize": {"gridImg": "531x531", "listImg": "358x358", "longImg": "531x708"},
            "insertArticle": "1", "insertScene": "1", "insertedCount": "5", "isCorrect": "1",
            "jdv": "0|appmarket|t_2018512525_appmarket|tuiguang|42111_0_xiaomi001_0_0|1682405829", "keyword": "早教启智", "newMiddleTag": "1",
            "newVersion": "3", "oneBoxMod": "1", "orignalSearch": "1", "orignalSelect": "1", "page": "15", "pageEntrance": "1", "pagesize": "10",
            "populationType": "201", "pvid": "d1bacf055ff244bfa25bfe227d1dfdd7", "searchVersionCode": "9830", "secondInsedCount": "0", "showShopTab": "yes",
            "showStoreTab": "1", "sourceRef": [{"eventId": "Startup_OpenAppParam_Status", "isDirectSearch": "1", "pageId": "InlineWebView_H5PV", "pvId": ""}],
            "stock": "1", "ver": "118"}
    new_body = json.dumps(body, separators=(',', ':'), ensure_ascii=False)
    end_body = get_cipher_uuid(new_body)
    test = 'oyTrZQHyHwvidQVyStesCISiSwPydQvtbQVPc3DroIS6StOsBMTsdXTfZWHPoRLCYWTvbMS6SxHzYWT0ZXD0pQTrc2U2DRnuWO5iY21uoWSzZNLrHtr4J0HtoO4zoQvZWO5ipRHzYWT0ZXD0SsmsZQV2aWDvaWHUYWviStesDtGsBMTvoRLlc2VuG291bxGsEsSnDzSsBMTwcw9kdOV4cQvucyS6SuZpbxVibP8mSsmsaW1rZ2VzaXfvStf7SwdyaWHTbWcsEsS1CzP4DJCnSsmsbQvzdOvjZyS6StC1ERqzDJqsBMTib25xIW1xStesDJCnoNcmEMT9BMTfbxDvcxHLcxHfY2nvStesCISiSwvkc2VydPDtZW5vStesCISiSwvkc2VydQVuG291bxGsEsS1SsmsaXDNb3TyZWD0StesCISiSwfudsS6StL8YXLmbWPya2V0pRHpCtKnENUnCtUyDV9rcRLjYXThZXH8dRVfZ3Vrbwd8DNSnCJPpCP94aWPlbWumCNPpCP8mpNO2ENS0CNU4CtusBMThZXv3b3TuStes5fof5fWZ5ZMl5fw6SsmsbwV3JWvuZQnvVQPxStesCISiSw5vd1ZvcxDfb24sEsSzSsmsb25vGw94JW9uStesCISiSw9yaWdkYWnJZWPyY2qsEsSnSsmsb3TfZ25rbPDvbQVtdMS6StOsBMTmYWdvStesCJUsBMTmYWdvHW50cwPkY2UsEsSnSsmscQPxZXDfowUsEsSnCMSiSxLlcRViYXHfb25UoXLvStesCtKnSsmscRZfZMS6SwGnYwPtZtK1DWZwCtG0YwZrCtVsZwUyCtduCWHwZQG3Ssmsc2VrcwDeVwVyc2vlbuDlZQUsEsS5ENCmSsmsc2Vtb25uIW5zZWHNb3VkdMS6StKsBMTzaQ93U2rlcPHrYsS6SxvvcySiSxDeb3dJdQ9yZVHrYsS6StOsBMTzb3VyY2VIZWYsEvj7SwV2ZW50IWGsEsTJdQPydRVmX09mZW5LcRLGYXTrbV9JdQP0dXCsBMTfc0HfcwVtdPDvYXTtaMS6StOsBMTmYWdvIWGsEsTTbwnfbwVXZWTWaWV3X0q1UPYsBMTmduvuStesSx1dBMTzdQ9tayS6StOsBMT2ZXSsEsSnCJqspG=='
    logger.info(end_body == test)
    #  新方法
    end_body_new = get_cipher_uuid_new(new_body)
    logger.info(f"新方法结果为:{end_body_new}")
    logger.info(end_body_new == test)



