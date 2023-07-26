// 快手抓包  不可用 会黑设备 提示操作频繁
// 新版本快手不可用  建议使用 hook_use_http
//com.kuaishou.aegon.okhttp.CronetInterceptorConfig    a

console.log("kuaishou 代理")

//frida -U --no-pause -f com.smile.gifmaker -l kuaishou.js
setImmediate(function() {
   setTimeout(kuaishou, 5000)
});


function kuaishou() {
    Java.perform(function main() {
        console.log("Inside java perform function");

        let utils = Java.use("com.kuaishou.aegon.okhttp.CronetInterceptorConfig");
        utils.a.overload('java.lang.String', '[Ljava.lang.String;', 'boolean').implementation = function (str, strArr, z) {

            let result_one = this.a(str, strArr, z)
            console.log("返回结果为：", result_one)
            return false;
        }
    })
}