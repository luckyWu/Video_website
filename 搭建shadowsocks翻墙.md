# 搭建shadowsocks翻墙

```
安装必要组建
centos执行 yum install build-essential autoconf libtool openssl-devel gcc -y
debian执行 apt-get install build-essential autoconf libtool libssl-dev gcc -y

安装git
centos执行 yum install git -y
debian执行 apt-get install git -y
装完了执行 git --version检查是否安装成功。








git clone -b master https://github.com/Flyzy2005/ss-fly
```

![img](https://www.textarea.com/image/8621c5a4c526b42cff6811f60abd3180.png!w1920!h1080!t.png)2.运行搭建ss脚本代码

```
ss-fly/ss-fly.sh -i password 1024
```

 安装shadowsocks

打开shell，使用VPS服务商提供的root用户和密码SSH登录VPS。然后执行如下命令：

#### CentOS:

```
yum install python-setuptools && easy_install pip
pip install shadowsocks
```

#### Debian/Ubuntu:

```
apt-get install python-pip
pip install shadowsocks
```

``

shadowsocks就安装好了。

有时Ubuntu会遇到第一个命令安装python-pip时找不到包的情况。pip官方给出了一个安装脚本，可以自动安装pip。先下载脚本，然后执行即可：

```
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
```

或者使用easy_install安装：

```
sudo easy_install shadowsocks
```

### 编写配置文件

shadowsocks启动时的参数，如服务器端口，代理端口，登录密码等，可以通过启动时的命令行参数来设定，也可以通过json格式的配置文件设定。推荐使用配置文件，方便查看和修改。

用vi新建一个配置文件：

```
vi /etc/shadowsocks.json
```

然后输入如下内容：

```
{ 
   "server":"0.0.0.0", 
   "server_port":25, 
   "local_address": "127.0.0.1", 
   "local_port":1080, 
   "password":"mypassword",
   "timeout":300, 
   "method":"aes-256-cfb", 
   "fast_open": false
}
```

简单说明一下各个配置项：

#### server

你的VPS服务器的IP地址

#### server_port

你的shadowsocks服务端口。一般可以填一个1025到49151之间的数字。不过如果使用一个知名端口，比如25（电子邮件）、21（FTP），“可能”会更安全，因为GFW对这些基础互联网服务下手的可能性似乎会小一些。注意不要和你的VPS上已经有的服务冲突。

#### local_address

本地IP地址，作为服务器使用的时候可以不用关注，填127.0.0.1即可。

#### local_port

本地端口，也不用关注。

#### password

你的shadowsocks服务密码，客户端连接时需要填写的。

#### timeout

超时时间，如果当心网络不好可以设置大一点。

#### method

加密方式，建议填写`aes-256-cfb`，安全性比较高。

#### fast_open

在Ubuntu上建议填True。

填好以后保存退出。

### 启动shadowsocks

如果已经写好了配置文件，启动shadowsocks服务器的命令如下：

```
ssserver -c /etc/shadowsocks.json
```

后台启动和停止shadowsocks服务器：

```
ssserver -c /etc/shadowsocks.json -d start
ssserver -c /etc/shadowsocks.json -d stop
```

shadowsocks的日志保存在

```
/var/log/shadowsocks.log
```