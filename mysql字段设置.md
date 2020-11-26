# 数据库设置

id,  电视集数，电视名称， 电视清晰度，国家， 电视格式， 磁力链接， 电视名id，更新时间， 创建时间, 状态



```
DROP TABLE IF EXISTS series;
DROP TABLE IF EXISTS movies;
create table series
(
  id int not null AUTO_INCREMENT,
  pid varchar(200),
  name    VARCHAR(200),
  magent  VARCHAR(1024),
  status    INT,
  hd VARCHAR(20),
  lang VARCHAR(4),
  area VARCHAR(20),
  format VARCHAR(20),
  create_at    DATE,
  update_at    DATE,
  num int,
  PRIMARY KEY (id),
  CONSTRAINT FK_movie FOREIGN KEY (name) REFERENCES movies(name)
) DEFAULT CHARSET=utf8;
```



电视剧表

id, 电视名称，主演，导演， 地区， 年份， 时长，更新时间， 创建时间，电视图片，电视详情， 发布时间，状态

```
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS series;
DROP TABLE IF EXISTS movies;
create table movies
(
  id     int not null AUTO_INCREMENT,
  pid varchar(200),
  name    VARCHAR(200),
  url  VARCHAR(1024),
  year    VARCHAR(8),
  status int,
  img VARCHAR(1024),
  descr  text,
  performer VARCHAR(1024),
  lang VARCHAR(10),
  area VARCHAR(20),
  pubtime DATE,
  create_at    DATE,
  update_at    DATE,
  UNIQUE key uq(name),
  PRIMARY KEY (id)
) AUTO_INCREMENT=0  DEFAULT CHARSET=utf8;
create table series
(
  id int not null AUTO_INCREMENT,
  pid varchar(200),
  name    VARCHAR(200),
  magent  VARCHAR(1024),
  status    INT,
  hd VARCHAR(20),
  lang VARCHAR(4),
  area VARCHAR(20),
  format VARCHAR(20),
  create_at    DATE,
  update_at    DATE,
  num int,
  PRIMARY KEY (id),
  CONSTRAINT FK_movie FOREIGN KEY (name) REFERENCES movies(name)
) DEFAULT CHARSET=utf8;


create table movies
(
  id     int not null AUTO_INCREMENT,
  create_at    DATE,
  PRIMARY KEY (id)
) AUTO_INCREMENT=0  DEFAULT CHARSET=utf8;
```

增加字段

```
ALTER TABLE movies ADD desc varchar(2048);
```

查询

```
select num,magent from series where num<4 and name="隐秘而伟大" ORDER BY num ASC
```



**插入数据**

```
INSERT INTO table_name ( field1, field2,...fieldN )
                       VALUES
                       ( value1, value2,...valueN );
```



```
show databases;

```



**MySQL 常用字段类型**

 

一个数据表是由若干个字段组成的，一个表十几个字段也很正常，每个字段表示不同的信息，需要使用不同类型的数据。

 所以在创建表的时候，要为每个字段指定适合的数据类型。

MySQL 中常用的字段类型有以下这些：

1. 整数类型

| 数据类型  | 数据范围        |
| --------- | --------------- |
| TINYINT   | -128 -- 127     |
| SMALLINT  | -32768 -- 32767 |
| MEDIUMINT | -2^23 -- 2^23-1 |
| INT       | -2^31 -- 2^31-1 |
| BIGINT    | -2^63 -- 2^63-1 |

 

2. 字符串类型

 

| 数据类型   | 字节范围        | 用途               |
| ---------- | --------------- | ------------------ |
| CHAR(n)    | 0 -- 255字节    | 定长字符串         |
| VARCHAR(n) | 0 -- 65535字节  | 变长字符串         |
| TEXT       | 0 -- 65535字节  | 长文本数据         |
| LONGTEXT   | 0 -- 2^32-1字节 | 极大文本数据       |
| BLOB       | 0 -- 65535字节  | 二进制长文本数据   |
| LONGBLOB   | 0 -- 2^32-1字节 | 二进制极大文本数据 |

 

3. 小数类型

 

| 数据类型 | 数据用法     | 数据范围   |
| -------- | ------------ | ---------- |
| Float    | Float(m,n)   | 7位有效数  |
| Double   | Double(m,n)  | 15位有效数 |
| Decimal  | Decimal(m,n) | 28位有效数 |

m 表示浮点数的总长度，n 表示小数点后有效位数。

 

4. 时间类型

 

| 数据类型  | 格式                   | 用途       |
| --------- | ---------------------- | ---------- |
| DATE      | YYYY-MM-DD             | 日期       |
| TIME      | HH:MM:SS               | 时间       |
| YEAR      | YYYY                   | 年份       |
| DATETIME  | YYYY-MM-DD HH:MM:SS    | 日期和时间 |
| TIMESTAMP | 10位或13位整数（秒数） | 时间戳     |

 

5. 枚举类型enum(枚举值1,枚举值2,...)枚举类型只能在列出的值中选择一个，如性别。