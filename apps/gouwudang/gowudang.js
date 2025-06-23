
console.log("frida start into lvzhou ...")

// # frida -U  -f com.gwdang.app -l gowudang.js
function gowudang() {
    Java.perform(function other() {
        // let ParamsInterceptor = Java.use("com.gwdang.core.net.interceptors.ParamsInterceptor");
        // ParamsInterceptor["allSign"].implementation = function (map) {
        //     console.log(`ParamsInterceptor.allSign is called: map=${map}`);
        //     let result = this["allSign"](map);
        //     console.log(`ParamsInterceptor.allSign result=${result}`);
        //     return result;
        // };
        //
        let EasyAES = Java.use("com.gwdang.core.util.EasyAES");
        EasyAES["encrypt"].overload('java.lang.String').implementation = function (str) {
            console.log(`EasyAES.encrypt is called: str=${str}`);
            let result = this["encrypt"](str);
            console.log(`EasyAES.encrypt result=${result}`);
            return result;
        };

        let GZIPUtils = Java.use("com.gwdang.core.util.GZIPUtils");
        GZIPUtils["compress"].implementation = function (str) {
            console.log(`GZIPUtils.compress is called: str=${str}`);
            let result = this["compress"](str);
            console.log(`GZIPUtils.compress result=${result}`);
            return result;
        };

        EasyAES["getHash"].overload('java.lang.String', 'java.lang.String').implementation = function (str, str2) {
            console.log(`EasyAES.getHash is called: str=${str}, str2=${str2}`);
            let result = this["getHash"](str, str2);
            console.log(`EasyAES.getHash result=${result}`);
            return result;
        };

        let Md5Utils = Java.use("com.gwdang.core.util.Md5Utils");
        Md5Utils["getVal_UTF8"].implementation = function (str) {
            // console.log(`Md5Utils.getVal_UTF8 is called: str=${str}`);
            console.log("传入字符串为:", str)
            let result = this["getVal_UTF8"](str);
            console.log(`Md5Utils.getVal_UTF8 result=${result}`);
            return result;
        };

        EasyAES["getHash"].overload('java.lang.String', 'java.lang.String').implementation = function (str, str2) {
            console.log(`EasyAES.getHash is called: str=${str}, str2=${str2}`);
            let result = this["getHash"](str, str2);
            console.log(`EasyAES.getHash result=${result}`);
            return result;
        };
    })

}


function f() {
    
}

function call(){
    Java.perform(function (){
        let Md5Utils = Java.use("com.gwdang.core.util.Md5Utils");
        var str0 = 'zzwrPss0F8B0IVSW_arg=wFasi1pUT5RdREpx1yYvvZSOOrtjnCDzLB2RpSYQ3z3bUau+7SK2d2W/XdiBzZqh6IcjhViE49NKyI6NBn+oUccReCWy8P0+CQVWoqMdPURuRDuzBSZM9Y7DK4mJnoSE66L6uyhqnkvdedDjRJgkkNafa/TROjBQdaus4KzIP6AOW/VHBkMB0A0Chf4a0QRsNSsBx8cMsefW68FpxNsIzpZRyob2oVV6Asey9L3oAPMmMN+NbxWCz7gG6erVWSpYj+uv9HZcuT+DL8LPjcB9PUTXvtYKbfRDRopz8RRTt9D/ZAQi1eiNBFwPC8xr/E3fUDG0Msr7rRX4M1VCr1S6MftS+LubzYchmUsjzpimFjt/m86lsiOP0oqNagtwSj7r2vRRT3hKSMW36bWanaMg/6RAF0xmj9nCBSENJ3ir2PnSq8JAQ0u9a9MF+cz0kuhGPkaHQG2nzBXYA+nyJYh0jMdBk6mv/syRaaUBx+J9E46SWEtVzeqvCPyYmICXoGkA9H8P6IgBvFKqFen3ZcQcvURy7zv2jWAejX2wd/pVWm3rgyIXpaWuThMtFRt+d6lXyU9WoscUdyPxlfR7PtMoR1Tf12FiEWPNvgp5idd4W2inFaM9AXF+wCk3IgxyY+Cgiy4duKrSdSGoIP2B8Tz3R5H+kcxRFvgtfHOoJXIeDcXcew0dmfmyqwk04+Pf+V04Vz2WQ8zQ4c2gN65857bfS1oLKZacfIgjeINFvTYJqNQ2H4tquMaqctTuGN4i9Z+ZTQRjLcU04ENap+l/yeVhXX8WMEzJE+aR4GPBdSLgEHmAYsR6ias/mA5eom+09wx5WoY6dA5hRx/OjRPoJIwewIJc+Ctax4Wf7c8cEYfDOdzjTh5m3Cx8Sp9coc6V76u+_channel=XiaoMiMarket_timestamp=1749542652556_tof=1749539548751app_platform=androidapp_version=25052904device=1080*2029dp_id=70115700013-3p=defaultscene=urluniq-id=456816211911099uniq-id2=67cbaf5df5bdeba9wr=1zzwrPss0F8B0IVSW'
        let result = Md5Utils["getVal_UTF8"](str0);
        console.log("res:",result)
    })
}

function call1(){
    Java.perform(function (){
        let Md5Utils = Java.use("com.gwdang.core.util.EasyAES");
        var str0 = 'zzwrP'
        let result = Md5Utils["encrypt"](str0);
        console.log("res:",result)
    })
}


setImmediate(function() {
    setTimeout(gowudang, 5000);
});
