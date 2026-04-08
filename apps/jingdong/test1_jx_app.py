"""
app 6.0.0
"""
from curl_cffi import requests


headers = {
    "Host": "api.m.jd.com",
    "x-rp-client": "h5_1.0.0",
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": "jdltapp;android;6.0.0;;;appBuild/22440;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1775096578824%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22CJK%3D%22%2C%22ad%22%3A%22DtYyYJq5CzuyYJrwYWOnEK%3D%3D%22%2C%22od%22%3A%22DtdtYwPwDWHwDWTuZWTrEG%3D%3D%22%2C%22ov%22%3A%22Ctu%3D%22%2C%22ud%22%3A%22DtYyYJq5CzuyYJrwYWOnEK%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jd.pingou%22%7D;jxtj/jx;Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36",
    "x-referer-page": "https://wqs.jd.com/item/view.html",
    "accept": "*/*",
    "origin": "https://wqs.jd.com",
    "x-requested-with": "com.jd.pingou",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://wqs.jd.com/item/view.html?sku=10063917177883&_fd=jx&has_native=0&sid=ccbd6f119fa23cfe30e5c497b1430a7w&un_area=1_72_55673_0",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}
cookies = {
    "wxa_level": "1",
    "cid": "4",
    "webp": "1",
    "visitkey": "6386825846734734582",
    "__jdv": "122270672%7Cdirect%7C-%7Cnone%7C-%7C1775036485456",
    "__jdc": "122270672",
    "jxsid_s_u": "https%3A//wqs.jd.com/item/view.html",
    "unpl": "",
    "__jda": "122270672.17750364854541940265618.1775036485.1775096580.1775096580.4",
    "__jdb": "122270672.1.17750364854541940265618|4.1775096580",
    "mba_sid": "13.15",
    "mba_muid": "17750364854541940265618.13.1775096595870"
}
url = "http://api.m.jd.com/api"
params = {
    "functionId": "jxdetail_ass_comment"
}
data = {
    "functionId": "jxdetail_ass_comment",
    "appid": "jx_h5",
    "t": "1775096601184",
    "channel": "jxapp",
    "clientVersion": "1.2.5",
    "client": "jxapp",
    "uuid": "6386825846734734582",
    "cthr": "1",
    "loginType": "2",
    "x-api-eid-token": "jdd03HRHAX3VZQDJILYGHKRLSWUUU7KFZFELD2KWGA67ZD7J7ROYXUPQHE5WZBW6CORWW7G4MFZZKQONNTES2MIH7RPWURQAAAAM5JQAEYMIAAAAADPIQMDYN2QLRTMX",
    "body": "{\"version\":\"v2\",\"sku\":\"10063917177883\",\"page\":2,\"pagesize\":10,\"sorttype\":5,\"skucomment\":0,\"score\":0,\"sceneval\":2,\"buid\":325,\"appCode\":\"msd1188198\",\"time\":1775096601184,\"signStr\":\"88a8f9df58554b5a6d56832a843494f5\"}",
    "h5st": "20260402102325204;ie55ejyjvj75e5y3;45fa7;tk03wa2d31bae18n3tApQDoLEkKiFztZL2IfeBqkok4z9AKRDkjNXHp7VJlaNFPNQNACfOAMKRFoIK771clYtsEL2mgV;010995372fe4b6cac51c19bc63da5cebcd3f897c4252a072f1f2827287e62c3f;5.3;1775096601204;of7ruCLj4HUeGW4eBSERyCVS2XYSCipjxjpPFipjLDrgzrJdJz1TIipjLDrgJX4eyjlfGS1T0jISFSYSGiof2LITyjofJiod2L4f6XoSJrJdJrEa-OFTGOEjLrJp-jJf3fFe6PYSGWIS6n1fHSVd5rYe5r4T4b1f7flf3f4TJipjxj5PKSEQKeFjLrJp-jpfJrJdJbYOJipjLDrgJjIg4zZe1uWS-GFSMWoRJrJdJTEjLrJp-j5f6eoO4W1QoOFjLDIj_ulS9mFPJrpjh7Jj-KIO_iUTLLUO9GlYJrJdJTlPJrpjh7ZMLrJp4rJdJnYf2iFjLrpjLDrg3nojxjpf6XETJrpjLrJp-LYgLDIj5nYOJipjLrpjh7JjKmYdiS1f7KIRWq4RJrJdJ31QHyVT5ipjLrpjh7pfLDIjzXETJrpjLrJp-rojxj5e2iFjLrpjLDrg1fojxjJe2iFjLrpjLDrg7rJdJXYOJipjLrpjh7pfLDIj3XETJrpjLrJp-j4fLDIj4XETJrpjLrJp-jZe9nIg7jpjxjZf2iFjLrpjLDrg7rJdJ-1OJrpjLrJp-nYgLDIj46FjLrpjLDrg7rJdJ7FjLrpjLDrg7rJdJb1OJrpjLrJpwqJdJbFQGakNGipjLDrguqpjhjZXdC0R7qGYJ21YAO2UHCFjLDIj6rEjLrpjLD7NLDIj7qEjLrJp-jJO0q5d5rof9LIfzrYd6zZfa_XX8blQCWEbLLoji2njwrYfLbVR8ikS9mnjwLUO9GlYJrJdJnVO4ipjLD7N;1a12cd7114edf8525d4dc03ec1fd4e64bbf25b61eb20bd6ef4fc08b7b57e1cb8;qbkgHGHQ8GlOIyVOF6JQ8G1P5WFW3yVSC61T-bEQGGlQI6ZNHuFT-bVR7qUT"
}
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)