## frida_js
使用过frida hook的js代码（自用）


###### apps
> 一些hook的app记录   

[apps](./apps/readme.md)

###### 脱壳    
[脱壳 frida_dump](https://github.com/lasting-yang/frida_dump)

######  yang神hook代码
[frida_hook_libart](https://github.com/lasting-yang/frida_hook_libart)   


###### 知识点
1. Java中 （byte） 类型的强转
```Java
    bArr[i2] = (byte) (255 & j2)
```

```python
# 实现java的类型强转 (byte) 2093322535     # -256 ~ 255  # -128 ~ 127
def int_to_byte(target_int: int) -> int:
    if -128 <= target_int <= 127:
        return target_int
    cc = bin(target_int)
    byte_cc = cc[-8:]
    if byte_cc.startswith('1') and target_int < 0:
        return -(int(byte_cc, 2) - 256)
    if byte_cc.startswith('1') and target_int > 0:
        return int(byte_cc, 2) - 256
    if byte_cc.startswith('0') and target_int > 0:
        return int(byte_cc, 2)
    return -(int(byte_cc, 2))
```

2. Python中 针对于 负数的十进制 转为二进制
```python
def int_to_bin(number, index, feature=True):
    """
    index为该数据位宽,number为待转换数据,
    feature为True则进行十进制转二进制，为False则进行二进制转十进制。
    """
    # 十进制转换为二进制
    if feature is True:
        if number >= 0:
            b = bin(number)
            b = '0' * (index+2 - len(b)) + b
        else:
            b = 2 ** index + number
            b = bin(b)
            # 注意这里算出来的结果是补码
            b = '1' * (index+2 - len(b)) + b
        b = b.replace("0b", "")
        b = b.replace("-", "")
        return b
    # 二进制转换为十进制
    elif feature is False:
        i = int(str(number), 2)
        # 如果是负数
        if i >= 2**(index-1):
            i -= (2**index-i)
            return i
        else:
            return i
```
3. 对一个数组的长度字节 []byte 转为base64
   [参考代码](./apps/kuaishouxiaoshuo/othre.py)
```python
c = [-86, 105, -105, 34, 1, -89, -111, 120, 56, 50, 57, 51, 99, 48, 99, 48, 49, 50, 48, 102, 56, 55, 99, 98, 101, 57, 99, 97, 99, 57, 99, 56, 53, 98, 102, 98, 50, 55, 50, 100, 101, 53, 99, 97, 57, 55, 98, 51, 100, 54, 100, 98, 100, 53, 99, 51]
d = ['10101010', '01101001', '10010111', '00100010', '00000001', '10100111', '10010001', '01111000', '00111000', '00110010', '00111001', '00110011', '01100011', '00110000', '01100011', '00110000', '00110001', '00110010', '00110000', '01100110', '00111000', '00110111', '01100011', '01100010', '01100101', '00111001', '01100011', '01100001', '01100011', '00111001', '01100011', '00111000', '00110101', '01100010', '01100110', '01100010', '00110010', '00110111', '00110010', '01100100', '01100101', '00110101', '01100011', '01100001', '00111001', '00110111', '01100010', '00110011', '01100100', '00110110', '01100100', '01100010', '01100100', '00110101', '01100011', '00110011']
end = "qmmXIgGnkXg4MjkzYzBjMDEyMGY4N2NiZTljYWM5Yzg1YmZiMjcyZGU1Y2E5N2IzZDZkYmQ1YzM="
```
4. python版生成Base64 (参照网上)   
     [Python  Base64代码](./apps/kuaishouxiaoshuo/other_base64.py)
5. Android的Base64源码    
    [Android Base64源码](./apps/common_utils/Base64.txt)     
6. Java中`str1.getBytes()` python实现
```python
cstr = "天下大吉"
b = cstr.encode('utf-8')
b_arr = [x if x < 128 else x - 256 for x in b]
print(b_arr)


bytes_list = [x + 256 if x < 0 else x for x in b_arr] # 转换为无符号字节值
b = bytes(bytes_list)
s = b.decode('utf-8')
print(s)
```






