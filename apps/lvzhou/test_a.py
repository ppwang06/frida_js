"""
accessrefresh_code=4j6t1n5q&accessrefresh_count=2&aid=01A8gF8KfWuLqHRAknSMihZZ_FnhQNuSnFghVQEYKwu9YqjM0.&cfrom=28C8395010&channel_id=18&count=10&cuid=8229301430&cursor=-1&fill_comments_and_wow=false&indi_recommend=true&latitude=&longitude=&network_type=WIFI&noncestr=s30qQwksy7875995mD51481oGwz570&platform=ANDROID&refresh_desire=1&timestamp=1762750767986&ua=Xiaomi-MI8__oasis__4.6.0__Android__Android10&version=4.6.0&vid=2014286592168&wm=5311_90005


"""
import requests


headers = {
    "Host": "oasis.weibo.cn",
    "spr": "from:28C8395010;wm:5311_90005;luicode:;uicode:30000377;fid:231842_0009;lfid:;aid:01A8gF8KfWuLqHRAknSMihZZ_FnhQNuSnFghVQEYKwu9YqjM0.;oriuicode:;orifid:;networktype:WIFI",
    "gsid": "DfXsYY/+9W+P2/y2MubYnI3CZ+ZxjfNUt89q9aHPduSGYAU8LYM2dmXI/1ttdhmLwCpU9m10xhhYB4TQJs3TZ66VRsn4/vyShHFohH+bKoVnbGP9O+2NG1806l0dCxFJ",
    "authorization": "Bearer",
    "trace": "",
    "x-log-uid": "8229301430",
    "x-sessionid": "5490b6ab-07f1-4370-a9d6-f84c82f369c3",
    "aid": "01A8gF8KfWuLqHRAknSMihZZ_FnhQNuSnFghVQEYKwu9YqjM0.",
    "user-agent": "Xiaomi-MI8__oasis__4.6.0__Android__Android10"
}
url = "https://oasis.weibo.cn/v1/timeline/discovery"
params = {
    "channel_id": "18",
    "refresh_desire": "1",
    "accessrefresh_count": "2",
    "latitude": "",
    "cursor": "-1",
    "accessrefresh_code": "4j6t1n5q",
    "network_type": "WIFI",
    "ua": "Xiaomi-MI8__oasis__4.6.0__Android__Android10",
    "wm": "5311_90005",
    "aid": "01A8gF8KfWuLqHRAknSMihZZ_FnhQNuSnFghVQEYKwu9YqjM0.",
    "vid": "2014286592168",
    "cuid": "8229301430",
    "sign": "ae58633441e4a5ac4f434962777a5d0c",
    "timestamp": "1762750767986",
    "cfrom": "28C8395010",
    "count": "10",
    "longitude": "",
    "version": "4.6.0",
    "indi_recommend": "true",
    "fill_comments_and_wow": "false",
    "noncestr": "s30qQwksy7875995mD51481oGwz570",
    "platform": "ANDROID"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)