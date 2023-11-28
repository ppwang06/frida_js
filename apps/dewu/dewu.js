/*
*
    var linker = Process.findModuleByName('linker64');
    var exports = linker.enumerateSymbols();
    var call_function_addr1 = null;
    for (var i in exports) {
        var exports_name = exports[i].name;
        var exports_address = exports[i].address;

        // __dl__Z20__android_dlopen_extPKciPK17android_dlextinfoPKv
        // if (exports_name.indexOf("__dl__Z20__android_dlopen_extPKciPK17android_dlextinfoPKv") !== -1) {
        if (exports_name.indexOf('__dl___loader_android_dlopen_ext') !== -1) {
            // console.log('__dl___loader_android_dlopen_ext finded:', linker.name, exports_name, exports_address, exports_address.sub(linker.base));
            call_function_addr1 = exports_address;
        }
    }

    if (call_function_addr1 != null) {
        Interceptor.attach(call_function_addr1, {
            onEnter: function (args) {
                // console.log(Memory.readUtf8String(args[0]));
                if (Memory.readUtf8String(args[0]).indexOf('libmsaoaidsec.so') !== -1) {
                    args[0].writeUtf8String('/system/lib64/libc.so');
                    // console.log('replace libmsaoaidsec to libc');
                }
            },
        });
    }
* */
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