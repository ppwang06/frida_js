"""
8.0.0版本  token
如果 post 有data 需要参与加密逻辑
不过token 没校验
"""
import hashlib
import requests


headers = {
    "Host": "sh-gateway.shihuo.cn",
    "platform": "android",
    "timestamp": "1755674329309",
    "app-v": "8.0.0",
    "oaid": "{NjdjYmFmNWRmNWJkZWJhOQ}",
    "osv": "10",
    "network": "1",
    "luid": "dcff4a4d-60ee-46c0-bcf8-fdaed7bd56c4",
    "appid": "app",
    "user-agent": "Android 10 {WGlhb21p} CPU_ABI arm64-v8a CPU_ABI2  HARDWARE qcom MODEL {TUkgOA} network/NETWORK_WIFI shihuo/8.0.0 sc({holder},ali) minVersion(23836) sh-dv-sign[v1|b8b107023f8ee89f9fbcc1651e4da9380d2751f79b8da0aa]",
    "daga-ban-personal": "0"
}
url = "https://sh-gateway.shihuo.cn/v4/services/sh-applicationapi/pti"
params = {
    "minVersion": "23836",
    "clientCode": "{holder}",
    "v": "8.0.0",
    "channel": "ali",
    "device": "MI 8",
    "platform": "android",
    "timestamp": "1755674329309",
    "access_token": "2322TizdV3pjw8CBsy",
    "token": "8e66c66551c0118b5d8e46f27c790202"
}
base_info = {
    "minVersion": "23836",
    "clientCode": "{holder}",
    "v": "8.0.0",
    "channel": "ali",
    "device": "MI 8",
    "platform": "android",
    "timestamp": "1755674329309",
}
new_keys = sorted(base_info.keys())
end_str = ""
for one_key in new_keys:
    one_val = base_info.get(one_key)
    if one_val == "{holder}":
        one_val = "f055c204a8b60be1"
    end_str += f"{one_val}"
print(end_str)
md5_token = hashlib.md5(f"{end_str}123456".encode()).hexdigest()
print(md5_token)

# response = requests.get(url, headers=headers, params=params)
#
# print(response.text)
# print(response)