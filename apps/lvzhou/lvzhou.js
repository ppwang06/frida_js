console.log("frida start into lvzhou ...")

// # frida -U --no-pause -f com.sina.oasis -l lvzhou.js
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
    })
}


setImmediate(function() {
    setTimeout(lvzhou, 5000);
});
