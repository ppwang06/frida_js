/*
* 13.1.0   eid参数  hook测试
*
*
* ./wang_server16 -l 127.0.0.1:8089
* adb forward tcp:8089 tcp:8089
* frida -H 127.0.0.1:8089 -f com.jingdong.app.mall -l hook_jd_eid.js
* eid参数生成位置
*
* eid数据为： eidAe6b7412211l5382431490f7d1577554b8fadb8b7ef6eabddf9432qzcwA0vjTIS4ALkvYvCnLp95Gqp7Bk3xjz+9KQRQo0wki9fwEZBDJvxjHQA1a31b0966457b5a342f79fc55f958a3b
* eid数据为： eidAe6b7412211l5382431490f7d1577554b8fadb8b7ef6eabddf9432qzcwA0vjTIS4ALkvYvCnLp95Gqp7Bk3xjz+9KQRQo0wki9fwEZBDJvxjHQA  删除  1a31b0966457b5a342f79fc55f958a3b
* 去除最后32为即为eid参数
* */
function hook_java() {
    Java.perform(function other() {
        // eid
        let head = Java.use("com.jdcn.risk.cpp.LoadDoor")
        head.getEid.implementation = function (str) {
            let result = this.getEid(str);
            console.log("eid数据为：", result)
            return result
        }

    })
}

//主动调用
function call_eid() {
	let loadDoor = Java.use("com.jdcn.risk.cpp.LoadDoor")
	const currentApplication = Java.use("android.app.ActivityThread").currentApplication();
	const context = currentApplication.getApplicationContext();
	const eid = loadDoor.getEid(context);
	console.log("eid:", eid)
	return eid
}

function main_jdgs() {
    hook_java()
}

setTimeout(main_jdgs)