//frida -U --pause -f com.xxxxxx -l c.js
function hook_java() {
    Java.perform(function other() {
        // eid
        // var linker = Process.findModuleByName('linker64');
        // var exports = linker.enumerateSymbols();
        // var call_function_addr1 = null;
        // for (var i in exports) {
        //     var exports_name = exports[i].name;
        //     var exports_address = exports[i].address;
        //
        //     // __dl__Z20__android_dlopen_extPKciPK17android_dlextinfoPKv
        //     // if (exports_name.indexOf("__dl__Z20__android_dlopen_extPKciPK17android_dlextinfoPKv") !== -1) {
        //     if (exports_name.indexOf('__dl___loader_android_dlopen_ext') !== -1) {
        //         // console.log('__dl___loader_android_dlopen_ext finded:', linker.name, exports_name, exports_address, exports_address.sub(linker.base));
        //         call_function_addr1 = exports_address;
        //     }
        // }
        //
        // if (call_function_addr1 != null) {
        //     Interceptor.attach(call_function_addr1, {
        //         onEnter: function (args) {
        //             // console.log(Memory.readUtf8String(args[0]));
        //             if (Memory.readUtf8String(args[0]).indexOf('libmsaoaidsec.so') !== -1) {
        //                 args[0].writeUtf8String('/system/lib64/libc.so');
        //                 // console.log('replace libmsaoaidsec to libc');
        //             }
        //         },
        //     });
        // }
        // var strstr = Module.findExportByName("libc.so", "strstr");
        // console.log("find strstr:", strstr);
        // Interceptor.attach(strstr, {
        //     onEnter: function (args) {
        //         // 判断 LIBFRIDA 字符串
        //         if (ptr(args[1]).readCString().indexOf("LIBFRIDA") >= 0 ){
        //             this.LIBFRIDA = true
        //         }
        //         if (ptr(args[1]).readCString().indexOf("frida") >= 0) {
        //             this.frida = true
        //         }
        //
        //         if (ptr(args[1]).readCString().indexOf(":5DBA") >= 0 ){
        //             this.d8a = true
        //         }
        //         if (ptr(args[1]).readCString().indexOf(":69A2") >= 0 ){
        //             this.a2 = true
        //         }
        //     },
        //     onLeave: function(retval){
        //         if (this.LIBFRIDA){
        //             retval.replace(0x0);
        //         }
        //         if (this.frida){
        //             retval.replace(0x0);
        //         }
        //         if (this.d8a){
        //             retval.replace(0x0);
        //         }
        //         if (this.a2){
        //             retval.replace(0x0);
        //         }
        //     }
        // })
        let b = Java.use("com.ex.sdk.java.utils.f.b");
        b["a"].implementation = function (str) {
            console.log(`b.a is called: str=${str}`);
            let result = this["a"](str);
            console.log(`b.a result=${result}`);
            return result;
        };

    })
}

function main_jdgs() {
    hook_java()
}

setTimeout(main_jdgs)