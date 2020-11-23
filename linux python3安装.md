# linux python3安装

1. 安装依赖环境

```
　yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
```

​    2.下载Python3 　https://www.python.org/downloads

` wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz` 

​    3.安装python3

```
安装在/usr/local/python3（具体安装位置看个人喜好）
mkdir -p /usr/local/python3
```

  4.解压

```
tar -zxvf Python-3.6.1.tgz
```

5.进入解压后的目录，指定安装目录，编译安装

```
cd Python-3.6.1
./configure --prefix=/usr/local/python3
make
make install
```

6.建立python3的软链

`ln -s /usr/local/python3/bin/python3 /usr/bin/python3` 

