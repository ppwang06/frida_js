/*
*
*
* com.jf.my
* frida -U --pause -f com.jf.my  -l frida_miyuan.js
* */

//找寻反调试的so文件
function find_so() {
    Java.perform(function () {

        var dlopen = Module.findExportByName(null, "dlopen");
        var android_dlopen_ext = Module.findExportByName(null, "android_dlopen_ext");

        Interceptor.attach(dlopen, {
            onEnter: function (args) {
                var path_ptr = args[0];
                var path = ptr(path_ptr).readCString();
                console.log("[dlopen:]", path);
            },
            onLeave: function (retval) {

            }
        });

        Interceptor.attach(android_dlopen_ext, {
            onEnter: function (args) {
                var path_ptr = args[0];
                var path = ptr(path_ptr).readCString();
                console.log("[dlopen_ext:]", path);
            },
            onLeave: function (retval) {

            }
        });
    });
}

function hook_java() {
    Java.perform(function other() {
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
        // jdgs
        let bridge = Java.use("com.jd.security.jdguard.core.Bridge")
        bridge["main"].implementation = function (i2, objArr) {
            console.log(`Bridge.main is called: i2=${i2}, objArr=${objArr}`);
            let result = this["main"](i2, objArr);
            console.log(`Bridge.main result=${result.toString()}`);
            return result;
        };

        //查看第一个入参的结果
        let c = Java.use("el.c");
        c["A"].implementation = function (bArr) {
            console.log(`c.A is called: bArr=${bArr}`);
            let result = this["A"](bArr);
            console.log(`c.A result=${result}`);
            return result;
        };
    })
}


//找强退的so文件
function hook_dlopen() {
    Interceptor.attach(Module.findExportByName(null, "android_dlopen_ext"),
        {
            onEnter: function (args) {
                var pathptr = args[0];
                if (pathptr !== undefined && pathptr != null) {
                    var path = ptr(pathptr).readCString();
                    console.log("load " + path);
                }
            }
        }
    );
}

function hook_pthread_create() {
    Interceptor.attach(Module.findExportByName("libc.so", "pthread_create"),{
        onEnter: function (args) {
            let func_addr = args[2];
            console.log("线程函数被调用了----", func_addr, "调用so----" + Process.findModuleByAddress(func_addr).name)
            if(Process.findModuleByAddress(func_addr).name.indexOf("libexec.so") != -1){
                Interceptor.replace(func_addr, new NativeCallback(
                    function () {
                        console.log("线程函数被替换了---", func_addr)
                        return ;
                    }
                , 'void', ['void']))
            }
        },
        onLeave: function (retval) {
        }
    })
}

/*
*
* normal find thread func offset libexec.so 0x752377008c 196748 3008c
normal find thread func offset libexec.so 0x7523770160 196960 30160
normal find thread func offset libexec.so 0x7523783c88 277640 43c88
normal find thread func offset libexec.so 0x752378711c 291100 4711c
normal find thread func offset libexec.so 0x7523787388 291720 47388
* */

function yxs_test() {
    var pthread_create_addr = Module.findExportByName("libc.so", "pthread_create");
    var pthread_create = new NativeFunction(pthread_create_addr, "int", ["pointer", "pointer", "pointer", "pointer"]);
    Interceptor.replace(pthread_create_addr, new NativeCallback((parg0, parg1, parg2, parg3) => {
        let so_name = Process.findModuleByAddress(parg2).name;
        var so_base = Module.getBaseAddress(so_name);
        var offset = (parg2 - so_base);
        var PC = 0;
        if (
            (so_name.indexOf("libexec.so") > -1 && offset === 271572)
        ){
            console.log('爱加密检测线程处理')
        } else {
            PC = pthread_create(parg0, parg1, parg2, parg3);
        }

        return PC;
    }, "int", ["pointer", "pointer", "pointer", "pointer"]));
}
yxs_test()


// var pthread_create_addr = Module.findExportByName(null, "pthread_create");
// var pthread_create = new NativeFunction(pthread_create_addr, "int", ["pointer", "pointer", "pointer", "pointer"]);
//
// Interceptor.replace(pthread_create_addr, new NativeCallback(
//     function(parg0, parg1, parg2, parg3) {
//         let so_name = Process.findModuleByAddress(parg2).name;
//         var so_base = Module.getBaseAddress(so_name);
//         var offset = (parg2 - so_base);
//         var PC = 0;
//         console.log("normal find thread func offset", so_name, parg2, offset, offset.toString(16));
//         return pthread_create(parg0, parg1, parg2, parg3);
//         // 或 return 0; 如果你不想调用原始的 pthread_create
//     },
//     "int", // 返回类型
//     ["pointer", "pointer", "pointer", "pointer"] // 参数类型
// ));




// function hook_dlopen(soName = '') {
//     Interceptor.attach(Module.findExportByName(null, "android_dlopen_ext"), {
//         onEnter: function(args) {
//             var pathptr = args[0];
//             if (pathptr) {
//                 var path = ptr(pathptr).readCString();
//                 console.log("Loading: " + path);
//                 if (path.indexOf(soName) >= 0) {
//                     console.log("Already loading: " + soName);
//                     // hook_system_property_get();
//                 }
//             }
//         }
//     });
// }
// setImmediate(hook_dlopen, "libexec.so");


// function hook_pthread_create(){
//     Interceptor.attach(Module.findExportByName(null, "pthread_create"),
//         {
//             onEnter: function (args) {
//                 var module = Process.findModuleByAddress(ptr(this.returnAddress))
//                 //this.returnAddress返回当前函数的地址，也就是谁调用的这个函数
//                 if (module != null) {
//                     console.log("[pthread_create] called from", module.name)
//                 }
//                 else {
//                     console.log("[pthread_create] called from", ptr(this.returnAddress))
//                 }
//             },
//         }
//     )
// }
// hook_pthread_create()


// function hook_pthread() {
//
//     var pthread_create_addr = Module.findExportByName('libc.so', 'pthread_create');
//     console.log("pthread_create_addr,", pthread_create_addr);
//
//     var pthread_create = new NativeFunction(pthread_create_addr, "int", ["pointer", "pointer", "pointer", "pointer"]);
//
//     Interceptor.replace(pthread_create_addr, new NativeCallback(function (a,b,c,d) {
//         var m = Process.getModuleByName("libexec.so");
//         var base = m.base;
//         var so_name = Process.getModuleByAddress(c).name;
//         var so_path = Process.getModuleByAddress(c).path;
//         var offset = c.sub(base);
//
//         console.log("so_name", so_name, "offset", offset, "path", so_path, "parg2", c);
//
//         var PC = 0;
//         if ((so_name.indexOf("libexec.so") > -1) || (so_name.indexOf("xxxx") > -1)) {
//         console.log("find thread func offset", so_name, offset);
//
//         // 循环检测偏移量，如果命中则不创建线程，只是打印anti bypss
//         if ((0x4400c === offset)) {
//             console.log("anti bypass");
//         } else if (0x44060 === offset) {
//             console.log("anti bypass");
//         } else {
//             PC = pthread_create(a,b,c,d);
//             console.log("ordinary sequence", PC)
//         }
//         } else {
//         PC = pthread_create(a,b,c,d);
//         // console.log("ordinary sequence", PC)
//         }
//         return PC;
//     }, "int", ["pointer", "pointer", "pointer", "pointer"]))
// }
// hook_pthread()


// yxs_test()
// function main_jdgs() {
//     hook_dlopen()
// }
// setTimeout(main_jdgs)