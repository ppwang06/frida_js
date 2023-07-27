"""
京东app 12.0.4 分析记录
根据前人的经验 在 jdbitmapkit   so文件中
wareBusiness
{"abTest800":true,"acceptPrivacy":true,"avoidLive":false,"bbtf":"","brand":"Redmi","bybt":"","cityCode":72,"cityId":0,"cpsNoTuan":null,"darkModelEnum":3,"districtId":0,"euaf":false,"eventId":"Babel_FlexCubePro","fromType":0,"isDesCbc":true,"isFromOpenApp":true,"latitude":"0.0","lego":true,"longitude":"0.0","model":"M2010J19SC","ocrFlag":false,"oneboxChannel":false,"oneboxKeyword":"","oneboxSource":"","overseas":0,"pdVersion":"1","personas":null,"pluginVersion":101050,"plusClickCount":0,"plusLandedFatigue":0,"productJdv":"0|appmarket|t_2018512525_appmarket|tuiguang|42111_0_xiaomi001_0_0|1686710773","provinceId":"0","prstate":"0","refreshMe":null,"searchWareflag":"","selfDelivery":"0","skuId":"100046282516","source_type":"babel_sale","source_value":"{\"fno\":\"0-0-21\",\"ford2\":\"-100\",\"bi\":\"1#2#167079bc556bd0583d9ec540fec1356b52c6d41a-100-710007#85282016\",\"mord\":\"-100\",\"ford1\":\"-100\",\"feedjud\":\"0\",\"mid\":\"94925698\",\"bi2\":\"2\",\"typ\":\"40952\",\"uibi\":\"-100\",\"bord\":\"0\",\"mci\":\"21033694-75732020--100046282516#1-0-1221--0--#1-0--NIR-#656-85282016#app\",\"exnum\":\"-100\",\"sgid\":\"21033694\",\"ftid2\":\"-100\",\"sord\":\"2\",\"ftid1\":\"-100\",\"sku\":\"100046282516\",\"bid\":\"0\",\"aid\":\"01093934\",\"fclabel\":\"-100\",\"feedtyp\":\"-100\"}","townId":0,"uAddrId":"0","utmMedium":null,"wareInnerSource":"extra.inner.source.init","yrqNew":"1"}
1f9eedbeeb19f7fe
android
12.0.4
结果:st=1686721954321&sign=998c4f43cf8fbbc9e2a7083ac13074fd&sv=120

100  112  121  一种分支算法
101  110  122  一种分支算法
102  111  120  一种分支算法
method_map = {
    "100": 0,
    "101": 1,
    "102": 2,
    "110": 1,
    "111": 2,
    "112": 0,
    "120": 2,
    "121": 0,
    "122": 1,
}
"""