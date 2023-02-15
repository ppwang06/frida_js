import sys
import frida

device = None
app = "com.dragon.read"
app = "com.ss.android.ugc.aweme"

jscode = """
'use strict';

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
"""


def launch_app():
    global device
    device = frida.get_remote_device()
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
    print("spawn_added:", spawn)
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


def main():
    launch_app()


if __name__ == '__main__' and '__file__' in globals():
    main()
