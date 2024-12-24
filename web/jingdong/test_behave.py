"""
behavior_report
不确定是否为行为上报
"""
import json

base = {
    "kmC": [],
    "kmMD": [],
    "kmMM": [],
    "kmMMkd": [],
    "kmTS": [],
    "kmTM": [],
    "kmI": [],
    "kmMC": "",
    "kmMCF": "",
    "initTs": 1735030155203,
    "reTs": 1735030156226,
    "kmTEC": 0,
    "kmIEC": 0,
    "wc": 0,
    "wd": 0,
    "l": "zh-CN",
    "ls": "zh-CN",
    "ml": 2,
    "pl": 5,
    "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "pp": {},
    "extend": {
        "wd": 0,
        "l": 0,
        "ls": 5,
        "wk": 0,
        "bu2": 0,
        "bu3": 79,
        "bu4": 0,
        "bu5": 0,
        "bu6": 32,
        "bu7": "",
        "bu8": 0
    },
    "pp1": "",
    "bu1": "",
    "w": 1920,
    "h": 1080,
    "ow": 1920,
    "oh": 1040,
    "url": "https://item.jd.com/3742086.html",
    "og": "https://item.jd.com",
    "pf": "Win32",
    "pr": 1,
    "re": "https://cfe.m.jd.com/",
    "referer": "https://cfe.m.jd.com/",
    "bu2": "    at https://storage.360buyimg.com/webcontainer/main/js-security-v3-rac.js?v=20241224:5:16760",
    "canvas": "0fb7f119e21bb6b17b2b0d333a5617bf",
    "webglFp": "ff9f09985d234c7453f38289693c5baa",
    "ccn": 16,
    "lsc": 1,
    "ssc": 1,
    "csc": 1,
    "tz": "Asia/Shanghai",
    "pld": "PDF Viewer,Chrome PDF Viewer,Chromium PDF Viewer,Microsoft Edge PDF Viewer,WebKit built-in PDF",
    "eid": "54BASGCZANOW55GV6K77ARKHGUOFLZSWPELCA4MFEK4YD42KQL2RZWNXX4YCBX6LQ3PUWBUXOWLEGKE5UU7Z2BKSCU",
    "fp": "88d4844789bb21ed15c38ab0a7fea1dc",
    "jsToken": "jdd0354BASGCZANOW55GV6K77ARKHGUOFLZSWPELCA4MFEK4YD42KQL2RZWNXX4YCBX6LQ3PUWBUXOWLEGKE5UU7Z2BKSCUAAAAMT67NSP2AAAAAACDFRBYNA4AAJFUX"
}

dat = json.dumps(base, separators=(",", ":"))


def xor_encrypt_decrypt(input_string, key=5):
    return ''.join(chr(ord(char) ^ key) for char in input_string)


encrypted_string = xor_encrypt_decrypt(dat)
print(f"Encrypted string: {encrypted_string}")


g = "~'nhF'?^X)'nhHA'?^X)'nhHH'?^'ALS)4=443=)4214)461')'ALS)4=4420)4277)412')'ALS)4=44=6)4255)434')'GJA\)4=44<4)4333)42<')'GJA\)4=4754)4367)4<0')'GJA\)4=4740)400=)763')'ALS)4=4776)4073)703')'ALS)4=4767)41<7)727')'ALS)4=4712)4174)652')'ALS)4=4047)45<<)652')'ALS)4=4075)4471)7<=')'ALS)4=4060)4757)731')'ALS)4=4010)4703)71=')'ALS)4=4004)465=)77=')'ALS)4=4032)4170)4=<')'ALS)4=4020)41==)424')'ALS)4=40=3)401<)40=')'ALS)4=40<4)435<)463'X)'nhHHna'?^X)'nhQV'?^X)'nhQH'?^X)'nhL'?^X)'nhHF'?'fwphg(rwdu?0)ajf?43)vphhdw|(uwjhjqljk?7')'nhHFC'?'fwphg(rwdu?1)ajf?2)vphhdw|(uwjhjqljk?7)ajf?<)fwphg(rwdu?4')'lklqQv'?4260565400756)'w`Qv'?42605656=235<)'nhQ@F'?4=)'nhL@F'?0)'rf'?5)'ra'?5)'i'?'m(FK')'iv'?'m(FK')'hi'?7)'ui'?0)'pd'?'Hjliid*0+5%-Rlkajrv%KQ%45+5>%Rlk31>%}31,%Duui`R`gNlq*062+63%-NMQHI)%iln`%B`fnj,%Fmwjh`*464+5+5+5%Vdcdwl*062+63')'uu'?~x)'`}q`ka'?~'ra'?5)'i'?5)'iv'?0)'rn'?5)'gp7'?5)'gp6'?2=)'gp1'?5)'gp0'?5)'gp3'?67)'gp2'?'')'gp='?5x)'uu4'?'qjn`k857=61507=`fa2g1<c7f24cd65<=ga371)4)<36<50>%ZZoad84=4444<60+4260565400645450=<10<67+4260565400+4260565400+4260565400+4>%ZZoag84=4444<60+4+4260565400645450=<10<67y4+4260565400>%ZZoaf84=4444<60>%ZZoas84=4444<60yalw`fqy(ykjk`y(y4260565400646>%ovdslc84>%ovdslc84>%6DG<A76C2D1G6FVV8oaa5601GDVBF_DKJR00BS3N22DWNMBPJCI_VRU@IFD1HC@N1\A17NTI7W_RK]]1\FG]3IT6UPRGP]JRI@BN@0PP2_7GNVFPDDDDHQ32KVU7DDDDDDFACWG\KD1DDOCP]>%6DG<A76C2D1G6F<G801GDVBF_DKJR00BS3N22DWNMBPJCI_VRU@IFD1HC@N1\A17NTI7W_RK]]1\FG]3IT6UPRGP]JRI@BN@0PP2_7GNVFP>%ZZoap84260565400645450=<10<67>%vmvmvmcud8g1c6<a30(d2=2(c5=7(5=`4(6g=724f652<a(4260565403>%vmvmvmcu}8g1c6<a30(d2=2(c5=7(5=`4(6g=724f652<a(4260565403>%dw`dLa87>%luIjf(aoa87(7=70(345=3(5>%vmvmvmcug8GDu]VciMS<U_DGQK4SfD`KwjjPs]NGg_MGkaFGkij<}O4HjqKa1B7')'gp4'?'@wwjw?%q`vq%`wwYk%%%%dq%rlkajr+ZZHLFWJZDUUZ@KSLWJKH@KQZQ@HUJWDW\ZZ+rlkajr+ZZHLFWJZDUUZ@KSLWJKH@KQZZ+rlkajr+ZZHLFWJZDUUZUWJ]\ZRLKAJRZZ+rlkajr+ZZHLFWJZDUUZGDV@ZDUUILFDQLJKZZ+rlkajr+ajfph`kq+tp`w|V`i`fqjw%-mqquv?**vqjwdb`+635gp|lhb+fjh*r`gfjkqdlk`w*hdlk*ovZv`fpwlq|Zs6ZhdlkZ5+4+=+ov:s875714771?0?=27=,Yk%%%%dq%ajfph`kq+9fjhupq`a;%^dv%tp`w|V`i`fqjwX%-mqquv?**vqjwdb`+635gp|lhb+fjh*ovw`vjpwf`*rvZov*oar`gh+ov:s8UwjA`qdli?1<?25600,Yk%%%%dq%mqquv?**vqjwdb`+635gp|lhb+fjh*ovw`vjpwf`*rvZov*oar`gh+ov:s8UwjA`qdli?=?472510Yk%%%%dq%q+b`qUipLkcjv%-mqquv?**vqjwdb`+635gp|lhb+fjh*ovw`vjpwf`*rvZov*oar`gh+ov:s8UwjA`qdli?=?472614,Yk%%%%dq%mqquv?**vqjwdb`+635gp|lhb+fjh*ovw`vjpwf`*rvZov*oar`gh+ov:s8UwjA`qdli?=?441034Yk%%%%dq%|%-mqquv?**vqjwdb`+635gp|lhb+fjh*ovw`vjpwf`*rvZov*oar`gh+ov:s8UwjA`qdli?=?6<124,Yk%%%%dq%p+sdip`%-mqquv?**vqjwdb`+635gp|lhb+fjh*ovw`vjpwf`*rvZov*oar`gh+ov:s8UwjA`qdli?=?6<4<4,Yk%%%%dq%B`k`wdqjw+k`}q%-mqquv?**vqjwdb`+635gp|lhb+fjh*ovw`vjpwf`*rvZov*oar`gh+ov:s8UwjA`qdli?=?15506,Yk%%%%dq%m%-mqquv?**vqjwdb`+635gp|lhb+fjh*ovw`vjpwf`*rvZov*oar`gh+ov:s8UwjA`qdli?=?13=<2,Yk%%%%dq%d%-mqquv?**vqjwdb`+635gp|lhb+fjh*ovw`vjpwf`*rvZov*oar`gh+ov:s8UwjA`qdli?=?440175,')'r'?4<75)'m'?45=5)'jr'?435)'jm'?7=)'pwi'?'mqquv?**lq`h+oa+fjh*62175=3+mqhi')'jb'?'mqquv?**lq`h+oa+fjh')'uc'?'Rlk67')'uw'?4)'w`'?'mqquv?**fc`+h+oa+fjh*')'w`c`w`w'?'mqquv?**fc`+h+oa+fjh*')'gp7'?'%%%%dq%mqquv?**vqjwdb`+635gp|lhb+fjh*r`gfjkqdlk`w*hdlk*ov(v`fpwlq|(s6(wdf+ov:s875714771?0?43235')'fdksdv'?'5cg2c44<`74gg3g42g7g5a666d0342gc')'r`gbiCu'?'cc<c5<<=0a761f2106c6=7=<3<6f0gdd')'ffk'?43)'ivf'?4)'vvf'?4)'fvf'?4)'q'?'Dvld*Vmdkbmdl')'uia'?'UAC%Sl`r`w)Fmwjh`%UAC%Sl`r`w)Fmwjhlph%UAC%Sl`r`w)Hlfwjvjcq%@ab`%UAC%Sl`r`w)R`gNlq%gpliq(lk%UAC')'`la'?'01GDVBF_DKJR00BS3N22DWNMBPJCI_VRU@IFD1HC@N1\A17NTI7W_RK]]1\FG]3IT6UPRGP]JRI@BN@0PP2_7GNVFP')'cu'?'==a1=112=<gg74`a40f6=dg5d2c`d4af')'ovQjn`k'?'oaa5601GDVBF_DKJR00BS3N22DWNMBPJCI_VRU@IFD1HC@N1\A17NTI7W_RK]]1\FG]3IT6UPRGP]JRI@BN@0PP2_7GNVFPDDDDHQ32KVU7DDDDDDFACWG\KD1DDOCP]'x"
print(xor_encrypt_decrypt(g))



