/*
* 中国民族报app
* 直接使用小黄鸟就行  flutter 开发的app
* */

console.log("frida start into minzubao ...")

//  frida -U --no-pause -f com.trs.mzb -l minzubao.js
function yangshipin() {
    Java.perform(function () {
        function hook_ssl_verify_result(address) {
            console.log("start to handler")
            Interceptor.attach(address, {
                onEnter: function(args) {
                    console.log("Disabling SSL validation")
                },
                onLeave: function(retval) {
                    console.log("Retval: " + retval);
                    retval.replace(0x1);
                }
            });
        }

        var m = Process.findModuleByName("libflutter.so");
        // var pattern = "2d e9 f0 4f a3 b0 82 46 50 20 10 70";
        var pattern = "FF 03 05 D1 FD 7B 0F A9 FA 67 10 A9";
        var res = Memory.scan(m.base, m.size, pattern, {
                onMatch: function(address, size){
                    console.log('[+] ssl_verify_result found at: ' + address.toString());
                    hook_ssl_verify_result(address);
                },
                onError: function(reason){
                    console.log('[!] There was an error scanning memory');
                },
                onComplete: function() {
                    console.log("All done")
                }
        });
    });
}

setImmediate(function() {
    setTimeout(yangshipin, 8000);
});


function disablePinning() {
    var address = Module.findBaseAddress('libflutter.so').add(0x5873D4);
    console.log("[*] Disabling SSL pinning")
    Interceptor.attach(address, {
        onEnter: function (args) {
            console.log("Disabling SSL validation")
        },
        onLeave: function (retval) {
            console.log("Retval: " + retval)
            retval.replace(0x1);
        }
    });
}











