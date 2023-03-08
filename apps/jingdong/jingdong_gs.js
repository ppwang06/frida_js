/*
*jdgs 参数 b1 b2 b3 b4 b5 b6 b5
* String o = o(h());
* h() 即为 包含sign sv st 整个链接编码
* https://api.m.jd.com/client.action?functionId=wareBusiness&lmt=0&clientVersion=11.6.3&build=98691&client=android&partner=tencent&oaid=704979036e7cbd2f&eid=eidAc9c18120fasbMLKP5hp3SOaYpQ20bPRbRjCykWy6sCpawV+EKUqtGllWA1x9X58cLDd6CDY46a0NjavcgM6H8WitQBS1gOXCegnS1NJM82gPh5J0&sdkVersion=30&lang=zh_CN&harmonyOs=0&networkType=wifi&uemps=0-2-2&ext={"prstate":"0","pvcStu":"1"}&ef=1&ep={"hdid":"JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw=","ts":1677739871655,"ridx":-1,"cipher":{"area":"CV83Cv8yDzu5XzK=","d_model":"JJSmCJLACJvJGm==","wifiBssid":"dW5hbw93bq==","osVersion":"CJO=","d_brand":"WQvrb21f","screen":"CtSnEMenCNqm","uuid":"CWY5ZWVuYwVvYtO5ZtdwZG==","aid":"CWY5ZWVuYwVvYtO5ZtdwZG==","openudid":"CWY5ZWVuYwVvYtO5ZtdwZG=="},"ciphertype":5,"version":"1.2.0","appname":"com.jingdong.app.mall"}&bef=1&scval=10058672351007&st=1677740688768&sign=6125c906de1d98c0f51dc0ec30eaf266&sv=122
* https://api.m.jd.com/client.action?functionId=wareBusiness&lmt=0&clientVersion=11.6.3&build=98691&client=android&partner=tencent&oaid=704979036e7cbd2f&eid=eidAc9c18120fasbMLKP5hp3SOaYpQ20bPRbRjCykWy6sCpawV+EKUqtGllWA1x9X58cLDd6CDY46a0NjavcgM6H8WitQBS1gOXCegnS1NJM82gPh5J0&sdkVersion=30&lang=zh_CN&harmonyOs=0&networkType=wifi&uemps=0-2-2&ext=%7B%22prstate%22%3A%220%22%2C%22pvcStu%22%3A%221%22%7D&ef=1&ep=%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1677739871655%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22area%22%3A%22CV83Cv8yDzu5XzK%3D%22%2C%22d_model%22%3A%22JJSmCJLACJvJGm%3D%3D%22%2C%22wifiBssid%22%3A%22dW5hbw93bq%3D%3D%22%2C%22osVersion%22%3A%22CJO%3D%22%2C%22d_brand%22%3A%22WQvrb21f%22%2C%22screen%22%3A%22CtSnEMenCNqm%22%2C%22uuid%22%3A%22CWY5ZWVuYwVvYtO5ZtdwZG%3D%3D%22%2C%22aid%22%3A%22CWY5ZWVuYwVvYtO5ZtdwZG%3D%3D%22%2C%22openudid%22%3A%22CWY5ZWVuYwVvYtO5ZtdwZG%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D&bef=1&scval=10058672351007&st=1677740688768&sign=6125c906de1d98c0f51dc0ec30eaf266&sv=122
* 进入o 函数
* String d2 = d(); 查看d2的值
* d2 应为域名后面的值 /client.action
*
*
* bb9983b0937bea1e9ea822cee2ed9754f77b0ddcb3316d13a4718be7a1ea7a09=&build=98691&client=android&clientVersion=11.6.3&ef=1&eid=eidAc9c18120fasbMLKP5hp3SOaYpQ20bPRbRjCykWy6sCpawV+EKUqtGllWA1x9X58cLDd6CDY46a0NjavcgM6H8WitQBS1gOXCegnS1NJM82gPh5J0&ep=%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1677746727693%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22area%22%3A%22CV83Cv8yDzu5XzK%3D%22%2C%22d_model%22%3A%22JJSmCJLACJvJGm%3D%3D%22%2C%22wifiBssid%22%3A%22dW5hbw93bq%3D%3D%22%2C%22osVersion%22%3A%22CJO%3D%22%2C%22d_brand%22%3A%22WQvrb21f%22%2C%22screen%22%3A%22CtSnEMenCNqm%22%2C%22uuid%22%3A%22CWY5ZWVuYwVvYtO5ZtdwZG%3D%3D%22%2C%22aid%22%3A%22CWY5ZWVuYwVvYtO5ZtdwZG%3D%3D%22%2C%22openudid%22%3A%22CWY5ZWVuYwVvYtO5ZtdwZG%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D&ext=%7B%22prstate%22%3A%220%22%2C%22pvcStu%22%3A%221%22%7D&functionId=getLegoWareDetailComment&harmonyOs=0&lang=zh_CN&lmt=0&networkType=wifi&oaid=704979036e7cbd2f&partner=tencent&sdkVersion=30&sign=615681b7c713fe98277828aa5531c146&st=1677748980740&sv=120&uemps=0-2-2
* bb9983b0937bea1e9ea822cee2ed9754f77b0ddcb3316d13a4718be7a1ea7a09=&build=98691&client=android&clientVersion=11.6.3&ef=1&eid=eidAc9c18120fasbMLKP5hp3SOaYpQ20bPRbRjCykWy6sCpawV+EKUqtGllWA1x9X58cLDd6CDY46a0NjavcgM6H8WitQBS1gOXCegnS1NJM82gPh5J0&ep={"hdid":"JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw=","ts":1677746727693,"ridx":-1,"cipher":{"area":"CV83Cv8yDzu5XzK=","d_model":"JJSmCJLACJvJGm==","wifiBssid":"dW5hbw93bq==","osVersion":"CJO=","d_brand":"WQvrb21f","screen":"CtSnEMenCNqm","uuid":"CWY5ZWVuYwVvYtO5ZtdwZG==","aid":"CWY5ZWVuYwVvYtO5ZtdwZG==","openudid":"CWY5ZWVuYwVvYtO5ZtdwZG=="},"ciphertype":5,"version":"1.2.0","appname":"com.jingdong.app.mall"}&ext={"prstate":"0","pvcStu":"1"}&functionId=getLegoWareDetailComment&harmonyOs=0&lang=zh_CN&lmt=0&networkType=wifi&oaid=704979036e7cbd2f&partner=tencent&sdkVersion=30&sign=615681b7c713fe98277828aa5531c146&st=1677748980740&sv=120&uemps=0-2-2
*
*
* https://api.m.jd.com/client.action?functionId=wareBusiness&lmt=0&clientVersion=11.6.3&build=98691&client=android&partner=tencent&oaid=704979036e7cbd2f&eid=eidAc9c18120fasbMLKP5hp3SOaYpQ20bPRbRjCykWy6sCpawV+EKUqtGllWA1x9X58cLDd6CDY46a0NjavcgM6H8WitQBS1gOXCegnS1NJM82gPh5J0&sdkVersion=30&lang=zh_CN&harmonyOs=0&networkType=wifi&uemps=0-2-2&ext={"prstate":"0","pvcStu":"1"}&ef=1&ep={"hdid":"JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw=","ts":1677750005535,"ridx":-1,"cipher":{"area":"CV83Cv8yDzu5XzK=","d_model":"JJSmCJLACJvJGm==","wifiBssid":"dW5hbw93bq==","osVersion":"CJO=","d_brand":"WQvrb21f","screen":"CtSnEMenCNqm","uuid":"CWY5ZWVuYwVvYtO5ZtdwZG==","aid":"CWY5ZWVuYwVvYtO5ZtdwZG==","openudid":"CWY5ZWVuYwVvYtO5ZtdwZG=="},"ciphertype":5,"version":"1.2.0","appname":"com.jingdong.app.mall"}&bef=1&scval=10041076378326&st=1677808140757&sign=89a959ede50a598eca21615f24731f31&sv=102
* bef=1&build=98691&c464ac81321971d7cb99debd7c4768a391d2732e3eff1f0274cfae6f71b548bb=&client=android&clientVersion=11.6.3&ef=1&eid=eidAc9c18120fasbMLKP5hp3SOaYpQ20bPRbRjCykWy6sCpawV+EKUqtGllWA1x9X58cLDd6CDY46a0NjavcgM6H8WitQBS1gOXCegnS1NJM82gPh5J0&ep={"hdid":"JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw=","ts":1677750005535,"ridx":-1,"cipher":{"area":"CV83Cv8yDzu5XzK=","d_model":"JJSmCJLACJvJGm==","wifiBssid":"dW5hbw93bq==","osVersion":"CJO=","d_brand":"WQvrb21f","screen":"CtSnEMenCNqm","uuid":"CWY5ZWVuYwVvYtO5ZtdwZG==","aid":"CWY5ZWVuYwVvYtO5ZtdwZG==","openudid":"CWY5ZWVuYwVvYtO5ZtdwZG=="},"ciphertype":5,"version":"1.2.0","appname":"com.jingdong.app.mall"}&ext={"prstate":"0","pvcStu":"1"}&functionId=wareBusiness&harmonyOs=0&lang=zh_CN&lmt=0&networkType=wifi&oaid=704979036e7cbd2f&partner=tencent&scval=10041076378326&sdkVersion=30&sign=89a959ede50a598eca21615f24731f31&st=1677808140757&sv=102&uemps=0-2-2
*
* POST /client.action bef=1&build=98691&c464ac81321971d7cb99debd7c4768a391d2732e3eff1f0274cfae6f71b548bb=&client=android&clientVersion=11.6.3&ef=1&eid=eidAc9c18120fasbMLKP5hp3SOaYpQ20bPRbRjCykWy6sCpawV+EKUqtGllWA1x9X58cLDd6CDY46a0NjavcgM6H8WitQBS1gOXCegnS1NJM82gPh5J0&ep=%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1677750005535%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22area%22%3A%22CV83Cv8yDzu5XzK%3D%22%2C%22d_model%22%3A%22JJSmCJLACJvJGm%3D%3D%22%2C%22wifiBssid%22%3A%22dW5hbw93bq%3D%3D%22%2C%22osVersion%22%3A%22CJO%3D%22%2C%22d_brand%22%3A%22WQvrb21f%22%2C%22screen%22%3A%22CtSnEMenCNqm%22%2C%22uuid%22%3A%22CWY5ZWVuYwVvYtO5ZtdwZG%3D%3D%22%2C%22aid%22%3A%22CWY5ZWVuYwVvYtO5ZtdwZG%3D%3D%22%2C%22openudid%22%3A%22CWY5ZWVuYwVvYtO5ZtdwZG%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D&ext=%7B%22prstate%22%3A%220%22%2C%22pvcStu%22%3A%221%22%7D&functionId=wareBusiness&harmonyOs=0&lang=zh_CN&lmt=0&networkType=wifi&oaid=704979036e7cbd2f&partner=tencent&scval=10041076378326&sdkVersion=30&sign=89a959ede50a598eca21615f24731f31&st=1677808140757&sv=102&uemps=0-2-2
*
* "请求方式" + "空格" + "uri"  + "空格" + "url参数排序 + 请求body(sha256)="""
*
* u() 标准str
* -|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-§§-|-§§-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-§§-|-§§-|-|-|-§§-|-|-|-|-|-|-|-|-|-|-§§-|-|-|-|-§§-|-|-|-|-|-|-
* lime|-|lime|-|-|-|-|-|-|-|-|-|-|-|-|-|-§§0|1§§-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-§§-|114551566336§§-|-|1.0|-§§0|1|-|-|-|-|-|-|-|-|-§§XiaoMi/MIUI/V125|-|-|1677724370806|-§§-|-|-|-|-|-|-
* s()
* eidAc9c18120fasbMLKP5hp3SOaYpQ20bPRbRjCykWy6sCpawV+EKUqtGllWA1x9X58cLDd6CDY46a0NjavcgM6H8WitQBS1gOXCegnS1NJM82gPh5J0
* w()
* 1.0
* q()
* 83
* public static native Object[] main(int i2, Object[] objArr);
* Object[] main = Bridge.main(101, new Object[]{bArr, u(), s(), w(), q()});
*
*
* */

console.log("frida start into jd ...")


// frida -H 127.0.0.1:8080 -l jingdong_gs.js 京东
Java.perform(function other() {
    let head = Java.use("com.jd.security.jdguard.a.e")
    let dak = Java.use("com.jd.security.jdguard.d.a")
    let headc = Java.use("com.jd.security.jdguard.a.c")
    let core = Java.use("com.jd.security.jdguard.core.e")
    let bridge = Java.use("com.jd.security.jdguard.core.Bridge")
    let clza = Java.use("com.jd.security.jdguard.a.e$a");

    // 打印调用堆栈
    function showStack() {
        let Throwable = Java.use("java.lang.Throwable");
        let stackTraceString = Java.use("android.util.Log").getStackTraceString(Throwable.$new())
        console.log(stackTraceString);
    }

    // 打印进入so的入参
    bridge.main.implementation = function (i2, uri_list) {
        console.log("uri-->:", i2, uri_list)
        let result = this.main(i2, uri_list)
        console.log("获取到的main()结果为", result)
        return result
    }

    headc.b.overload('java.net.URI',  '[B', 'java.lang.String', 'java.lang.String', 'boolean').implementation = function (uri,  bArr, str, str2, z) {
        console.log("aaa", bArr)
        return this.b(uri, bArr, str, str2, z)
    }


    // 获取jdgs结果
    // head.i.implementation = function () {
    //     let result = this.i();
    //     var keyset3 = result.keySet();
    //     var it3 = keyset3.iterator();
    //     // 获取java map 数据
    //     while(it3.hasNext()){
    //         var keystr3 = it3.next().toString();
    //         var valuestr3 = result.get(keystr3);
    //         console.log( "jdgs结果", keystr3, valuestr3)
    //     }
    //     return result
    // }

    // 获取o的结果
    head.o.implementation = function (uri) {
        console.log("uri-->:", uri)
        let result = this.o(uri);
        // console.log("获取到的o()结果为", result)
        return result
    }

    // 获取传入A的字节
    core.A.implementation = function (barr) {
        console.log("A--->barr-->:", barr)
        let result = this.A(barr);
        console.log("获取到的A()结果为", result)
        return result
    }

    // 获取a()操作
    // head.a.implementation = function (alist, build, z) {
    //     console.log("list-->:", alist, build, z)
    //     let result = this.a(alist, build, z);
    //     console.log("获取到的j()结果为", result)
    //     return result
    // }

    // headc.a.overload('java.net.URI', 'boolean', '[B', 'java.lang.String', 'java.lang.String', 'java.util.Map', 'java.lang.String', 'java.util.Map').implementation = function (uri, z, bArr, str, str2, str3) {
    //     console.log(bArr)
    //     // let result = this.a();
    //     // console.log("获取到的a()结果为", result)
    //     // return result
    // }


    // 获取h()结果 即入参
    // head.h.implementation = function () {
    //     let result = this.h();
    //     console.log("获取到的h()结果为", result)
    //     return result
    // }

    // 获取 d2的值
    // head.d.implementation = function () {
    //     let result = this.d();
    //     console.log("获取到的d()结果为", result)
    //     return result
    // }

    // 获取 g的值  true
    // head.g.implementation = function () {
    //     let result = this.g();
    //     console.log("获取到的g()结果为", result)
    //     return result
    // }

    // 获取 g的值  true
    // head.j.implementation = function (c) {
    //     console.log("j的入参为：", c.value)
    //     let result = this.j(c);
    //     console.log("获取到的j()结果为", result)
    //     return result
    // }

})