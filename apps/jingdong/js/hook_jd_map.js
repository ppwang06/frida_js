console.log("frida start into jd ...")


// frida -H 127.0.0.1:8080 -l hook_jd_map.js 京东
Java.perform(function other() {
    let head = Java.use("com.jd.phc.e")

    head.b.implementation = function (map, bArr) {
        // map 数据类型打印
        var keyset3 = map.keySet();
        var it3 = keyset3.iterator();
        while(it3.hasNext()){
            var keystr3 = it3.next().toString();
            var valuestr3 = map.get(keystr3);
            console.log("--->", keystr3, valuestr3)
        }
        console.log(bArr)
        let result = this.b(map, bArr);
        console.log(result)
        return result
    }
})