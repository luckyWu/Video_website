# go

安装包下载，安装

```
https://golang.google.cn/dl/
```

新建工作目录

```
新建D:\work\go目录
在go目录再新建bin, pkg， src目录
在src目录新建github.com目录 #github.com目录下为工程目录
```

配置GOPATH

```
在 GOPATH 指定的工作目录下，代码总是会保存在 $GOPATH/src 目录下。在工程经过 go build、go install 或 go get 等指令后，会将产生的二进制可执行文件放在 $GOPATH/bin 目录下，生成的中间缓存文件会被保存在 $GOPATH/pkg 下

windows在环境变量中添加变量名为GOPATH, 值为工作路径如D:\work\go
```

在github.com目录下新建文件夹为test

在test文件夹中新建test.go文件写入

```
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

在命令行中使用go run命令执行文件

```
D:\work\go\src\githunb.com\test>go run test.go
Hello, World!
```



 

