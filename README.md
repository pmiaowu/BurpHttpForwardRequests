# 简介

http请求转发酱一个可怜兮兮还不知道自己唯一使命的Burpsuite 转发插件 (°ー°〃)愣住

注意: 该插件只会在以下几个burp模块运行
- Burp Proxy模块
- Burp Repeater模块

此插件最大的作用就是配合作者其他的Burp插件进行漏洞扫描

# 功能

此插件会把所有的“Burp Proxy模块/Burp Repeater模块”请求转发到“Burp Scanner模块”进行扫描

# 安装过程

Jython官网: https://www.jython.org/downloads.html

Jython环境安装包: http://search.maven.org/remotecontent?filepath=org/python/jython-standalone/2.7.0/jython-standalone-2.7.0.jar

![](./readme/images/1.png)
![](./readme/images/2.png)
![](./readme/images/3.png)
![](./readme/images/14.png)
![](./readme/images/6.png)
![](./readme/images/13.png)

# 使用例子

安装完毕以后,任意打开一个url链接就可以了

![](./readme/images/15.png)

例如打开任意一个网站
![](./readme/images/7.png)
![](./readme/images/8.png)
![](./readme/images/9.png)

# 注意项-关于请求不转发的问题

如果你发现一个“Burp Proxy模块请求”第一次可以成功转发到“Burp Scanner模块”,后面都不转发了,请注意这不是Bug!!!,这不是Bug!!!,这不是Bug!!!

这是因为我添加了Url重复检测的判断

你可以查看插件根目录下的“test_logs”文件夹,里面会以你的扫描域名生成一个“xxxx.com-xx年-xx月-xx日.log"

这个log会记录“Burp Proxy模块请求”转发到“Burp Scanner模块”的Url

解决方案:
1. 通过这个插件的Tag来关闭Url重复检测的功能
2. 可以删除对应域名的文件,这样它就会重新转发了

# Url黑名单添加

在根目录你可以看到“black_url.txt”文件,打开此文件,一行一域名添加即可

过滤某个域名: www.domain.com

过滤某个域名的全部子域名: *.domain.com

每个在“black_url.txt”文件里面的url此插件都不会进行转发

![](./readme/images/4.png)

# Url白名单添加

白名单里面如果有数据,那么此插件就只会转发白名单里面的域名请求

注意: 如果黑名单与白名单的域名冲突的话,那么黑名单的执行优先级更高!!!!!

注意: 如果黑名单与白名单的域名冲突的话,那么黑名单的执行优先级更高!!!!!

注意: 如果黑名单与白名单的域名冲突的话,那么黑名单的执行优先级更高!!!!!

![](./readme/images/11.png)
只转发某个域名: www.domain.com
只转发某个域名的全部子域名: *.domain.com

注意: 域名不需要填写 http:// 或是 https://

# Tag面板配置项

![](./readme/images/5.png)
![](./readme/images/10.png)
![](./readme/images/11.png)
![](./readme/images/12.png)

# Url调试功能添加

新参数: is_burp_debug=True/False
请求方法: Get

功能: 如果您想调试某个url但是又不想此插件转发请求出去可以通过此功能实现

## Url调试功能例子:

例如说我现在有一个url: https://github.com/pmiaowu

以前我们一访问他请求就转发到“Burp Scanner模块”了

现在您可以输入: https://github.com/pmiaowu?is_burp_debug=True

那么此请求就不会转发了 :)

# 插件基本使用方法

## url重复验证功能说明

如果你发现一个“Burp Proxy模块请求”第一次可以成功转发到“Burp Scanner模块”,后面都不转发了,请注意这不是Bug!!!,这不是Bug!!!,这不是Bug!!!

转发插件默认启动Url重复检测的判断

你可以查看插件根目录下的“test_logs”文件夹,里面会以你的扫描域名生成一个“xxxx.com-xx年-xx月-xx日.log"

这个log会记录“Burp Proxy模块请求”转发到“Burp Scanner模块”的Url

如果你想要重新转发相同的请求的话, 有三个方法



```
方法一-临时有效的

进入“test_logs”文件夹 删除里面的内容
```
![](./readme/images/16.png)



```
方法二-临时有效的

进入 http请求转发插件-基本设置 这个tag

里面有个 “是否启动url重复验证” 把那个勾取消即可
```
![](./readme/images/17.png)



```
方法三-永久有效的

打开 “config\forwardRequests.py” 这个文件

找到一个配置 “URL_REPEATED_VERIFY” 修改为 False 即可
```
![](./readme/images/18.png)

## 白名单域名功能-设置方法

注意: 域名不需要填写 http:// 或是 https://

### 转发全部链接-设置方法

![](./readme/images/15.png)

这样每个请求就都会进行转发了

### 转发某个域名请求-设置方法

如果想要每个域名的请求进行转发, 那也是可以的

例子一: 转发 www.baidu.com 的请求设置方法如下
![](./readme/images/19.png)



例子二: 转发 所有baidu.com 的请求设置方法如下
![](./readme/images/20.png)


例子三: 转发 ip 的请求设置方法如下
![](./readme/images/21.png)

### 转发某个链接-设置方法

假设我们现在在 Burp Repeater模块 有一个请求想要进行转发, 那么可以这样转发
![](./readme/images/22.png)

