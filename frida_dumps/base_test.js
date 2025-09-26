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

// find_so()

// var dlopen_ext = Module.findExportByName(null, "android_dlopen_ext");
// if (dlopen_ext) {
//     Interceptor.attach(dlopen_ext, {
//         onEnter: function (args) {
//             var pathptr = args[0];
//             if (pathptr !== undefined && pathptr != null) {
//                 var path = ptr(pathptr).readCString();
//                 console.log("load " + path);
//             }
//         }
//     });
// } else {
//     console.log("android_dlopen_ext not found!");
// }

function yxs_test() {
    var pthread_create_addr = Module.findExportByName(null, "pthread_create");
    var pthread_create = new NativeFunction(pthread_create_addr, "int", ["pointer", "pointer", "pointer", "pointer"]);
    Interceptor.replace(pthread_create_addr, new NativeCallback((parg0, parg1, parg2, parg3) => {
        let so_name = Process.findModuleByAddress(parg2).name;
        var so_base = Module.getBaseAddress(so_name);
        var offset = (parg2 - so_base);
        var PC = 0;
        if (

            (so_name.indexOf("libexec.so") > -1 && offset === 289256) ||
            (so_name.indexOf("libexec.so") > -1 && offset === 286532)

        ){
            console.log('爱加密检测线程处理')
        } else {
            PC = pthread_create(parg0, parg1, parg2, parg3);
        }

        return PC;
    }, "int", ["pointer", "pointer", "pointer", "pointer"]));
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


//com.zjhzwxzl.jdgj
function hook_exit_vpn() {
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

//简单版 vpn检测过
function main() {
    Java.perform(function () {
        Java.use("java.net.NetworkInterface").getName.implementation = function(){
            var string_class = Java.use("java.lang.String");
            var gname = this.getName();
            if(gname == string_class.$new("tun0")){
                console.log("find ===> ", gname);
                return string_class.$new("rmnet_data0")
            } else{
                console.log("gname ===> ", gname)
            }
            return gname;
        }
        // Java.use("android.net.ConnectivityManager").getNetworkCapabilities.implementation = function(v){
        //     console.log(v)
        //     var res = this.getNetworkCapabilities(v)
        //     console.log("res ==> ", res)
        //     return null;
        // }
        Java.use("android.net.NetworkCapabilities").hasTransport.implementation = function(v){
            console.log(v)
            var res = this.hasTransport(v)
            console.log("res ==> ", res)
            return false;
        }
    })
}




function main_jdgs() {
    main()
}
//
setTimeout(main_jdgs)