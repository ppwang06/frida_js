/*
*jdgs 参数 b1 b2 b3 b4 b5 b6 b5
*
* */

console.log("frida start into jd ...")


// frida -H 127.0.0.1:8080 -l jingdong_b1.js 京东
Java.perform(function other() {
    let head = Java.use("com.jd.security.jdguard.a.e")
    let core = Java.use("com.jd.security.jdguard.core.e")
    let bridge = Java.use("com.jd.security.jdguard.core.Bridge")

    // head.o.overload('android.net.Uri$Builder').implementation = function (str) {
    //     console.log(str)
    //     let result = this.o(str);
    //     console.log(result)
    //     return result
    // }
    //   d--->/client.action
    // head.d.implementation = function () {
    //     let result = this.d();
    //     console.log("dd---->", result)
    //     return result
    // }
    // core.A.implementation = function (bArr) {
    //     console.log(bArr)
    //     let result = this.A(bArr);
    //     console.log(result)
    //     return result
    // }
    function showStack() {
        let Throwable = Java.use("java.lang.Throwable");
        let stackTraceString = Java.use("android.util.Log").getStackTraceString(Throwable.$new())
        console.log(stackTraceString);
    }

    bridge.main.implementation = function (i, obj) {
        // showStack()
        // console.log(i, obj)
        console.log(i)
        for (let index=0; index < obj.length; index++) {
          const elem = obj[index];
          console.log(elem)
        }
        let result = this.main(i, obj);
        console.log(result)
        return result
    }
})