import sys
import frida

device = None
app = "com.smile.gifmaker"
jscode = """
'use strict';

Java.perform(function(){
    var t1 = Java.use("com.kuaishou.aegon.okhttp.CronetInterceptorConfig");
      t1.a.overload('java.lang.String', '[Ljava.lang.String;', 'boolean').implementation = function(a1,a2,a3){
           return false;
            };      
            
               var t2 = Java.use("com.kuaishou.dfp.a.d");
      t2.a.overload('com.kuaishou.dfp.a.z', 'com.kuaishou.dfp.a.a.a.a.a.a.b', 'com.kuaishou.dfp.d.k', 'boolean', 'boolean').implementation = 
      function(a1,a2,a3,a4,a5){
      console.log(a2.toString());
      console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()));
           return this.a(a1,a2,a3,a4,a5);
            };    
});
"""


def launch_app():
    global device
    device = frida.get_remote_device()
    print(device)
    device.on("spawn-added", spawn_added)
    device.enable_spawn_gating()
    print("Enabled spawn gating")

    pid = device.spawn(app)
    process = device.attach(pid)
    script = process.create_script(jscode)
    script.on("message", on_message)
    script.load()
    device.resume(pid)

    print("wait")
    line = None
    while line != "quit":
        line = sys.stdin.readline().strip()
        try:
            device.get_process(app)
        except frida.ProcessNotFoundError:
            return
    process.detach()
    device.kill(pid)


def spawn_added(spawn):
    # print("spawn_added:", spawn)
    if spawn.identifier.startswith(app):
        session = device.attach(spawn.pid)
        script = session.create_script(jscode)
        script.on("message", on_message)
        script.load()
    device.resume(spawn.pid)


def on_message(message, data):
    if message["type"] == "send":
        print("[*] {0}".format(message["payload"]))
    else:
        print("on_message", message, data)


import os


def main():
    os.system("adb shell rm -rf /storage/emulated/0/.com.smile.gifmaker/.rrssuu")
    os.system(
        "adb shell rm -rf /storage/emulated/0/.com.smile.gifmaker/storage/emulated/0/Android/data/com.smile.gifmaker/files/.rrssuu")

    launch_app()


if __name__ == '__main__' and '__file__' in globals():
    main()
