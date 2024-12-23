/*
adb forward tcp:27042 tcp:27042
adb forward tcp:27043 tcp:27043

frida -U -f com.taobao.taobao  -l taobao.js


adb forward tcp:27042 tcp:27042
adb forward tcp:27043 tcp:27043

frida -U -f com.taobao.taobao  -l taobao.js
frida -H 127.0.0.1:8080 -f com.taobao.taobao  -l taobao.js
frida -H 127.0.0.1:8080 -f com.tmall.wireless  -l taobao.js
* */
Java.perform(function () {
    var enableSpdy = false;
    var SwitchConfig = Java.use('mtopsdk.mtop.global.SwitchConfig');

    var instance = SwitchConfig.getInstance();
    instance.setGlobalSpdySslSwitchOpen(enableSpdy);
    instance.setGlobalSpdySwitchOpen(enableSpdy);

});

console.log("loaded script");