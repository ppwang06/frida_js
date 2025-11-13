console.log("frida start into lvzhou ...")

// # frida -U --no-pause -f com.sina.oasis -l lvzhou.js
//<liboasiscore.so> method_name => java.lang.String com.weibo.xvideo.NativeApi.s(byte[], boolean) ,offset=> 0x116cc ,module_name=> liboasiscore.so
function lvzhou() {
    Java.perform(function other() {
        let head = Java.use("com.weibo.xvideo.NativeApi")
        // 使用系统工具类将byte数组转成hex、utf8.
        var ByteString = Java.use("com.android.okhttp.okio.ByteString");
        head.s.implementation = function (barr, z) {
            console.log("str:"+ByteString.of(barr).utf8())
            console.log(barr)
            console.log(z)
            let result = this.s(barr, z);
            console.log(result)
            return result
        }

        // let d = Java.use("bh.d");
        // d["g"].implementation = function (str) {
        //     console.log(`d.g is called: str=${str}`);
        //     let result = this["g"](str);
        //     console.log(`d.g result=${result}`);
        //     return result;
        // };
    })
}


setImmediate(function() {
    setTimeout(lvzhou, 5000);
});
