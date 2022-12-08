"""
快手免费小说 整体流程

1. 请求方式 + & + （请求参数排序后） + & + "时间戳计数"
    时间戳计数：return new j2((int) (System.currentTimeMillis() / TimeUnit.MINUTES.toMillis(1L)), new Random().nextInt());
    例：
    GET&abi=arm64&apiLevel=30&app=KG_APP_NOVEL&categoryType=1&cc=cn&ch=VIVO&did=ANDROID_8b858b6df9940c7b&dpbs=3sCt3iAAMzE5MzgwMTMwAM8HAD3gXNgBuug8rBAAAAB_l
    H2KGr92RXzWQeW8yYDV
    &egid=DFP5671385357024295DFFF7E8DEB8C695C3FCFC9DC88342CCB25D88DBD3262B&fr=ANDROID&isp=&kpf=ANDROID&kpn=KG_APP_NOVEL&lan=zh-cn&md=Xiaomi(M2010J19SC)&mi=&nt=WIFI&oc=Xiaomi&od=704979036e7cbd2f&os=11&privacyDi
    sagreed=0&sr=1080*2218&ss=PHVua25vd24gc3NpZD4=
    &ve=1.0.0.2&-3339544450813078700
2. 调用so  atlasSign  生成sig3(未解决)
3. ("时间戳计数转字节数组 即 -3339544450813078700" + sig3字节数组  )  ---> 转base64
4. 操作base64变换    变换方式：replace('+', '-').replace('/', '_').replaceAll("=", "")
"""