/*
* 抖音抓包
* com.ss.android.ugc.aweme
* 可以用来抖音抓包 但手机app显示加载失败 点击重试
* frida -U --no-pause -f com.ss.android.ugc.aweme -l douyin.js
* */
setImmediate(function() {
    Java.perform(function() {
        var targetClass='org.chromium.CronetClient';
        var methodName='tryCreateCronetEngine';
        var gclass = Java.use(targetClass);
        gclass[methodName].overload('android.content.Context','boolean','boolean','boolean','boolean','java.lang.String','java.util.concurrent.Executor','boolean').implementation = function(arg0,arg1,arg2,arg3,arg4,arg5,arg6,arg7) {

        }
    })
})