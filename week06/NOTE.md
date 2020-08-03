# Python学习笔记Week06 by Santo

# 作业记录 


1. Bootstrap模板适配待修改。 

2. 作业调试时遇到一个报错如下，主要提示为ValueError: source code string cannot contain null bytes，OSError: [WinError 123] 文件名、目录名或卷标语法不正确。: '<frozen importlib._bootstrap>'，经过几番折腾，各种比对、改文件未果，继续好几轮谷歌终于在StackOverflow上找到答案，原来时windows下用 python manage.py inspectdb > models.py生成的文件格式不是utf-8导致，修改文件格式后bug消失！https://stackoverflow.com/questions/46248546/python-django-valueerror-source-code-string-cannot-contain-null-bytes

   `PS D:\Learning\Coding\Python\Python001-class01\week06\SDjango> d:/ProgramData/Anaconda3/python.exe .\manage.py runserver Watching for file changes with StatReloader Exception in thread django-main-thread: Traceback (most recent call last):  File "D:\ProgramData\Anaconda3\lib\threading.py", line 926, in _bootstrap_inner    self.run()  File "D:\ProgramData\Anaconda3\lib\threading.py", line 870, in run    self._target(*self._args, **self._kwargs)  File "D:\ProgramData\Anaconda3\lib\site-packages\django\utils\autoreload.py", line 54, in wrapper          fn(*args, **kwargs)  File "D:\ProgramData\Anaconda3\lib\site-packages\django\core\management\commands\runserver.py", line 109, in inner_run    autoreload.raise_last_exception()  File "D:\ProgramData\Anaconda3\lib\site-packages\django\utils\autoreload.py", line 77, in raise_last_exception    raise _exception[1]  File "D:\ProgramData\Anaconda3\lib\site-packages\django\core\management\__init__.py", line 337, in execute    autoreload.check_errors(django.setup)()  File "D:\ProgramData\Anaconda3\lib\site-packages\django\utils\autoreload.py", line 54, in wrapper          fn(*args, **kwargs)  File "D:\ProgramData\Anaconda3\lib\site-packages\django\__init__.py", line 24, in setup    apps.populate(settings.INSTALLED_APPS)  File "D:\ProgramData\Anaconda3\lib\site-packages\django\apps\registry.py", line 114, in populate           app_config.import_models()  File "D:\ProgramData\Anaconda3\lib\site-packages\django\apps\config.py", line 211, in import_models        self.models_module = import_module(models_module_name)  File "D:\ProgramData\Anaconda3\lib\importlib\__init__.py", line 127, in import_module    return _bootstrap._gcd_import(name[level:], package, level)  File "", line 1006, in _gcd_import  File "", line 983, in _find_and_load  File "", line 967, in _find_and_load_unlocked  File "", line 677, in _load_unlocked  File "", line 724, in exec_module  File "", line 860, in get_code  File "", line 791, in source_to_code  File "", line 219, in _call_with_frames_removed ValueError: source code string cannot contain null bytes   Traceback (most recent call last):  File ".\manage.py", line 21, in     main()  File ".\manage.py", line 17, in main    execute_from_command_line(sys.argv)  File "D:\ProgramData\Anaconda3\lib\site-packages\django\core\management\__init__.py", line 381, in execute_from_command_line    utility.execute()  File "D:\ProgramData\Anaconda3\lib\site-packages\django\core\management\__init__.py", line 375, in exec    self.fetch_command(subcommand).run_from_argv(self.argv) _argv    self.execute(*args, **cmd_options)  File "D:\ProgramData\Anaconda3\lib\site-packages\django\core\management\commands\runserver.py", line 60, in execute    super().execute(*args, **options)  File "D:\ProgramData\Anaconda3\lib\site-packages\django\core\management\base.py", line 364, in execute    output = self.handle(*args, **options)  File "D:\ProgramData\Anaconda3\lib\site-packages\django\core\management\commands\runserver.py", line 95, in handle    self.run(**options)  File "D:\ProgramData\Anaconda3\lib\site-packages\django\core\management\commands\runserver.py", line 102, in run    autoreload.run_with_reloader(self.inner_run, **options)  File "D:\ProgramData\Anaconda3\lib\site-packages\django\utils\autoreload.py", line 598, in run_with_reloader    start_django(reloader, main_func, *args, **kwargs)  File "D:\ProgramData\Anaconda3\lib\site-packages\django\utils\autoreload.py", line 583, in start_django    reloader.run(django_main_thread)  File "D:\ProgramData\Anaconda3\lib\site-packages\django\utils\autoreload.py", line 301, in run    self.execute(*args, **cmd_options)  File "D:\ProgramData\Anaconda3\lib\site-packages\django\core\management\commands\runserver.py", line 60, in execute    super().execute(*args, **options)  File "D:\ProgramData\Anaconda3\lib\site-packages\django\core\management\base.py", line 364, in execute    output = self.handle(*args, **options)  File "D:\ProgramData\Anaconda3\lib\site-packages\django\core\management\commands\runserver.py", line 95, in handle    self.run(**options)  File "D:\ProgramData\Anaconda3\lib\site-packages\django\core\management\commands\runserver.py", line 102, in run    autoreload.run_with_reloader(self.inner_run, **options)  File "D:\ProgramData\Anaconda3\lib\site-packages\django\utils\autoreload.py", line 598, in run_with_reloader    start_django(reloader, main_func, *args, **kwargs)  File "D:\ProgramData\Anaconda3\lib\site-packages\django\utils\autoreload.py", line 583, in start_django    reloader.run(django_main_thread)  File "D:\ProgramData\Anaconda3\lib\site-packages\django\utils\autoreload.py", line 301, in run    self.run_loop()  File "D:\ProgramData\Anaconda3\lib\site-packages\django\utils\autoreload.py", line 307, in run_loop    next(ticker)  File "D:\ProgramData\Anaconda3\lib\site-packages\django\utils\autoreload.py", line 347, in tick    for filepath, mtime in self.snapshot_files():  File "D:\ProgramData\Anaconda3\lib\site-packages\django\utils\autoreload.py", line 363, in snapshot_files    for file in self.watched_files():    next(ticker)  File "D:\ProgramData\Anaconda3\lib\site-packages\django\utils\autoreload.py", line 347, in tick    for filepath, mtime in self.snapshot_files():  File "D:\ProgramData\Anaconda3\lib\site-packages\django\utils\autoreload.py", line 363, in snapshot_files    for file in self.watched_files():  File "D:\ProgramData\Anaconda3\lib\site-packages\django\utils\autoreload.py", line 262, in watched_files    yield from iter_all_python_module_files()  File "D:\ProgramData\Anaconda3\lib\site-packages\django\utils\autoreload.py", line 103, in iter_all_python_module_files    return iter_modules_and_files(modules, frozenset(_error_files))  File "D:\ProgramData\Anaconda3\lib\site-packages\django\utils\autoreload.py", line 139, in iter_modules_and_files    if not path.exists():  File "D:\ProgramData\Anaconda3\lib\pathlib.py", line 1346, in exists    self.stat()  File "D:\ProgramData\Anaconda3\lib\pathlib.py", line 1168, in stat    return self._accessor.stat(self) OSError: [WinError 123] 文件名、目录名或卷标语法不正确。:'<frozen importlib._bootstrap>'`

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

