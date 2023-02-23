
console.log("frida start into app ...")

//frida -U --no-pause -f com.shizhuang.duapp -l dewu.js
setImmediate(function() {
    setTimeout(delay_load_injection, 5000);
});


function delay_load_injection() {
    Java.perform(function dewu() {
        console.log("Frida start to update  method")
        let head = Java.use("com.shizhuang.dudatastatistics.aliyunsls.DataStatistics")

        head.t.overload('java.lang.String').implementation = function (str) {
            console.log("传入字符串为:", str)
            let result = this.t(str);
            console.log("md5后数据为：", result)
            return result
        }

    })
}