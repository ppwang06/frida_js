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

    var NetworkParams = Java.use('X.SYN');
    NetworkParams.LIZ.overload('android.content.Context', 'org.json.JSONObject', 'X.SYQ').implementation = function (a1, a2,a3) {
        console.log(a2.toString());
        var x = this.LIZ(a1, a2,a3);
        return x;
    };

    });

console.log("loaded script");