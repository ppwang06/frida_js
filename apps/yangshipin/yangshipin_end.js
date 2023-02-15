console.log("frida start into yangshipin ...")

//  frida -U --no-pause -f com.cctv.yangshipin.app.androidp -l yangshipin.js
function yangshipin() {
    Java.perform(function other() {

        // 打印调用方法堆栈
        function showStack() {
            let Throwable = Java.use("java.lang.Throwable");
            let stackTraceString = Java.use("android.util.Log").getStackTraceString(Throwable.$new())
            console.log(stackTraceString);
        }

        let tls_check = Java.use("okhttp3.internal.tls.OkHostnameVerifier")
        let new_check = Java.use("okhttp3.CertificatePinner")
        let conn = Java.use("okhttp3.internal.connection.RealConnection")
        let ver2 = Java.use("b.h0.k.d")

        // tls_check.verifyHostname.overload('java.lang.String', 'java.security.cert.X509Certificate').implementation = function (str, Cert) {
        //     showStack()
        //     let result = this.verifyHostname(str, Cert);
		// 	console.log("verifyHostname", result)
        //     return true;
        // }
        // tls_check.verifyHostname.overload('java.lang.String', 'java.lang.String').implementation = function (str4, str3) {
        //     showStack()
        //     let result = this.verifyHostname(str4, str3);
		// 	console.log("verifyHostname2", result)
        //     return true;
        // }
        //
        // tls_check.verifyIpAddress.overload('java.lang.String', 'java.security.cert.X509Certificate').implementation = function (str1, Cert1) {
        //     showStack()
        //     let result = this.verifyIpAddress(str1, Cert1);
		// 	console.log("verifyIpAddress", result)
        //     return true;
        // }
        //
        tls_check.verify.overload('java.lang.String', 'javax.net.ssl.SSLSession').implementation = function (str2, session) {
            // showStack()
            let result = this.verify(str2, session);
            console.log("verify", result)
            return true;
        }

        new_check.check.overload('java.lang.String', 'java.util.List') .implementation = function (str5, cert_list) {
            // showStack()
            console.log("str5", str5)
            console.log("cert_list", cert_list)
            let result = this.check(str5, cert_list);
			console.log("verify new_check", "result")
            return;
        }

        conn.connectTls.implementation = function (connectionSpecSelector) {
            // showStack()
            let result1 = this.connectTls(connectionSpecSelector);
			console.log("connectTls", result1)
            return result1;
        }
        // ver2.verify.overload('java.lang.String', 'javax.net.ssl.SSLSession').implementation = function (str6, cert) {
        //     showStack()
        //     let result = this.verify(str6, cert);
		// 	console.log("verify222222 new_check", result)
        //     return true;
        // }
    })
}

setImmediate(function() {
    setTimeout(yangshipin, 5000);
});