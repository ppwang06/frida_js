
/**
 * hook导出的加密函数的参数,
 * so里面共传入两个参数,参数1 为要加密的内容, 参数2 为AES ECB模式的key
 * //frida -U --no-pause -f com.shizhuang.duapp -l dewu.js
 *  --no-pause是即时hook
 *  --no-pause 自动运行程序
 *
 *  -f是通过spawn，也就是重启apk注入js
 *  -f 指定一个进程，重启它并注入脚本
 *
 *   -U, --usb             connect to USB device
 *   -l 指定加载一个Javascript脚本
 */


const AES_Calculate = Module.findExportByName("libJNIEncrypt.so", "AES_128_ECB_PKCS5Padding_Encrypt")
console.log("func addr is ---" + AES_Calculate);

// 两个参数的话 参数类似数组的形式进行取值，一个返回结果直接使用即可
if (AES_Calculate !== null) {
    Interceptor.attach(AES_Calculate, {
        onEnter: function (args) {
            let args0 = Memory.readCString(args[0])
            console.log("args0:", args0)

            let args1 = Memory.readCString(args[1]);
            console.log("args1:", args1)

        },
        onLeave: function (retval) {
            let result1 = Memory.readCString(retval);
            console.log("result1", result1)
        }
    });
} else {
    console.log("未找到对应的内存地址...")
}


