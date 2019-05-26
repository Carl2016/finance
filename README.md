
# Finance
这是一个python股票数据收集和分析系统，我们使用tushare开源接口，定时的是爬取数据保存到数据库中，然后我们拿数据库中的数据用来分析策略。

## 愿景

> 希望有人用它，希望更多的人用它。
> 希望它能帮助到别人

## 项目简介

**系统需求**
- python3.6
- Flask
- tushare
- pandas
- Flask-APScheduler
- Flask-Security
- Flask-Mail
- SQLAlchemy
- Jinja2
- Flask-Login

**前端技术**
- layui
- jquery
- echarts

**功能简介**
- 任务调度调度，定时爬取数据到数据库
- 使用echarts图形化展现数据
- 用户权限控制

## 2019-05-26更新
* 更换后台界面 X-admin
* 更改文件目录
* 新增日线行情K线图
* 更新菜单分类列表

## 项目部署

配置数据库文件config.py ,并且导入数据库脚本在db目录下

```code
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:xxxx@localhost:3306/finance?charset=utf8'
```

1.下载项目到本地，以下是把项目克隆到本地

```code
git clone https://gitee.com/zcm2015/finance.git
```

2.初始化数据库，在项目根目录执行

```code
python manager.py create_db
```

3.导入db脚本
```
脚本在db目录下:finance.sql
```

4.启动项目，在项目根目录执行

```code
python manager.py runserver
```

5.访问项目地址

```
http://localhost:5000/login
```

6.登录用户
```
用户名：admin
密码:admin
```

**截图截图**

![输入图片说明](https://images.gitee.com/uploads/images/2019/0526/232656_7f8ae03c_387233.png "日线行情.PNG")

![输入图片说明](https://images.gitee.com/uploads/images/2019/0526/232829_43c0317c_387233.png "股票列表.PNG")

![输入图片说明](https://images.gitee.com/uploads/images/2019/0526/232905_a0f65011_387233.png "任务调度.PNG")

![输入图片说明](https://images.gitee.com/uploads/images/2019/0526/232913_8a0ab6d9_387233.png "每日指标.PNG")

![输入图片说明](https://images.gitee.com/uploads/images/2019/0526/233102_06f41441_387233.png "菜单.PNG")