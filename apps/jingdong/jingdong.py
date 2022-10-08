"""
getCommentListWithCard
{
    "category": "1318;12099;9756",
    "deepPageId": "79bef4fb77668cffc28aae2a48dce4c1",
    "isCurrentSku": true,
    "isFirstRequest": false,
    "num": "10",
    "offset": "1",
    "pictureCommentType": "A",
    "shadowMainSku": "0",
    "shieldCurrentComment": "1",
    "shopType": "0",
    "sku": "10045740493528",
    "sortType": 5,
    "tagId": "",
    "tagType": "",
    "type": "0"
}
1f9eedbeeb19f7fe
android
11.2.6
st=1664260905501&sign=8655c4666f04a54851390fb2cf7748c6&sv=121
st 和 sv 参与计算
"""
import json
from urllib.parse import urljoin, urlencode, quote, unquote
import base64
from hashlib import md5
body = {
    "category": "1318;12099;9756",
    "deepPageId": "79bef4fb77668cffc28aae2a48dce4c1",
    "isCurrentSku": True,
    "isFirstRequest": False,
    "num": "10",
    "offset": "1",
    "pictureCommentType": "A",
    "shadowMainSku": "0",
    "shieldCurrentComment": "1",
    "shopType": "0",
    "sku": "10045740493528",
    "sortType": 5,
    "tagId": "",
    "tagType": "",
    "type": "0"
}
d = {
    "functionId": "getCommentListWithCard",
    "body": json.dumps(body, separators=(',', ':')),
    "uuid": "1f9eedbeeb19f7fe",
    "client": "android",
    "clientVersion": "11.2.6",
    "st": "1664260905501",
    "sv": "121",
}
new_d = unquote(urlencode(d))
print(new_d)

md_val = md5(base64.b64encode(new_d.encode())).hexdigest()
print(md_val)
