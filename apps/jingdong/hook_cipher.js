console.log("frida start into jd ...")



//frida -H 127.0.0.1:8080 -U --no-pause -f com.jingdong.app.mall -l jingdong.js
// frida -H 127.0.0.1:8080 -l hook_cipher.js 京东
// frida -H 127.0.0.1:8080 -f com.jingdong.app.mall -l hook_cipher.js
Java.perform(function other() {
    let head = Java.use("com.jd.phc.d")

    head.b.implementation = function (bArr) {
        console.log(bArr)
        let result = this.b(bArr);
        console.log(result)
        return result
    }
})