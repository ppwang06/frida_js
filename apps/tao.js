//frida -U -f com.taobao.taobao  -l t11.js
Java.perform(function () {
    var enableSpdy = false;
    var SwitchConfig = Java.use('mtopsdk.mtop.global.SwitchConfig');

    var instance = SwitchConfig.getInstance();
    instance.setGlobalSpdySslSwitchOpen(enableSpdy);
    instance.setGlobalSpdySwitchOpen(enableSpdy);

});

console.log("loaded script");