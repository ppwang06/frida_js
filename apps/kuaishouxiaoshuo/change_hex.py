import json
data = {
    "sua": "Windows NT 10.0; Win64; x64",
}
# new_data = json.dumps(data, indent=2)
new_data = "abc"
b = new_data.encode('utf-8')
b_arr = [x if x < 128 else x - 256 for x in b]
print(b_arr)
print(len(b_arr))


def ascii_to_binary(a_list):
    bin_list = [format(char, '08b') for char in a_list]
    return bin_list


# 给定的 ASCII 码列表
ascii_list = [97, 98, 1]

# 转换为二进制字符串列表
binary_list = ascii_to_binary(ascii_list)
print(binary_list)





