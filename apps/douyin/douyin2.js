//可以用来抖音抓包
//frida -U --no-pause -f com.ss.android.ugc.aweme -l douyin.js
Java.perform(function(){

    var ba = Java.use('org.chromium.CronetClient');
    if (ba){
        console.log("2 find class");
        ba.tryCreateCronetEngine.implementation = function(){
            console.log("use http");
            }
        }

    });

console.log("loaded script");