package main

import (
	"encoding/base64"
	"fmt"
)

func getCipherUUID(uuid string) string {
	base64List := "KLMNOPQRSTABCDEFGHIJUVWXYZabcdopqrstuvwxefghijklmnyz0123456789+/"

	return base64.NewEncoding(base64List).EncodeToString([]byte(uuid))
}

func main() {
	//原始结果 oyTrZQHyHwvidQVyStesCISiSwPydQvtbQVPc3DroIS6StOsBMTsdXTfZWHPoRLCYWTvbMS6SxHzYWT0ZXD0pQTrc2U2DRnuWO5iY21uoWSzZNLrHtr4J0HtoO4zoQvZWO5ipRHzYWT0ZXD0SsmsZQV2aWDvaWHUYWviStesDtGsBMTvoRLlc2VuG291bxGsEsSnDzSsBMTwcw9kdOV4cQvucyS6SuZpbxVibP8mSsmsaW1rZ2VzaXfvStf7SwdyaWHTbWcsEsS1CzP4DJCnSsmsbQvzdOvjZyS6StC1ERqzDJqsBMTib25xIW1xStesDJCnoNcmEMT9BMTfbxDvcxHLcxHfY2nvStesCISiSwvkc2VydPDtZW5vStesCISiSwvkc2VydQVuG291bxGsEsS1SsmsaXDNb3TyZWD0StesCISiSwfudsS6StL8YXLmbWPya2V0pRHpCtKnENUnCtUyDV9rcRLjYXThZXH8dRVfZ3Vrbwd8DNSnCJPpCP94aWPlbWumCNPpCP8mpNO2ENS0CNU4CtusBMThZXv3b3TuStes5fof5fWZ5ZMl5fw6SsmsbwV3JWvuZQnvVQPxStesCISiSw5vd1ZvcxDfb24sEsSzSsmsb25vGw94JW9uStesCISiSw9yaWdkYWnJZWPyY2qsEsSnSsmsb3TfZ25rbPDvbQVtdMS6StOsBMTmYWdvStesCJUsBMTmYWdvHW50cwPkY2UsEsSnSsmscQPxZXDfowUsEsSnCMSiSxLlcRViYXHfb25UoXLvStesCtKnSsmscRZfZMS6SwGnYwPtZtK1DWZwCtG0YwZrCtVsZwUyCtduCWHwZQG3Ssmsc2VrcwDeVwVyc2vlbuDlZQUsEsS5ENCmSsmsc2Vtb25uIW5zZWHNb3VkdMS6StKsBMTzaQ93U2rlcPHrYsS6SxvvcySiSxDeb3dJdQ9yZVHrYsS6StOsBMTzb3VyY2VIZWYsEvj7SwV2ZW50IWGsEsTJdQPydRVmX09mZW5LcRLGYXTrbV9JdQP0dXCsBMTfc0HfcwVtdPDvYXTtaMS6StOsBMTmYWdvIWGsEsTTbwnfbwVXZWTWaWV3X0q1UPYsBMTmduvuStesSx1dBMTzdQ9tayS6StOsBMT2ZXSsEsSnCJqspG==
	//自己加密 oyTrZQHyHwvidQVyStesCISiSwPydQvtbQVPc3DroIS6StOsBMTsdXTfZWHPoRLCYWTvbMS6SxHzYWT0ZXD0pQTrc2U2DRnuWO5iY21uoWSzZNLrHtr4J0HtoO4zoQvZWO5ipRHzYWT0ZXD0SsmsZQV2aWDvaWHUYWviStesDtGsBMTvoRLlc2VuG291bxGsEsSnDzSsBMTwcw9kdOV4cQvucyS6SuZpbxVibP8mSsmsaW1rZ2VzaXfvStf7SwdyaWHTbWcsEsS1CzP4DJCnSsmsbQvzdOvjZyS6StC1ERqzDJqsBMTib25xIW1xStesDJCnoNcmEMT9BMTfbxDvcxHLcxHfY2nvStesCISiSwvkc2VydPDtZW5vStesCISiSwvkc2VydQVuG291bxGsEsS1SsmsaXDNb3TyZWD0StesCISiSwfudsS6StL8YXLmbWPya2V0pRHpCtKnENUnCtUyDV9rcRLjYXThZXH8dRVfZ3Vrbwd8DNSnCJPpCP94aWPlbWumCNPpCP8mpNO2ENS0CNU4CtusBMThZXv3b3TuStes5fof5fWZ5ZMl5fw6SsmsbwV3JWvuZQnvVQPxStesCISiSw5vd1ZvcxDfb24sEsSzSsmsb25vGw94JW9uStesCISiSw9yaWdkYWnJZWPyY2qsEsSnSsmsb3TfZ25rbPDvbQVtdMS6StOsBMTmYWdvStesCJUsBMTmYWdvHW50cwPkY2UsEsSnSsmscQPxZXDfowUsEsSnCMSiSxLlcRViYXHfb25UoXLvStesCtKnSsmscRZfZMS6SwGnYwPtZtK1DWZwCtG0YwZrCtVsZwUyCtduCWHwZQG3Ssmsc2VrcwDeVwVyc2vlbuDlZQUsEsS5ENCmSsmsc2Vtb25uIW5zZWHNb3VkdMS6StKsBMTzaQ93U2rlcPHrYsS6SxvvcySiSxDeb3dJdQ9yZVHrYsS6StOsBMTzb3VyY2VIZWYsEvj7SwV2ZW50IWGsEsTJdQPydRVmX09mZW5LcRLGYXTrbV9JdQP0dXCsBMTfc0HfcwVtdPDvYXTtaMS6StOsBMTmYWdvIWGsEsTTbwnfbwVXZWTWaWV3X0q1UPYsBMTmduvuStesSx1dBMTzdQ9tayS6StOsBMT2ZXSsEsSnCJqspG==
	uuid := "{\"addrFilter\":\"1\",\"articleEssay\":\"1\",\"buriedExpLabel\":\"tsabtest|base64|dXNlcmdyb3d0aF8xODcxN3xiYXNl|tsabtest\",\"deviceidTail\":\"64\",\"exposedCount\":\"172\",\"frontExpids\":\"F_null_0\",\"imagesize\":{\"gridImg\":\"531x531\",\"listImg\":\"358x358\",\"longImg\":\"531x708\"},\"insertArticle\":\"1\",\"insertScene\":\"1\",\"insertedCount\":\"5\",\"isCorrect\":\"1\",\"jdv\":\"0|appmarket|t_2018512525_appmarket|tuiguang|42111_0_xiaomi001_0_0|1682405829\",\"keyword\":\"早教启智\",\"newMiddleTag\":\"1\",\"newVersion\":\"3\",\"oneBoxMod\":\"1\",\"orignalSearch\":\"1\",\"orignalSelect\":\"1\",\"page\":\"15\",\"pageEntrance\":\"1\",\"pagesize\":\"10\",\"populationType\":\"201\",\"pvid\":\"d1bacf055ff244bfa25bfe227d1dfdd7\",\"searchVersionCode\":\"9830\",\"secondInsedCount\":\"0\",\"showShopTab\":\"yes\",\"showStoreTab\":\"1\",\"sourceRef\":[{\"eventId\":\"Startup_OpenAppParam_Status\",\"isDirectSearch\":\"1\",\"pageId\":\"InlineWebView_H5PV\",\"pvId\":\"\"}],\"stock\":\"1\",\"ver\":\"118\"}"
	res := getCipherUUID(uuid)
	fmt.Println(res)
}
