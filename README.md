
# Finance
这是一个python股票数据收集和分析系统，我们使用tushare开源接口，定时的是爬取数据保存到数据库中，然后我们拿数据库中的数据用来分析策略。


## 愿景

> 希望有人用它，希望更多的人用它。
> 希望它能帮助到别人


## 项目简介

**系统需求**
- python3.0
- Flask
- tushare
- pandas
- SQLAlchemy
- Jinja2
- Flask-Login

**前端技术

- layui
- jquery
- echarts

**功能简介**

1.任务调度调度，定时爬取数据到数据库
2.使用echarts图形化展现数据
3.用户权限控制


## 项目部署

1.下载项目到本地，以下是把项目克隆到本地

```code
git clone https://gitee.com/zcm2015/finance.git
```

2.初始化数据库，在项目根目录执行

```code
python manage.py create_db
```

3.启动项目，在项目根目录执行

```code
python manage.py runserver
```

4.访问项目地址

```
http://localhost:5000/auth/
```

5.初始化数据

```code
# 初始化数据的接口在/app/init/views.py文件里

http://localhost:5000/init/initStock
```



**截图截图**

![输入图片说明](https://gitee.com/uploads/images/2018/0328/214522_603d37e5_387233.png "股票列表.PNG")

![输入图片说明](https://gitee.com/uploads/images/2018/0328/214743_c6fb8a91_387233.png "业绩报告.PNG")

![输入图片说明](https://gitee.com/uploads/images/2018/0328/214751_5708ce0d_387233.png "盈利能力.PNG")

