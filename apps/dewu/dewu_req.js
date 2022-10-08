//com.shizhuang.duapp.common.helper.net.interceptor
console.log("frida start into 得物 ...")


//frida -U --no-pause -f com.shizhuang.duapp -l dewu.js
setImmediate(function() {
    setTimeout(delay_load_injection, 5000);
});


function delay_load_injection() {
    Java.perform(function dewu() {
        console.log("Frida start to update  method")
        let head = Java.use("com.shizhuang.duapp.modules.productv2.brand.vm.BrandCoverViewModel")

        head.s.implementation = function (z) {
            console.log("传入字符串为:", z)
            let result = this.s(z);
            console.log("md5后数据为：", result)
            return result
        }


    })
}