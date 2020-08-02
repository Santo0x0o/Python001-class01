# Python学习笔记Week03 by Santo

# 作业记录 


1. Bootstrap模板适配待修改。 

# 1. 开发环境配置 

**获取课程源码操作方法：** 

切换分支：git checkout 5a 

**Django 官方文档** 

[https://docs.djangoproject.com/zh-hans/3.0/](https://docs.djangoproject.com/zh-hans/3.0/)

![图片](https://uploader.shimo.im/f/jz9U8Vmh0gWUQuSH.png!thumbnail)

![图片](https://uploader.shimo.im/f/z2k2UAliQcuctpLx.png!thumbnail)

![图片](https://uploader.shimo.im/f/SYk8lCdLe64SPCUR.png!thumbnail)

首次安装Django: pip install django==2.2.13 

![图片](https://uploader.shimo.im/f/ZphhR1hI0s3BvL6z.png!thumbnail)

# 2. 创建项目和目录结构 

**获取课程源码操作方法：** 

切换分支：git checkout 5a 

![图片](https://uploader.shimo.im/f/2kJmbKE2omSiUwLf.png!thumbnail)

![图片](https://uploader.shimo.im/f/w9oy1denmOOyZ1IZ.png!thumbnail)

![图片](https://uploader.shimo.im/f/s3ic7PXOYgztE5ZB.png!thumbnail)

# 3. 解析settings.py主要配置文件 

**获取课程源码操作方法：** 

切换分支：git checkout 5a 

![图片](https://uploader.shimo.im/f/a4SVUcKezSg5kwsh.png!thumbnail)

![图片](https://uploader.shimo.im/f/5WIzrTnsN97bYV2o.png!thumbnail)

# 4. urls调度器 

**获取课程源码操作方法：** 

切换分支：git checkout 5a 

URL调度器也叫URLConf 

![图片](https://uploader.shimo.im/f/JY11ugsbwIuoxFpA.png!thumbnail)

![图片](https://uploader.shimo.im/f/5Fb9Ct5PCdF46pDe.png!thumbnail)

![图片](https://uploader.shimo.im/f/xpMZKlSfWhFsprbP.png!thumbnail)

![图片](https://uploader.shimo.im/f/wnw4fN3OXVWWe9t4.png!thumbnail)

尝试运行Django 

python manager.py runserver 

报错，通过更新pymysql版本等逐步解决MySQL连接错误后，还有个报错如下： 

```python
PS D:\Learning\Coding\Python\pythontrain\MyDjango> d:/ProgramData/Anaconda3/python.exe .\manage.py runserver 
Watching for file changes with StatReloader 
Performing system checks… 
System check identified no issues (0 silenced). 
Exception in thread django-main-thread: 
Traceback (most recent call last): 
File "D:\ProgramData\Anaconda3\lib\threading.py", line 926, in _bootstrap_inner 
self.run() 
File "D:\ProgramData\Anaconda3\lib\threading.py", line 870, in run 
self._target(*self._args, *self._kwargs) File "D:\ProgramData\Anaconda3\lib\site-packages\django\utils\autoreload.py", line 54, in wrapper fn(args, **kwargs) 
File "D:\ProgramData\Anaconda3\lib\site-packages\django\core\management\commands\runserver.py", line 120, in inner_run 
self.check_migrations() 
File "D:\ProgramData\Anaconda3\lib\site-packages\django\core\management\base.py", line 453, in check_migrations 
executor = MigrationExecutor(connections[DEFAULT_DB_ALIAS]) 
File "D:\ProgramData\Anaconda3\lib\site-packages\django\db\migrations\executor.py", line 18, in init 
self.loader = MigrationLoader(self.connection) 
File "D:\ProgramData\Anaconda3\lib\site-packages\django\db\migrations\loader.py", line 49, in init 
self.build_graph() 
File "D:\ProgramData\Anaconda3\lib\site-packages\django\db\migrations\loader.py", line 212, in build_graph 
self.applied_migrations = recorder.applied_migrations() 
File "D:\ProgramData\Anaconda3\lib\site-packages\django\db\migrations\recorder.py", line 73, in applied_migrations 
if self.has_table(): 
File "D:\ProgramData\Anaconda3\lib\site-packages\django\db\migrations\recorder.py", line 56, in has_table 
return self.Migration._meta.db_table in self.connection.introspection.table_names(self.connection.cursor()) 
File "D:\ProgramData\Anaconda3\lib\site-packages\django\db\backends\base\base.py", line 256, in cursor 
return self._cursor() 
File "D:\ProgramData\Anaconda3\lib\site-packages\django\db\backends\base\base.py", line 233, in _cursor 
self.ensure_connection() 
File "D:\ProgramData\Anaconda3\lib\site-packages\django\db\backends\base\base.py", line 217, in ensure_connection 
self.connect() 
File "D:\ProgramData\Anaconda3\lib\site-packages\django\db\backends\base\base.py", line 197, in connect 
self.init_connection_state() 
File "D:\ProgramData\Anaconda3\lib\site-packages\django\db\backends\mysql\base.py", line 231, in init_connection_state 
if self.features.is_sql_auto_is_null_enabled: 
File "D:\ProgramData\Anaconda3\lib\site-packages\django\utils\functional.py", line 80, in get 
res = instance.dict[self.name] = self.func(instance) 
File "D:\ProgramData\Anaconda3\lib\site-packages\django\db\backends\mysql\features.py", line 82, in is_sql_auto_is_null_enabled 
cursor.execute('SELECT @@SQL_AUTO_IS_NULL') 
File "D:\ProgramData\Anaconda3\lib\site-packages\django\db\backends\utils.py", line 103, in execute 
sql = self.db.ops.last_executed_query(self.cursor, sql, params) 
File "D:\ProgramData\Anaconda3\lib\site-packages\django\db\backends\mysql\operations.py", line 146, in last_executed_query 
query = query.decode(errors='replace') 
AttributeError: 'str' object has no attribute 'decode' 
```

参照如下博文确认报错原因，并按指导操作解决： 
[https://blog.csdn.net/qq_36274515/article/details/89043481](https://blog.csdn.net/qq_36274515/article/details/89043481)

运行成功 

![图片](https://uploader.shimo.im/f/wlx8sY5o0xP7e0lc.png!thumbnail)

访问结果如下： 

![图片](https://uploader.shimo.im/f/9jYsYVurOAgt3PJP.png!thumbnail)

**Django显示的链接源如下：** 

settings.py_ROOT_URLCONF-----自定义APP_index.urls-----views.index 

![图片](https://uploader.shimo.im/f/GsSG0PGmbtG1Jk9V.png!thumbnail)

![图片](https://uploader.shimo.im/f/SZp4PONGNeFvV8b7.png!thumbnail)

![图片](https://uploader.shimo.im/f/pmpGiZ1CSNtzKrrh.png!thumbnail)

![图片](https://uploader.shimo.im/f/icB6fzX3NY4usJoI.png!thumbnail)

# 5. 模块和包 

**获取课程源码操作方法：** 

切换分支：git checkout 5a 

![图片](https://uploader.shimo.im/f/XRPVqkoylFVh673X.png!thumbnail)

```python
if __name__ == '__main__': 
__init__.py 
```

# 6. 让URL支持变量 

**获取课程源码操作方法：** 

切换分支：git checkout 5b 

![图片](https://uploader.shimo.im/f/vGhpVKZenYKdJSGM.png!thumbnail)

# 7. URL正则和自定义过滤器 

**获取课程源码操作方法：** 

切换分支：git checkout 5b 

![图片](https://uploader.shimo.im/f/4hPQhyZlGLoDNQwq.png!thumbnail)

# 8. view视图快捷方式 

**获取课程源码操作方法：** 

切换分支：git checkout 5b 

![图片](https://uploader.shimo.im/f/VbjOYPD8CJ2v0s1I.png!thumbnail)

![图片](https://uploader.shimo.im/f/jqOtxoAtAcMDDDuO.png!thumbnail)

![图片](https://uploader.shimo.im/f/tOiqVezrrV6bFYMR.png!thumbnail)

# 9. 使用ORM创建数据表 

**获取课程源码操作方法：** 

切换分支：git checkout 5c 

![图片](https://uploader.shimo.im/f/UKXsmGauFhyGCQke.png!thumbnail)

![图片](https://uploader.shimo.im/f/KKKTPX8OSoDuANls.png!thumbnail)

# 10. ORM API 

**获取课程源码操作方法：** 

切换分支：git checkout 5c 

![图片](https://uploader.shimo.im/f/EZjLKtHxq34ESroC.png!thumbnail)

![图片](https://uploader.shimo.im/f/eBtUYcpQzo9jyDb0.png!thumbnail)

![图片](https://uploader.shimo.im/f/edLQR4UYa07oMaBR.png!thumbnail)

常见报错 

1  django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module: No module named 'MySQLdb' 

解决方法：在 __init__.py 文件中添加以下代码即可 

import pymysql 

pymysql.install_as_MySQLdb() 

2   version = Database.version_info 

# if version < (1, 3, 13): 

# raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__) 

3  AttributeError: 'str' object has no attribute 'decode' 

出现这个错误之后可以根据错误提示找到文件位置，打开 operations.py 文件，找到以下代码： 

def last_executed_query(self, cursor, sql, params): 

query = getattr(cursor, '_executed', None) 

# if query is not None: 

#     query = query.decode(errors='replace') 

return query 

# 11. Django模板开发 

**获取课程源码操作方法：** 

切换分支：git checkout 5d 

# 12. 展示数据库中的内容 

**获取课程源码操作方法：** 

切换分支：git checkout 5d 

# 13. 豆瓣页面展示功能的需求分析 

**获取课程源码操作方法：** 

切换分支：git checkout 5e 

# 14. urlconf与models的配置 

**获取课程源码操作方法：** 

切换分支：git checkout 5e 

![图片](https://uploader.shimo.im/f/1AkIGSg4u09jDCvT.png!thumbnail)

![图片](https://uploader.shimo.im/f/TtD2iEX7TN0hwaYy.png!thumbnail)

在MySQL中 使用source xxx.sql 命令导入sql文件中的数据到数据库。 

通过 python manage.py inspectdb > models.py 获取已有数据库中的数据。 

# 15. views视图的编写 

**获取课程源码操作方法：** 

切换分支：git checkout 5e 

![图片](https://uploader.shimo.im/f/krYjn7gyx83h04nG.png!thumbnail)

![图片](https://uploader.shimo.im/f/U4bmsijXOWb5zYqZ.png!thumbnail)

# 16. 结合bootstrap模板进行开发 

**获取课程源码操作方法：** 

切换分支：git checkout 5e 

![图片](https://uploader.shimo.im/f/qu6Y7SwMec0p2r52.png!thumbnail)

![图片](https://uploader.shimo.im/f/oTZc6TKHkTOFCQDt.png!thumbnail)

bootstrap三个必要文件： 

bootstrap.min.css 

bootstrap.min.js 

jquery.js 

# 17. 如何阅读Django的源代码 

**获取课程源码操作方法：** 

切换分支：git checkout 5e 

![图片](https://uploader.shimo.im/f/RljDkRZmjl04Ibdb.png!thumbnail)

![图片](https://uploader.shimo.im/f/ev1G5hD9qNTjvVT3.png!thumbnail)

# 18. manage.py源码分析 

** 说明：视频 2’45" 处， 

`execute_from_command_line((runserver,8080))` 

应改为 

`execute_from_command_line(('manage.py','runserver','8080'))` 

**获取课程源码操作方法：** 

切换分支：git checkout 5e  

# 本周作业 

**作业背景** 

数据经过分析和清洗之后，需要使用适当的方式对数据进行展示，Web 就是当前最流行的展示方式之一。 

**作业要求：** 使用 Django 展示豆瓣电影中某个电影的短评和星级等相关信息： 


1. 要求使用 MySQL 存储短评内容（至少 20 条）以及短评所对应的星级； 
2. 展示高于 3 星级（不包括 3 星级）的短评内容和它对应的星级； 
3. （选做）在 Web 界面增加搜索框，根据搜索的关键字展示相关的短评。 

