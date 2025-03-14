"""
{
    "code": 0,
    "data": "012fgzPiyRQPqkH-bL6iR9qdnH-aCEzyV9IfyLxyPzBndwcgbl6YaWCEmO8r9P29FGYtMKUqBGQdQgJ7B6DxDf0opqj63yrkv1a5SXY2UvYUGrC9nMG4d72efKD_w5GobpZyt2X__JrEhzDA1P0WdCvAkVy-o1cLewHViQl634gfgP6kNYPM3Zs8p5OgsZm-oPM98nBXPtn3pxw0LABXxDfmehoNP3cTfgaovvnhiFNAPuqSKjgbnGqa7aIwE60M0PqzbVW_KAnVKRAOrYL0EiLKRg1IyjAOYKLRTXXE1h9VcTFFz7aa3s4-sHBCnKzQwseAKk8xWNhjB9WILM_23vcxeN0SmniZ3Z7sDdivl9H7M27bsJ9a1SV_oZvYbuVchD6L0QP248wks9jNsD5Iew6FXlEH4zdvCqAPEmO85astLhfbuIkZCoLu3wL42JCuaV67K-jQgC_WxcK2gd6qrpSC4goWuM5sJ5y4xw1qRJxoTvECfHLlWEjgVFqK0SLusgqg41SzGRYlZPSjivARJdo2_Uwl_oeeTwQ8pE8gx6RGlE2sMwP3F_1txU8gl2ynkyh_nd03a62Lc8xkVHcRfVYwrpjUX9dFxapa_WanE0RsS6gBxubtDL0ioiaE1O46ltagkvDcq2zr91KT1ESzYDeNWYojpenCuDQtjPbl1O8DxD2_5ZCUVKrYyQ9KMLyj_AzAass_RZlx0F1uDq7PX9SLfG4RqQWjGFcgSEf4cP2MBlM7LuIExNiM7DssrfyLk0LwaPCqv0H7_vmxMNrXlNq1emnl8RqLINQUGG6AmauYnfcLNAlBR5sFgNfL17Zm6cb8tcnWppz37uqjp2mJovSrVKM_rPA78S4mP9HWCNNA-Lsw_f2gjXEQyWsCia8D20y2Vy2CDIghV06n9B6wGSHopTbBP9gtxBdCHYf0icauQze7LbTFdvL6sv5jpv8zER8m6rsFjIHXMnX_5yyvbZLbgydeRs2f2hxIVx2vx9k1wmznVEO98qR3Lll8O8QmmLLKFa5X8nyj1x57PsXM2D_IRQTDYIN_4F7KbhSO-4Ncc22eYO1_7XbYJpxM6mL9Y52Fs-L_kFq-_CPLYBGkg2nh26sGd_rMwrfCAi13TO176jA2BBy80vSTjxggxXyWyPbmj8OQGYvcZozlX7Vg_a-EKH82eFW4PyhXTBxGhDA6WqRha_J3CQBHE_PUb4OTWWWKFLi1RqN2wSllP6cAQXWB7MSXoia1V-RbneubLHPp4JAwjdrkvsyQJX4fyq5hWjrx_fXOFLdatsKrX3Nk6au0g5Zc1rKv12HLll9UUU6o_ymCZb7rgHVIT6dk53oF2ytUCeZ48gi-lJOk2Qq8C8MRDqrC2J6htkyyX5XnyZdZn2DPV4n-8Rh7LBycAGt84_vfPLQ80iURoLzO2l_QuZlagp0vfoclzXXhSalEYMT__my6r2uT-SWewNOvqOD4t0eDOQ7uBdIjYR3byBthx7QUnIKgvXTZ-NTCPAIyb5xq0Ql5zKnTtPUHKMupsozg97_ugKdoGqJZrjXGO-G2e54UQfHTt6rY0-NMGCW67TasqnZDW2PpBRavNDWdCPq5",
    "message": "Success",
    "class": "com.jd.xh.dics.api.entity.ResponseDTO"
}
"""
import base64
from Crypto.Cipher import AES
import binascii


class EncryptDate:
    def __init__(self, key, iv):
        self.key = key.encode("utf-8")  # 初始化**
        self.length = AES.block_size  # 初始化数据块大小
        self.aes = AES.new(self.key, AES.MODE_CBC, iv=iv.encode())  # 初始化AES,ECB模式的实例
        # 截断函数，去除填充的字符
        self.unpad = lambda date: date[0:-ord(date[-1])]

    def pad(self, text):
        """
        #填充函数，使被加密数据的字节码长度是block_size的整数倍
        """
        count = len(text.encode('utf-8'))
        add = self.length - (count % self.length)
        entext = text + (chr(add) * add)
        return entext

    def encrypt_bin(self, encr_data):
        # 加密函数 输出hex
        res = self.aes.encrypt(self.pad(encr_data).encode("utf8"))
        return binascii.b2a_hex(res).decode()

    def encrypt_bs64(self, encr_data):
        # 加密函数 输出base64
        res = self.aes.encrypt(self.pad(encr_data).encode("utf8"))
        return str(base64.b64encode(res), encoding="utf8")

    def decrypt_bs64(self, decr_data):
        # 解密函数 base64
        res = base64.decodebytes(decr_data.encode("utf8"))
        msg = self.aes.decrypt(res).decode("utf8")
        return self.unpad(msg)

    def decrypt_bin(self, decr_data):
        # 解密函数 bin
        result = binascii.a2b_hex(decr_data)
        msg = self.aes.decrypt(result).decode().strip(b'\x00'.decode())
        return self.unpad(msg)


if __name__ == '__main__':
    # 这里**的长度必须是16的倍数
    key_str = "qy7YhmyCNcOAC3El9d3qGA=="
    iv_str = "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    eg = EncryptDate(key_str, iv_str)
    data = "012fgzPiyRQPqkH-bL6iR9qdnH-aCEzyV9IfyLxyPzBndwcgbl6YaWCEmO8r9P29FGYtMKUqBGQdQgJ7B6DxDf0opqj63yrkv1a5SXY2UvYUGrC9nMG4d72efKD_w5GobpZyt2X__JrEhzDA1P0WdCvAkVy-o1cLewHViQl634gfgP6kNYPM3Zs8p5OgsZm-oPM98nBXPtn3pxw0LABXxDfmehoNP3cTfgaovvnhiFNAPuqSKjgbnGqa7aIwE60M0PqzbVW_KAnVKRAOrYL0EiLKRg1IyjAOYKLRTXXE1h9VcTFFz7aa3s4-sHBCnKzQwseAKk8xWNhjB9WILM_23vcxeN0SmniZ3Z7sDdivl9H7M27bsJ9a1SV_oZvYbuVchD6L0QP248wks9jNsD5Iew6FXlEH4zdvCqAPEmO85astLhfbuIkZCoLu3wL42JCuaV67K-jQgC_WxcK2gd6qrpSC4goWuM5sJ5y4xw1qRJxoTvECfHLlWEjgVFqK0SLusgqg41SzGRYlZPSjivARJdo2_Uwl_oeeTwQ8pE8gx6RGlE2sMwP3F_1txU8gl2ynkyh_nd03a62Lc8xkVHcRfVYwrpjUX9dFxapa_WanE0RsS6gBxubtDL0ioiaE1O46ltagkvDcq2zr91KT1ESzYDeNWYojpenCuDQtjPbl1O8DxD2_5ZCUVKrYyQ9KMLyj_AzAass_RZlx0F1uDq7PX9SLfG4RqQWjGFcgSEf4cP2MBlM7LuIExNiM7DssrfyLk0LwaPCqv0H7_vmxMNrXlNq1emnl8RqLINQUGG6AmauYnfcLNAlBR5sFgNfL17Zm6cb8tcnWppz37uqjp2mJovSrVKM_rPA78S4mP9HWCNNA-Lsw_f2gjXEQyWsCia8D20y2Vy2CDIghV06n9B6wGSHopTbBP9gtxBdCHYf0icauQze7LbTFdvL6sv5jpv8zER8m6rsFjIHXMnX_5yyvbZLbgydeRs2f2hxIVx2vx9k1wmznVEO98qR3Lll8O8QmmLLKFa5X8nyj1x57PsXM2D_IRQTDYIN_4F7KbhSO-4Ncc22eYO1_7XbYJpxM6mL9Y52Fs-L_kFq-_CPLYBGkg2nh26sGd_rMwrfCAi13TO176jA2BBy80vSTjxggxXyWyPbmj8OQGYvcZozlX7Vg_a-EKH82eFW4PyhXTBxGhDA6WqRha_J3CQBHE_PUb4OTWWWKFLi1RqN2wSllP6cAQXWB7MSXoia1V-RbneubLHPp4JAwjdrkvsyQJX4fyq5hWjrx_fXOFLdatsKrX3Nk6au0g5Zc1rKv12HLll9UUU6o_ymCZb7rgHVIT6dk53oF2ytUCeZ48gi-lJOk2Qq8C8MRDqrC2J6htkyyX5XnyZdZn2DPV4n-8Rh7LBycAGt84_vfPLQ80iURoLzO2l_QuZlagp0vfoclzXXhSalEYMT__my6r2uT-SWewNOvqOD4t0eDOQ7uBdIjYR3byBthx7QUnIKgvXTZ-NTCPAIyb5xq0Ql5zKnTtPUHKMupsozg97_ugKdoGqJZrjXGO-G2e54UQfHTt6rY0-NMGCW67TasqnZDW2PpBRavNDWdCPq5"
    data = data.replace("-", "+").replace("_", "/")
    msg_bin = eg.decrypt_bs64(str(data))
    print(msg_bin)
    # eg2 = EncryptDate(key_str, iv_str)