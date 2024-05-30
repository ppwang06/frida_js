//frida -U -f com.taobao.taobao  -l tao.js
Java.perform(function () {
    var enableSpdy = false;
    var SwitchConfig = Java.use('mtopsdk.mtop.global.SwitchConfig');

    var instance = SwitchConfig.getInstance();
    instance.setGlobalSpdySslSwitchOpen(enableSpdy);
    instance.setGlobalSpdySwitchOpen(enableSpdy);

});

console.log("loaded script");