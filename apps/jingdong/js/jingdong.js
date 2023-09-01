console.log("frida start into jd ...")



//frida -H 127.0.0.1:8080 -U --no-pause -f com.jingdong.app.mall -l jingdong.js
// frida -H 127.0.0.1:8080 -l jingdong.js 京东
Java.perform(function other() {
    let head = Java.use("com.jingdong.common.utils.BitmapkitUtils")

    head.getSignFromJni.implementation = function (Context, str, str2, str3, str4, str5) {
        console.log(Context)
        console.log(str)
        console.log(str2)
        console.log(str3)
        console.log(str4)
        console.log(str5)
        let result = this.getSignFromJni(Context, str, str2, str3, str4, str5);
        console.log(result)
        return result
    }
})
