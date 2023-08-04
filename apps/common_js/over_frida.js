
console.log("frida start into jd ...")


Java.perform(function other() {
    console.log('hooking2');
    var strstr = Module.findExportByName("libc.so", "strstr");
    console.log("find strstr:", strstr);
    Interceptor.attach(strstr, {
        onEnter: function (args) {
            // 判断 LIBFRIDA 字符串
            if (ptr(args[1]).readCString().indexOf("LIBFRIDA") >= 0 ){
                this.LIBFRIDA = true
            }
            if (ptr(args[1]).readCString().indexOf("frida") >= 0) {
                this.frida = true
            }

            if (ptr(args[1]).readCString().indexOf(":5DBA") >= 0 ){
                this.d8a = true
            }
            if (ptr(args[1]).readCString().indexOf(":69A2") >= 0 ){
                this.a2 = true
            }
        },
        onLeave: function(retval){
            if (this.LIBFRIDA){
                retval.replace(0x0);
            }
            if (this.frida){
                retval.replace(0x0);
            }
            if (this.d8a){
                retval.replace(0x0);
            }
            if (this.a2){
                retval.replace(0x0);
            }
        }
    })

     // 打印调用堆栈
    function showStack() {
        let Throwable = Java.use("java.lang.Throwable");
        let stackTraceString = Java.use("android.util.Log").getStackTraceString(Throwable.$new())
        console.log(stackTraceString);
    }
})
