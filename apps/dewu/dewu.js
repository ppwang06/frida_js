
console.log("frida start into 得物 ...")

//frida -U --no-pause -f com.shizhuang.duapp -l dewu.js
setImmediate(function() {
    setTimeout(delay_load_injection, 5000);
});


function delay_load_injection() {
    Java.perform(function dewu() {
        console.log("Frida start to update  method")

        // let uticcls = Java.use("com.shizhuang.duapp.common.utils.RequestUtils");
        // uticcls.a.overload('java.lang.String').implementation = function (str) {
        //     console.log("传入字符串为:", str)
        //     let result = this.a(str);
        //     console.log("md5后数据为：", result)
        //     return result
        // }
        //
        // let aes_util = Java.use("com.duapp.aesjni.AESEncrypt");
        // aes_util.encode.overload('java.lang.Object', 'java.lang.String') .implementation = function (obj, str) {
        //     console.log("aes  encode 传入字符串为:", obj)
        //     console.log("aes encode 传入字符串为:", str)
        //     let result = this.encode(obj, str);
        //     console.log("aes结果：", result)
        //     return result
        // }
        //
        // aes_util.encodeByte.implementation = function (b_arr, str) {
        //     console.log("encodeByte传入数组字符串为:", b_arr)
        //     console.log("encodeByte传入字符串为:", str)
        //     let c_result = this.encodeByte(b_arr, str);
        //     console.log("aes结果：", c_result)
        //     return c_result
        // }
        let head = Java.use("com.shizhuang.dudatastatistics.aliyunsls.DataStatistics")

        head.t.overload('java.lang.String').implementation = function (str) {
            console.log("传入字符串为:", str)
            let result = this.t(str);
            console.log("md5后数据为：", result)
            return result
        }


    })
}