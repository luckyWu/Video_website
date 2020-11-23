

# 拨号代理搭建



1.购买动态vps云，这里以云立方为例

![1597664442666](C:\Users\ADMINI~1\AppData\Local\Temp\1597664442666.png)





```
adsl-start #拨号         adsl-stop #停止拨号
service tinyproxy stop
```

```

$ wget https://bootstrap.pypa.io/get-pip.py
$ python get-pip.py
$ pip -V　　#查看pip版本
```

```
pip install -i 国内镜像地址 包名

清华：https://pypi.tuna.tsinghua.edu.cn/simple

阿里云：http://mirrors.aliyun.com/pypi/simple/

中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/

华中理工大学：http://pypi.hustunique.com/

山东理工大学：http://pypi.sdutlinux.org/ 

豆瓣：http://pypi.douban.com/simple/
```



2.Squid 搭建 HTTP 代理服务器 

```
yum install squid #安装squid
```

```
rpm -qa |grep squid #查看版本
squid-migration-script-3.5.20-15.el7_8.1.x86_64
squid-3.5.20-15.el7_8.1.x86_64
```

```
[root@www ~]# vi /etc/squid/squid.conf
# Squid normally listens to port 3128
http_port 3128
http_access allow all
```

```
squid -s 启动squid
squid -k kill 停止squid
```

```
netstat -ntlp   //查看当前所有tcp端口
```

```
iptables -I INPUT -p tcp --dport 8888 -j ACCEPT #防火墙开放该端口
```

3.redis安装

```
下载fedora的epel仓库
yum install epel-release
安装redis数据库
yum install redis
```

```
[root@www bin]# vi /etc/redis.conf

# Redis configuration file example.
bind 0.0.0.0
protected-mode no
```

```
查看redis状态 systemctl status redis
1.nohup redis-server &
2.通过指定配置文件启动
redis-server /etc/redis/6379.conf
远程连接 redis-cli -h 118.99.37.56 -p 6379
CONFIG GET protected-mode 查看配置文件
```

```
import redis
import random
 
# Redis 数据库 IP
REDIS_HOST = '118.99.37.56'
# Redis 数据库密码，如无则填 None
REDIS_PASSWORD = Npne
# Redis 数据库端口
REDIS_PORT = 6379
# 代理池键名
PROXY_KEY = 'adsl'
 
class RedisClient(object):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, proxy_key=PROXY_KEY):
        """
        初始化 Redis 连接
        :param host: Redis 地址
        :param port: Redis 端口
        :param password: Redis 密码
        :param proxy_key: Redis 哈希表名
        """
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)
        self.proxy_key = proxy_key
 
    def set(self, name, proxy):
        """
        设置代理
        :param name: 主机名称
        :param proxy: 代理
        :return: 设置结果
        """
        return self.db.hset(self.proxy_key, name, proxy)
 
    def get(self, name):
        """
        获取代理
        :param name: 主机名称
        :return: 代理
        """
        return self.db.hget(self.proxy_key, name)
 
    def count(self):
        """
        获取代理总数
        :return: 代理总数
        """
        return self.db.hlen(self.proxy_key)
 
    def remove(self, name):
        """
        删除代理
        :param name: 主机名称
        :return: 删除结果
        """
        return self.db.hdel(self.proxy_key, name)
 
    def names(self):
        """
        获取主机名称列表
        :return: 获取主机名称列表
        """
        return self.db.hkeys(self.proxy_key)
 
    def proxies(self):
        """
        获取代理列表
        :return: 代理列表
        """
        return self.db.hvals(self.proxy_key)
 
    def random(self):
        """
        随机获取代理
        :return:
        """
        proxies = self.proxies()
        return random.choice(proxies)
 
    def all(self):
        """
        获取字典
        :return:
        """return self.db.hgetall(self.proxy_key)
```

