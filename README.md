# 图书管理系统
<img src="https://img.shields.io/badge/Platform-Win32%20|%20Linux%20|%20macOS-blue?color=#4ec820" alt="Platform Win32 | Linux | macOS"> <img src="https://img.shields.io/badge/License-MIT-blue?color=#4ec820" alt="MIT"> <a href="https://wakatime.com/badge/github/wjy2311077/library-management-system-pyqt"><img src="https://wakatime.com/badge/github/wjy2311077/library-management-system-pyqt.svg" alt="wakatime"></a>

一个Windows风格的图书管理系统



## 简介

本项目基于[WHU_DB 资料管理系统](https://github.com/JOETtheIV/WHU_DB)，重构了部分代码，并重新绘制了UI

技术栈：Python3 + PyQt5 + PyQt-Fluent-Widgets

数据库：MySQL



## 功能

  用户管理：用户注册、修改信息、借书还书、浏览读者
  图书管理：增删改查
  管理员管理：增删查



## 截图

<img src="https://raw.githubusercontent.com/wjy2311077/library-management-system-pyqt/main/README.assets/MainWindow.png" alt="MainWindow">

<img src="https://raw.githubusercontent.com/wjy2311077/library-management-system-pyqt/main/README.assets/LoginWindow.png" alt="LoginWindow">

<img src="https://raw.githubusercontent.com/wjy2311077/library-management-system-pyqt/main/README.assets/SearchBooksWindow.png" alt="SearchBooksWindow">

<img src="https://raw.githubusercontent.com/wjy2311077/library-management-system-pyqt/main/README.assets/SearchAdminWindow.png" alt="SearchAdminWindow">


## 开发

### 安装依赖

```shell
pip install -r requirements.txt
```

如果PyQt-Fluent-Widgets安装失败，可以尝试使用以下命令
```shell
pip install "PyQt-Fluent-Widgets[full]" -i https://pypi.org/simple/
```


### 运行

更改Lib_DB.py中的参数可连接本地MySQL，同时运行StartClient.py启动客户端。

超级管理员用户密码为硬编码，在StartClient.py中修改。

通过登录超级管理员界面创建管理员，通过登录读者界面可以注册读者