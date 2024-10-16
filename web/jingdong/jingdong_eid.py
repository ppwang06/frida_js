"""
eid
"""
import json
from urllib.parse import quote, unquote


def td_encrypt(encrypt_info):
    n = json.dumps(encrypt_info, separators=(",", ":"))
    n = quote(n).replace("%28", "(").replace("%27", "'").replace("%29", ")").replace("/", "%2F")
    start = 0
    end_str = ""
    base_code_table = "23IL<N01c7KvwZO56RSTAfghiFyzWJqVabGH4PQdopUrsCuX*xeBjkltDEmn89.-"
    while start < len(n):
        c = ord(n[start])
        start += 1
        _9c = False if start > len(n) - 1 else ord(n[start])
        start += 1
        _ba = False if start > len(n) - 1 else ord(n[start])
        start += 1

        aa = c >> 2
        bb = (c & 0x3) << 0x4 | _9c >> 0x4
        cc = (_9c & 0xf) << 0x2 | _ba >> 0x6
        dd = _ba & 0x3f
        if not _9c:
            cc = dd = 0x40
        elif not _ba:
            dd = 0x40
        new_a = base_code_table[aa] if aa < len(base_code_table) else ""
        new_b = base_code_table[bb] if bb < len(base_code_table) else ""
        new_c = base_code_table[cc] if cc < len(base_code_table) else ""
        new_d = base_code_table[dd] if dd < len(base_code_table) else ""
        end_str = end_str + new_a + new_b + new_c + new_d
    return end_str.strip() + "/"


def td_decrypt(encrypted_str):
    base_code_table = "23IL<N01c7KvwZO56RSTAfghiFyzWJqVabGH4PQdopUrsCuX*xeBjkltDEmn89.-"
    reverse_base_code_table = {char: index for index, char in enumerate(base_code_table)}
    if encrypted_str.endswith('/'):
        encrypted_str = encrypted_str[:-1]

    n = []
    for i in range(0, len(encrypted_str), 4):
        if i + 4 > len(encrypted_str):
            break
        aa = reverse_base_code_table[encrypted_str[i]]
        bb = reverse_base_code_table[encrypted_str[i + 1]]
        cc = reverse_base_code_table[encrypted_str[i + 2]]
        dd = reverse_base_code_table[encrypted_str[i + 3]]

        c = (aa << 2) | (bb >> 4)
        _9c = ((bb & 0xF) << 4) | (cc >> 2)
        _ba = ((cc & 0x3) << 6) | dd

        n.append(chr(c))
        if cc != 0x40:
            n.append(chr(_9c))
        if dd != 0x40:
            n.append(chr(_ba))

    decoded_str = ''.join(n)
    decoded_str = unquote(decoded_str).replace("%", "}")
    return decoded_str


if __name__ == '__main__':
    d = {
        "a": "b"
    }
    print(td_encrypt(d))
    new_t = "7TJI7TceW0Pu7Tce7TZ37Tce7Tce7T7L7TcezlP47Tce7TZ37Tce7Tce7T7L7TceiQPmSg6PwHcPwj<PwH7KRN3LvAJh6eAewGAe6eAewQFH7Tce7TZ37TceZNNLgf366j966HckS4CTZk3L6jpLfk7RgfZhg4ZIfNphTjk56ACIZ<ENT<DBRPJSSAPFAfbAgfFZT4RyZfb6TjZNTPfwgPZOfLRSTP3ZwBfLSfNvATitRBfZ7Tce7T7L7Tcezg94FSAewGAB6SAewdZjWQPHJIAewGAe6eAewd2PwHcPwj<PwH7B7Tce7T7L7TceFd2PwHcPwj<PwHc*ZL2DZlceiliBO0FHwBNQFQAlOLwjZ0iBF0NPig6xFIAewGAe6eAewQZjqh3P7Tce7TZ3wSAe6eAewdiPwHcPwj<PwHcxwIDxvH<uwIAewGAe6eAewd3l7Tce7TZ37TcewL7VW1RVgN4DfN8kwBcEOTaxZTwDZSAewGAe6eAewQiPwHcPwj<PwHcx7Tce7T7L7TceWeAewGAB6SAewQZbOgwlZH4xiBAkilRQZgN4OT6EigwxwTwBw06xwH7G7Tce7T7L7TcezeAewGAB6SAewQZbWd6uyQ6uil9C7T70ilNeJN9pzQRPqIAewGAe6eAewdNB7Tce7TZ37Tce7Tce7T7L7TceydZAyeAewGAB6SAewQp4FL2BZNNLgf366j966HckS4CTZk3L6jpLfk7RgfZhg4ZIfNphTjk56ACIZ<ENT<DBRPJSSAPFAfbAgfFZT4RyZfb6TjZNTPfwgPZOfLRSTP3ZwBfLSfNvATitRBfZ6AN36AkTAk70AHfK6AN36AN3R<RyR<p56f<jgN30TfNi7Tce7T7L7TceWg4PwHcPwj<PwHcPwHcPZj6/"
    print(td_decrypt(new_t))

