/*
* 过简单的vpn检测 氢氧水  com.zjhzwxzl.jdgj
* frida -U --pause -f com.zjhzwxzl.jdgj  -l new_hook.js
*
* 蜜源的 com.jf.my
* frida -U --pause -f com.jf.my  -l new_hook.js
*
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

//  hook_dlopen1()
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

        let b = Java.use("com.jzyd.coupon.network.b");
        b["a"].overload('java.util.SortedMap').implementation = function (sortedMap) {
            console.log(`b.a is called: sortedMap=${sortedMap}`);

            // 查看map值
            var keyset3 = sortedMap.keySet();
            var it3 = keyset3.iterator();
            while(it3.hasNext()){
                var keystr3 = it3.next().toString();
                var valuestr3 = sortedMap.get(keystr3);
                console.log(keystr3, valuestr3)
            }

            let result = this["a"](sortedMap);
            console.log(`b.a result=${result}`);
            return result;
        };

        let b1 = Java.use("com.ex.sdk.java.utils.f.b");
        b1["a"].implementation = function (str) {
            console.log(`b.a is called: str=${str}`);
            let result = this["a"](str);
            console.log(`b.a result=${result}`);
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
function hook_dlopen1() {
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

//简单版 vpn检测过 h2o
function main() {
    Java.perform(function () {
        Java.use("java.net.NetworkInterface").getName.implementation = function(){
            var string_class = Java.use("java.lang.String");
            var gname = this.getName();
            if(gname === string_class.$new("tun0")){
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



///lib/arm64/libmsaoaidsec.so  shengqian
function hook_dlopen(){
    //Android8.0之后加载so通过android_dlopen_ext函数
    var android_dlopen_ext = Module.findExportByName(null,"android_dlopen_ext");
    console.log("addr_android_dlopen_ext",android_dlopen_ext);
    Interceptor.attach(android_dlopen_ext,{
        onEnter:function(args){
            var pathptr = args[0];
            if(pathptr!=null && pathptr != undefined){
                var path = ptr(pathptr).readCString();
                if(path.indexOf("libmsaoaidsec.so")!=-1){
                    console.log("android_dlopen_ext:",path);
                    hook_call_constructors()
                }
            }
        },
        onLeave:function(retvel){
            //console.log("leave!");
        }
    })

    Java.perform(function other() {
        let b = Java.use("com.jzyd.coupon.network.b");
        b["a"].overload('java.util.SortedMap').implementation = function (sortedMap) {
            console.log(`b.a is called: sortedMap=${sortedMap}`);

            // 查看map值
            var keyset3 = sortedMap.keySet();
            var it3 = keyset3.iterator();
            while(it3.hasNext()){
                var keystr3 = it3.next().toString();
                var valuestr3 = sortedMap.get(keystr3);
                console.log(keystr3, valuestr3)
            }

            let result = this["a"](sortedMap);
            console.log(`b.a result=${result}`);
            return result;
        };

        let b1 = Java.use("com.ex.sdk.java.utils.f.b");
        b1["a"].implementation = function (str) {
            console.log(`b.a is called: str=${str}`);
            let result = this["a"](str);
            console.log(`b.a result=${result}`);
            return result;
        };
    })

}

function hook_call_constructors() {
    let linker = null;
    if (Process.pointerSize === 4) {
        linker = Process.findModuleByName("linker");
    } else {
        linker = Process.findModuleByName("linker64");
    }
    let call_constructors_addr, get_soname
    let symbols = linker.enumerateSymbols();
    for (let index = 0; index < symbols.length; index++) {
        let symbol = symbols[index];
        if (symbol.name === "__dl__ZN6soinfo17call_constructorsEv") {
            call_constructors_addr = symbol.address;
        } else if (symbol.name === "__dl__ZNK6soinfo10get_sonameEv") {
            get_soname = new NativeFunction(symbol.address, "pointer", ["pointer"]);
        }
    }
    console.log(call_constructors_addr)
    var listener = Interceptor.attach(call_constructors_addr, {
        onEnter: function (args) {
            console.log("hooked call_constructors")
            var module = Process.findModuleByName("libmsaoaidsec.so")
            if (module != null) {
                Interceptor.replace(module.base.add(0x1c544), new NativeCallback(function () {
                    console.log("0x1c544:替换成功")
                }, "void", []))
                Interceptor.replace(module.base.add(0x1b8d4), new NativeCallback(function () {
                    console.log("0x1b8d4:替换成功")
                }, "void", []))
                Interceptor.replace(module.base.add(0x26e5c), new NativeCallback(function () {
                    console.log("0x26e5c:替换成功")
                }, "void", []))
                listener.detach()
            }

        },
    })
}

function main1(){
    // 过简单的vpn检测
    main()
    // find_so()
}

main1()



