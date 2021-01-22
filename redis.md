# redis

hash:

​      hgetall 对象---------取出对象所有值

​      hsetall对象----------一次设置所有值；

List:

​     lpush list1 1 2 3 4 5-----------------------5 4 3 2 1放的顺序

​     BLPOP list TIME------若列表中无元素，等一段时间无数据者输出无;b-BLOCK阻塞

网站优化的两大定律：

​            1.缓存：用空间换取时间 ---redis

​            2.削峰：能推迟的事都不要马上做；

启动Redis服务器：

​            redis-server 配置文件

​           

​            停止服务：

​            客服端>shutdown

​            Ctrl +  c

​            kill + 进程号；

## 常用5中数据类型：

1.字符串

2.哈希：

3.列表：

4.集合：

5.有序集合：

## 主从复制

master不用改配置

slave修改两条配置；

连接服务器通过info replication 查看信息

### redis放的应该是体量不大的热数据；





centos 配置

```
yum -y install redis
```

2.修改配置

```vim /etc/redis.conf
vim /etc/redis.conf
```



首先，注释这一行：

```
#bind 127.0.0.1
```

另外，推荐给Redis设置密码，取消注释这一行：

\#requirepass foobared

foobared即当前密码，可以自行修改为

```
requirepass 密码
```

然后重启Redis服务，使用的命令如下：

```
sudo systemctl restart redis
```

```
systemctl start redis.service #启动redis服务器
systemctl stop redis.service #停止redis服务器
systemctl restart redis.service #重新启动redis服务器
systemctl status redis.service #获取redis服务器的运行状态
systemctl enable redis.service #开机启动redis服务器
```



