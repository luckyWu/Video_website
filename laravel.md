# laravel

**一、 composer的安装：**

1.Composer是什么？ 是 PHP 用来管理依赖（dependency）关系的工具。 你可以在自己的项目中声明所依赖的外部工具库（libraries）， Composer 会帮你安装这些依赖的库文件。 

2.Composer常用命令： composer -v 查看版本 composer selfupdate 更新composer

**通过 Composer Create-Project**

你还可以在终端中通过 Composer 的 `create-project` 命令来安装 Laravel 应用：

composer create-project --prefer-dist laravel/laravel blog 

如果要下载安装 Laravel 其他版本应用，比如 5.6 版本，可以使用这个命令：

`composer create-project --prefer-dist laravel/laravel blog ``"5.6.*"` 

启动项目

```
php artisan serve --port=80 --host 0.0.0.0
```

安装bootstrap

1.安装bootstrap

```
composer require laravel/ui --dev
```

 2.引入bootstrap

```
php artisan ui bootstrap
```

3.Bootstrap 是以 NPM 扩展包的形式集成到 Laravel 项目中的. 在package.json中可发现：

- bootstrap —— Bootstrap NPM 扩展包；
- jquery —— jQuery NPM 扩展包；
- laravel-mix —— 由 Laravel 官方提供的静态资源管理工具。

这些扩展包，为 Laravel 提供了一套完整的前端工作流。

4.可以使用 NPM 对这些扩展包进行安装。

```
curl --silent --location https://rpm.nodesource.com/setup_5.x | bash -
yum -y install nodejs
```



先使用国内镜像加速：

```
$ npm config set registry=https://registry.npm.taobao.org
$ yarn config set registry 'https://registry.npm.taobao.org'
```

5.使用 Yarn 对扩展包进行安装，请在项目根目录下运行以下命令进行安装：

```
$ yarn install --no-bin-links
$ yarn add cross-env
```

6.编辑*resources/sass/app.scss*

```
@import '~bootstrap/scss/bootstrap';
```

7.将 Bootstrap 导入成功之后，需要使用以下命令来将 `.scss` 文件编译为 `.css` 才能正常使用

```
npm run dev
```

或使用以下命令实时监测.scss变化并及时编译为.css

```
 npm run watch-poll
```

(在进行项目开发时 `npm run watch-poll` 必须一直运行着，避免出现前端文件更改后没有应用到页面上）。

所有编译后的资源文件都被存放在 `public` 文件夹中，在 `public/css` 文件夹中看到刚刚编译成功之后的文件。

8.在所需视图页面的<head>中引入：

```
<link rel="stylesheet" href="{{ mix('css/app.css') }}">
```

