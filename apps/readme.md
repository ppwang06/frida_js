
```shell
# 查看当前手机运行APP
adb shell dumpsys window | findstr mCurrentFocus

# frida 端口转发
adb forward tcp:27042 tcp:27042
adb forward tcp:27043 tcp:27043

更名: 将frida-server改名为other-server
改端口: 手机里面用 other-server -l 127.0.0.1:8080 来启动
电脑里面先映射 adb forward tcp:8080 tcp:8080 
然后启动 frida -H 127.0.0.1:8080 -l jd.js com.jingdong.app.mall
或者先启动京东 frida -H 127.0.0.1:8080 -l jd.js 京东
```
###### APP记录
###### frida 检测
- `京东`
- `无线苏州`(改名字不好使)

###### flutter 开发的app
- `中国民族报`
- `凯旋`(数字藏品)

###### 抓包未解决的
- `央视频`
