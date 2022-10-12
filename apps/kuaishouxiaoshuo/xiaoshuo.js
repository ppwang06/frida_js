/*
* 快手免费小说  __sig3
* com.kuaishou.kgx.novel
* frida -U --no-pause -f com.kuaishou.kgx.novel -l xiaoshuo.js
*
* 48 位的 __sig3 返回值在so层 暂时无法解决
* 最后 类似base64结果已结局
* return Base64.encodeToString(bArr, 10).replace('+', '-').replace('/', '_').replaceAll("=", "");
*
* */

setImmediate(function() {
    setTimeout(delay_load_injection, 5000);
});

//14055656d88a984e435c5f5ebdc9ffe251510225404d4355
function delay_load_injection() {
    Java.perform(function kuaishouxiaoshuo() {

        // 打印调用方法堆栈
        function showStack() {
            let Throwable = Java.use("java.lang.Throwable");
            let stackTraceString = Java.use("android.util.Log").getStackTraceString(Throwable.$new())
            console.log(stackTraceString);
        }

        // 48 __sig
        console.log("Frida start to update  method")
        let head = Java.use("com.kuaishou.android.security.KSecurity")
        head.atlasSign.implementation = function (z) {
            console.log("传入字符串为:", z)
            let result = this.atlasSign(z);
            console.log("result--->：", result)
            return result
        }

        // 快手小说 最后 base64的结果
        // var ffSignCls =  Java.use("k.w.e.a1.t");
        // ffSignCls.a.overload('java.lang.String', 'java.lang.String', 'java.util.Map').implementation = function(a,b,c){
        //     var rc = this.a(a,b,c);
        //     console.log("a = " + a);
        //     console.log("b = " + b);
        //     console.log("c = " + c.entrySet().toArray());
        //     console.log(">>> rc = " + rc);
        //     return rc;
        // }

         // 最后一步的运算结果
        // var ccSignCls =  Java.use("k.w.e.i1.p1");
        // ccSignCls.a.overload('[B').implementation = function(barr){
        //     console.log("转base64前的 []byte" + barr)
        //     var rwc = this.a(barr);
        //     console.log("ccc -->result = " + rwc);
        //     return rwc;
        // }

        // 生成的salt 值
        // var ddSignCls =  Java.use("k.w.e.i1.j2");
        // ddSignCls.e.implementation = function(){
        //     var rcwc = this.e();
        //     console.log("result toString() = " + rcwc);
        //     return rcwc;
        // }

        // salt的十进制
        // var eeSignCls =  Java.use("com.google.common.primitives.Longs");
        // eeSignCls.toByteArray.implementation = function(j2){
        //     console.log("j2--->" + j2)
        //     var rcwcd = this.toByteArray(j2);
        //     console.log("j2 result--->" + rcwcd)
        //     return rcwcd;
        // }

        //
        // 生成 48 走的c 函数
        // var sig_48 =  Java.use("com.kuaishou.android.security.internal.crypto.e");
        // sig_48.c.implementation = function(str, z, str2){
        //     console.log("str--->" + str)
        //     console.log("z--->" + z)
        //     console.log("str2--->" + str2)
        //     let sigResult = this.b(str, z, str2);
        //     console.log("sigResult result--->" + sigResult)
        //     return sigResult;
        // }


    })
}

