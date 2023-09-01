/*
hook  jinddong  so代码
libjdbitmapkit.so
st=1665454891291&sign=1d1dbfb3989fdf1b9f1989f4029b0cf1&sv=111
frida -H 127.0.0.1:8080 -l hook_jd_so.js 京东
不可用
*/
console.log("start to hook handler so code....")


// hook 导出函数
const sign = Module.findExportByName("libjdbitmapkit.so", "Java_com_jingdong_common_utils_BitmapkitUtils_getSignFromJni")
console.log("getSignFromJni addr is ---" + sign);


if (sign !== null){
    console.log("找到目标函数")
    Interceptor.attach(sign, {
        onEnter: function (args) {
            console.log("input:\n", hexdump(args))
        },
        onLeave: function (retval) {
            console.log("result:\n", hexdump(retval))
        }
    });
} else {
    console.log("未找到目标函数地址...")
}