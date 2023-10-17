/*
* frida14
* 仅在Android 8.1下测试成功，其他版本可能需要重新修改适配
* 原作者: Simp1er
* */

const STD_STRING_SIZE = 3 * Process.pointerSize;

class StdString {
    constructor() {
        this.handle = Memory.alloc(STD_STRING_SIZE);
    }

    dispose() {
        const [data, isTiny] = this._getData();
        if (!isTiny) {
            Java.api.$delete(data);
        }
    }

    disposeToString() {
        const result = this.toString();
        this.dispose();
        return result;
    }

    toString() {
        const [data] = this._getData();
        return data.readUtf8String();
    }

    _getData() {
        const str = this.handle;
        const isTiny = (str.readU8() & 1) === 0;
        const data = isTiny ? str.add(1) : str.add(2 * Process.pointerSize).readPointer();
        return [data, isTiny];
    }
}


function prettyMethod(method_id, withSignature) {
    const result = new StdString();
    Java.api['art::ArtMethod::PrettyMethod'](result, method_id, withSignature ? 1 : 0);
    return result.disposeToString();
}

function readStdString(str) {
    if ((str.readU8() & 1) === 1) { // size LSB (=1) indicates if it's a long string
        return str.add(2 * Process.pointerSize).readPointer().readUtf8String();
    }
    return str.add(1).readUtf8String();
}

function attach(addr) {
    Interceptor.attach(addr, {
        onEnter: function (args) {
            this.arg0 = args[0]; // this
        },
        onLeave: function (retval) {
            var modulemap = new ModuleMap()
            modulemap.update()
            var module = modulemap.find(retval)
            // var string = Memory.alloc(0x100)
            // ArtMethod_PrettyMethod(string, this.arg0, 1)
            if (module != null) {
                console.log('<' + module.name + '> method_name =>',
                    prettyMethod(this.arg0, 1),
                    ',offset=>', ptr(retval).sub(module.base), ',module_name=>', module.name)
            } else {
                console.log('<anonymous> method_name =>', readStdString(string), ', addr =>', ptr(retval))
            }
        }
    });
}

function hook_RegisterNative() {
    var libart = Process.findModuleByName('libart.so')
    var symbols = libart.enumerateSymbols()
    for (var i = 0; i < symbols.length; i++) {
        if (symbols[i].name.indexOf('RegisterNative') > -1 && symbols[i].name.indexOf('ArtMethod') > -1 && symbols[i].name.indexOf('RuntimeCallbacks') < 0) {
            //art::RuntimeCallbacks::RegisterNativeMethod(art::ArtMethod*, void const*, void**)
            attach(symbols[i].address)
        }
    }

}

function main() {
    hook_RegisterNative()
}

setImmediate(main)