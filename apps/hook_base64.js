/**
 * Java层标准算法hook
 */

Java.perform(function () {
    /**
     打印堆栈
     */
    function showStack() {
        let Throwable = Java.use("java.lang.Throwable");
        let stackTraceString = Java.use("android.util.Log").getStackTraceString(Throwable.$new())
        console.log(stackTraceString);
    }

    let ByteString = Java.use("com.android.okhttp.okio.ByteString");

    /**
     * 字节数组转为Base64
     */
    function toBase64(tag, data) {
        console.log(tag + " Base64:" + ByteString.of(data).base64());
    }

    /**
     * 字节数组转为16进制
     */
    function toHex(tag, data) {
        console.log(tag + " Hex:" + ByteString.of(data).hex());
    }

    /**
     * 字节数组转为明文
     */
    function toUtf8(tag, data) {
        console.log(tag + " Utf8:" + ByteString.of(data).utf8());
    }

    /**
     * 打印字节数组对应的输出数据
     */
    function printData(tag, data) {
        toBase64(tag, data);
        toHex(tag, data);
        toUtf8(tag, data);
    }


    /***
     * 消息摘要算法hook
     * update 压入数据
     * digest 返回加密结果
     */
    function hookMessageDigest() {
        let MessageDigest = Java.use("java.security.MessageDigest");
        MessageDigest.update.overload('byte').implementation = function (b) {
            showStack();
            console.log("MessageDigest.update.overload('byte') is called!");
            let result = this.update.apply(this, arguments);
            let algorithm = this.getAlgorithm();
            printData(algorithm + " update param", Java.array('byte', [b]))
            console.log("============================================================");
            return result;
        }
        MessageDigest.update.overload('[B').implementation = function (byteArr) {
            showStack();
            console.log("MessageDigest.update.overload('[B') is called!");
            let result = this.update.apply(this, arguments);
            let algorithm = this.getAlgorithm();
            printData(algorithm + " update param", byteArr);
            console.log("============================================================");
            return result;
        }
        MessageDigest.digest.overload().implementation = function () {
            showStack();
            console.log("MessageDigest.digest.overload() is called!");
            let result = this.digest.apply(this, arguments);
            let algorithm = this.getAlgorithm();
            printData(algorithm + " digest result", result);
            console.log("============================================================");
            return result;
        }
        MessageDigest.digest.overload('[B').implementation = function (byteArr) {
            showStack();
            console.log("MessageDigest.digest.overload('[B') is called!");
            let result = this.digest.apply(this, arguments);
            let algorithm = this.getAlgorithm();
            printData(algorithm + " digest param", byteArr);
            printData(algorithm + " digest result", result);
            console.log("============================================================");
            return result;
        }

        MessageDigest.digest.overload('[B', 'int', 'int').implementation = function (byteArr, start, length) {
            showStack();
            console.log("MessageDigest.digest.overload('[B', 'int', 'int') is called!");
            let result = this.digest.apply(this, arguments);
            let algorithm = this.getAlgorithm();
            printData(algorithm + " digest param", byteArr);
            printData(algorithm + " digest result", result);
            console.log("============================================================" + "开始位置：" + start + " 截取长度：" + length);
            return result;
        }
    }

    /**
     * Mac算法hook
     * 1.init 初始化，秘钥
     * 2.update 压入数据
     * 3.doFinal 加密
     */
    function hookMac() {
        let Mac = Java.use("javax.crypto.Mac");

        Mac.init.overload('java.security.Key').implementation = function (key) {
            showStack();
            console.log("Mac.init.overload('java.security.Key') is called!");
            let result = this.init.apply(this, arguments);
            let algorithm = this.getAlgorithm();
            printData(algorithm + " init key", key.getEncoded())
            console.log("============================================================");
            return result;
        }

        Mac.update.overload('byte').implementation = function (b) {
            showStack();
            console.log("Mac.update.overload('byte') is called!");
            let result = this.update.apply(this, arguments);
            let algorithm = this.getAlgorithm();
            printData(algorithm + " update param", Java.array('byte', [b]))
            console.log("============================================================");
            return result;
        }
        Mac.update.overload('[B').implementation = function (byteArr) {
            showStack();
            console.log("Mac.update.overload('[B') is called!");
            let result = this.update.apply(this, arguments);
            let algorithm = this.getAlgorithm();
            printData(algorithm + " update param", byteArr)
            console.log("============================================================");
            return result;
        }
        Mac.update.overload('[B', 'int', 'int').implementation = function (byteArr, start, length) {
            showStack();
            console.log("Mac.update.overload('[B', 'int', 'int') is called!");
            let result = this.update.apply(this, arguments);
            let algorithm = this.getAlgorithm();
            printData(algorithm + " update param", byteArr)
            console.log("============================================================" + "开始位置：" + start + " 截取长度：" + length);
            return result;
        }
        Mac.doFinal.overload().implementation = function () {
            showStack();
            console.log("Mac.doFinal.overload() is called!");
            let result = this.doFinal.apply(this, arguments);
            let algorithm = this.getAlgorithm();
            printData(algorithm + " doFinal result", result)
            console.log("============================================================");
            return result;
        }
    }

    /**
     * DES,DESEde,AES,RSA
     * 1.init 加密类型,key,iv
     * 2.donFinal压入数据，得到结果 update压入结果有问题
     */
    function hookCipher() {
        function printResult(cipherObj, result, args) {
            let algorithm = cipherObj.getAlgorithm();
            let mode;

            if (cipherObj.opmode.value === 1) {
                mode = "加密";
            } else {
                mode = "解密";
            }

            console.log(algorithm + " mode:", mode);
            if (cipherObj.getParameters() != null) {
                printData(algorithm + " key", cipherObj.getParameters().getEncoded());
                printData(algorithm + " iv", cipherObj.getIV());
            }
            printData(algorithm + " doFinal param", args[0]);
            printData(algorithm + " doFinal result", result);
            console.log("============================================================");

        }

        let Cipher = Java.use("javax.crypto.Cipher");
        // 不常用重载，打印调用即可，根据堆栈信息在具体去看
        // init暂时注释
        Cipher.init.overload('int', 'java.security.cert.Certificate', 'java.security.SecureRandom').implementation = function (key) {
            showStack();
            console.log("Cipher.init.overload('int', 'java.security.cert.Certificate', 'java.security.SecureRandom') is called!");
            let result = this.apply(this, arguments);
            return result;
        }
        Cipher.init.overload('int', 'java.security.Key', 'java.security.AlgorithmParameters', 'java.security.SecureRandom').implementation = function (key) {
            showStack();
            console.log("Cipher.init.overload('int', 'java.security.Key', 'java.security.AlgorithmParameters', 'java.security.SecureRandom') is called!");
            let result = this.apply(this, arguments);
            return result;
        }

        // ECB模式，不带iv
        Cipher.init.overload('int', 'java.security.Key', 'java.security.SecureRandom').implementation = function () {
            showStack();
            console.log("Cipher.init.overload('int', 'java.security.Key', 'java.security.SecureRandom') is called!");
            let result = this.init.apply(this, arguments);
            let algorithm = this.getAlgorithm();
            let mode;
            if (arguments[0] === 1) {
                mode = "加密";
            } else {
                mode = "解密";
            }
            console.log(algorithm + " init mode:" + mode);
            try {
                // RSA使用私钥调用getEncoded() 会报错，异常捕获，具体逻辑，根据堆栈，去APP分析
                printData(algorithm + " init key", arguments[1].getEncoded());
            } catch (e) {
                console.log(e);
            }
            console.log("============================================================");
            return result;
        }

        // CBC模式，带iv
        Cipher.init.overload('int', 'java.security.Key', 'java.security.spec.AlgorithmParameterSpec', 'java.security.SecureRandom').implementation = function () {
            showStack();
            console.log("Cipher.init.overload('int', 'java.security.Key', 'java.security.spec.AlgorithmParameterSpec', 'java.security.SecureRandom') is called!");
            let result = this.init.apply(this, arguments);
            let algorithm = this.getAlgorithm();
            let ivParameterSpecObj = Java.cast(arguments[2], Java.use("javax.crypto.spec.IvParameterSpec"));
            let mode;
            if (arguments[0] === 1) {
                mode = "加密";
            } else {
                mode = "解密";
            }
            console.log(algorithm + " init mode:" + mode);
            printData(algorithm + " init key", arguments[1].getEncoded());
            printData(algorithm + " init iv", ivParameterSpecObj.getIV());
            console.log("============================================================");
            return result;
        }

        Cipher.doFinal.overload().implementation = function () {
            showStack();
            console.log("Cipher.doFinal.overload() is called!");
            let result = this.doFinal.apply(this, arguments);
            printResult(this, result, arguments);
            return result;
        }
        Cipher.doFinal.overload('[B').implementation = function () {
            showStack();
            console.log("Cipher.doFinal.overload('[B') is called!");
            let result = this.doFinal.apply(this, arguments);
            printResult(this, result, arguments);
            return result;
        }
        Cipher.doFinal.overload('[B', 'int').implementation = function () {
            showStack();
            console.log("Cipher.doFinal.overload('[B', 'int') is called!");
            let result = this.doFinal.apply(this, arguments);
            printResult(this, result, arguments);
            return result;
        }
        Cipher.doFinal.overload('[B', 'int', 'int').implementation = function () {
            showStack();
            console.log("Cipher.doFinal.overload('[B', 'int', 'int') is called!");
            let result = this.doFinal.apply(this, arguments);
            printResult(this, result, arguments);
            return result;
        }
        Cipher.doFinal.overload('[B', 'int', 'int', '[B').implementation = function () {
            showStack();
            console.log("Cipher.doFinal.overload('[B', 'int', 'int', '[B') is called!");
            let result = this.doFinal.apply(this, arguments);
            printResult(this, result, arguments);
            return result;
        }
        Cipher.doFinal.overload('[B', 'int', 'int', '[B', 'int').implementation = function () {
            showStack();
            console.log("Cipher.doFinal.overload('[B', 'int', 'int', '[B', 'int') is called!");
            let result = this.doFinal.apply(this, arguments);
            printResult(this, result, arguments);
            return result;
        }
    }

    /**
     * 签名算法hook
     * 私钥
     */
    function hookSignature() {
        let Signature = Java.use("java.security.Signature");
        Signature.initSign.overload('java.security.PrivateKey').implementation = function () {
            showStack();
            console.log("Signature.initSign.overload('java.security.PrivateKey') is called!");
            let result = this.initSign.apply(this, arguments);
            let algorithm = this.getAlgorithm();
            try {
                // RSA使用Hex编码的私钥调用getEncoded() 会报错，异常捕获，具体逻辑，根据堆栈，去APP分析
                printData(algorithm + " init key", arguments[0].getEncoded());
            } catch (e) {
                console.log(JSON.stringify(arguments[0]) + "|" + e);
            }
            console.log("============================================================");
            return result;
        }
        Signature.update.overload('byte').implementation = function () {
            showStack();
            console.log("Signature.update.overload('byte') is called!");
            let result = this.update.apply(this, arguments);
            let algorithm = this.getAlgorithm();
            printData(algorithm + " update param", Java.array('byte', [b]))
            console.log("============================================================");
            return result;
        }
        Signature.update.overload('[B', 'int', 'int').implementation = function () {
            showStack();
            console.log("Signature.update.overload('[B', 'int', 'int') is called!");
            let result = this.update.apply(this, arguments);
            let algorithm = this.getAlgorithm();
            printData(algorithm + " update param", arguments[0]);
            console.log("============================================================");
            return result;
        }
        Signature.sign.overload().implementation = function () {
            showStack();
            console.log("Signature.sign.overload() is called!");
            let result = this.sign.apply(this, arguments);
            let algorithm = this.getAlgorithm();
            printData(algorithm + " sign result", result);
            console.log("============================================================");
            return result;
        }
        Signature.sign.overload('[B', 'int', 'int').implementation = function () {
            showStack();
            console.log("Signature.sign.overload('[B', 'int', 'int') is called!");
            let result = this.sign.apply(this, arguments);
            let algorithm = this.getAlgorithm();
            printData(algorithm + " sign param", arguments[0]);
            printData(algorithm + " sign result", result);
            console.log("============================================================");
            return result;
        }
    }

    /**
     * Base64hook
     */
    function hookBase64() {
        let Base64 = Java.use("android.util.Base64");
        Base64.encodeToString.overload('[B', 'int').implementation = function () {
            let result = this.encodeToString.apply(this, arguments);
            printData("Base64 param", arguments[0]);
            console.log("-------------------------------");
            console.log("Base64 result:" + result);
            console.log("============================================================");
            return result;
        }
    }

    // 消息摘要算法hook
    hookMessageDigest();
    // Mac算法hook
    hookMac();
    // hookCipher
    hookCipher();
    // 数据签名算法hook
    hookSignature();
    // hookBase64编码
    hookBase64();

})



