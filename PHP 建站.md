# PHP 建站

1.查看centos版本

```
cat /etc/redhat-release
```

2.获取阿里镜像

```
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo 
```

**Apache服务的搭建与配置**

3.安装httpd

```
yum -y install httpd
```

4.查看httpd版本

```
rpm -qa | grep httpd
```

5.安装成功后，会产生下面两个文件 

```
/etc/httpd/conf/httpd.conf  # 主配置文件
/var/www/html                   # 默认网站家目录
```

6./etc/httpd/conf/httpd.conf主要参数

```
 31 serverRoot "/etc/httpd"           # 存放配置文件的目录
 42 Listen 80           # Apache服务监听端口
 66 User apache     # 子进程的用户
 67 Group apache   # 子进程的组
 86 ServerAdmin root@localhost  # 设置管理员邮件地址
119 DocumentRoot "/var/www/html" --网站家目录
# 设置DocumentRoot指定目录的属性
131 <Directory "/var/www/html">   # 网站容器开始标识
144 Options Indexes FollowSymLinks   # 找不到主页时，以目录的方式呈现，并允许链接到网站根目录以外
151 AllowOverride None                # none不使用.htaccess控制,all允许
156 Require all granted                 # granted表示运行所有访问，denied表示拒绝所有访问
157 </Directory>    # 容器结束
164 DirectoryIndex index.html       # 定义主页文件，当访问到网站目录时如果有定义的主页文件，网站会自动访问
316 AddDefaultCharset UTF-8      # 字符编码，如果中文的话，有可能需要改为gb2312或者gbk,因你的网站文件的默认编码而异
```

7.启动apache

```
systemctl start httpd.service
systemctl status httpd.service         --查看httpd服务是否启动

//systemctl stop httpd.service #停止
//systemctl restart httpd.service #重启
```

8.浏览器输入服务器ip地址

```
显示Testing 123
```

9.建立网站主页,在网站根目录下建立一个主页文件 

```
/var/www/html/index.html
```

**php安装和配置**

----

1.配置yum源

```
rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm 

rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
```

2.安装

```
yum -y install php72w php72w-cli php72w-common php72w-devel php72w-embedded php72w-fpm php72w-gd php72w-mbstring php72w-mysqlnd php72w-opcache php72w-pdo php72w-xml
```

3.查看版本

```
php  -v
```

4./var/www/html/路径下新建index.php并写入内容,重启apache

```
<?php
echo "Hello World!";
?>
#浏览器访问可以看到效果
```

