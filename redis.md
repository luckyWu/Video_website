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







​     