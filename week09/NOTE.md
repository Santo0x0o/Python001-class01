# Python学习笔记Week09 by Santo

# 作业记录：

查询管理器，及用户注册等原理待加深理解~~~

# 1. Django源码分析之URLconf的偏函数

**获取课程源码操作方法：**

切换分支：git checkout 7b

![图片](https://uploader.shimo.im/f/6kWDEOlwzlk9KkpD.png!thumbnail)

![图片](https://uploader.shimo.im/f/Z4vP5HAZjNMfmdZl.png!thumbnail)

![图片](https://uploader.shimo.im/f/5lXaJUL5rGkJHgMm.png!thumbnail)

![图片](https://uploader.shimo.im/f/YcL6j443ffWtJ7xS.png!thumbnail)

![图片](https://uploader.shimo.im/f/BzYP6jmIoTNFNeor.png!thumbnail)

![图片](https://uploader.shimo.im/f/qZklUDWBsSwJYiU2.png!thumbnail)

![图片](https://uploader.shimo.im/f/twSDZ4lDtsCYkJsK.png!thumbnail)

# 2. Django源码分析之URLconf的include

**获取课程源码操作方法：**

切换分支：git checkout 7b

![图片](https://uploader.shimo.im/f/iaCHYwdpO8LqY8kr.png!thumbnail)

# 3. Django源码分析之view视图的请求过程

**获取课程源码操作方法：**

切换分支：git checkout 7b

![图片](https://uploader.shimo.im/f/cxZpqyJoeJSH10Yr.png!thumbnail)

![图片](https://uploader.shimo.im/f/SnXUrenRjC8n9xuC.png!thumbnail)

![图片](https://uploader.shimo.im/f/hqcDRr36H5VvaRFY.png!thumbnail)

# 4. Django源码分析之view视图的响应过程

**获取课程源码操作方法：**

切换分支：git checkout 7b

![图片](https://uploader.shimo.im/f/XrJolZcrvjfrNtjz.png!thumbnail)

![图片](https://uploader.shimo.im/f/7UCSYH1E0myUt3bV.png!thumbnail)

# 5. Django源码分析之view视图的请求响应完整流程

**获取课程源码操作方法：**

切换分支：git checkout 7b

![图片](https://uploader.shimo.im/f/aR0USNVukNDMiD6r.png!thumbnail)

# 6. Django源码分析之model模型的自增主键创建

**获取课程源码操作方法：**

切换分支：git checkout 7b

![图片](https://uploader.shimo.im/f/clEeg1yQLjWYZcY9.png!thumbnail)

![图片](https://uploader.shimo.im/f/SYm6DaYrlh0yY631.png!thumbnail)

# 7. Django源码分析之model模型的查询管理器

**获取课程源码操作方法：**

切换分支：git checkout 7b

![图片](https://uploader.shimo.im/f/t2B2GILagFFDHd3S.png!thumbnail)

![图片](https://uploader.shimo.im/f/YAgfqKjV1NbQ36vx.png!thumbnail)

# 8. Django源码分析之template模板的加载文件

**获取课程源码操作方法：**

切换分支：git checkout 7b

![图片](https://uploader.shimo.im/f/8alqeZ9gABmF9ZZb.png!thumbnail)

![图片](https://uploader.shimo.im/f/Tp4E51Awj82gGii2.png!thumbnail)

![图片](https://uploader.shimo.im/f/rZ0OLQAOzN8hGLgS.png!thumbnail)

![图片](https://uploader.shimo.im/f/Y0cImIDf5Cye5Nqm.png!thumbnail)

![图片](https://uploader.shimo.im/f/xyI81AhVNP5MxDNy.png!thumbnail)

![图片](https://uploader.shimo.im/f/jMhCpw3OrFYeNI6r.png!thumbnail)

![图片](https://uploader.shimo.im/f/ZTG3FrcZ93QUlFrb.png!thumbnail)

# 9. Django源码分析之template模板的渲染

**获取课程源码操作方法：**

切换分支：git checkout 7b

![图片](https://uploader.shimo.im/f/gj5QdDJ7S7BdIInm.png!thumbnail)

![图片](https://uploader.shimo.im/f/al5SvlOkWHSli2Ps.png!thumbnail)

![图片](https://uploader.shimo.im/f/7XI2TOfTDWVgc5Sz.png!thumbnail)

![图片](https://uploader.shimo.im/f/7oxqFabZ9kNMrHby.png!thumbnail)

# 10. DjangoWeb相关功能-管理界面

**获取课程源码操作方法：**

切换分支：git checkout 8a

![图片](https://uploader.shimo.im/f/jmE1aCweEZj4XrSq.png!thumbnail)

![图片](https://uploader.shimo.im/f/A6L4cn50w1RcKdTP.png!thumbnail)

![图片](https://uploader.shimo.im/f/EkJIpsrx9om8Nbpo.png!thumbnail)

# 11. DjangoWeb相关功能-表单

**获取课程源码操作方法：**

切换分支：git checkout 8b

![图片](https://uploader.shimo.im/f/Bk2bUDjRvSoSk8pR.png!thumbnail)

![图片](https://uploader.shimo.im/f/aOxdncsfYCsdRdTl.png!thumbnail)

表单详解

[https://docs.djangoproject.com/zh-hans/2.2/ref/forms/fields/](https://docs.djangoproject.com/zh-hans/2.2/ref/forms/fields/)

# 12. DjangoWeb相关功能-表单CSRF防护

**获取课程源码操作方法：**

切换分支：git checkout 8b

![图片](https://uploader.shimo.im/f/mRz4bf7prdE5ceMv.png!thumbnail)

# 13. DjangoWeb相关功能-用户管理认证

**获取课程源码操作方法：**

切换分支：git checkout 8b

![图片](https://uploader.shimo.im/f/jSse1t5mJZBOzUmS.png!thumbnail)

运行以下命令注册用户：

```python
python manage.py shell
from django.contrib.auth.models import User
user = User.objects.create_user('username', 'user@user.com', 'userpassword')
user ###check the user
user.save()
```

# 14. DjangoWeb相关功能-信号

**获取课程源码操作方法：**

切换分支：git checkout 8b

![图片](https://uploader.shimo.im/f/l9nXQE7fFuyTqqdX.png!thumbnail)

![图片](https://uploader.shimo.im/f/yfpXgKNXK0WM5dZ3.png!thumbnail)

# 15. DjangoWeb相关功能-中间件

**获取课程源码操作方法：**

切换分支：git checkout 8b

![图片](https://uploader.shimo.im/f/iLoxiFOQ2lRMHCcN.png!thumbnail)

![图片](https://uploader.shimo.im/f/QtrIIeho2S7t3zDX.png!thumbnail)

# 16. Django相关功能-生产环境部署

**获取课程源码操作方法：**

切换分支：git checkout 8b

![图片](https://uploader.shimo.im/f/HQPJRDmm92u5hP16.png!thumbnail)

![图片](https://uploader.shimo.im/f/RS5xr69aPL24Yeo6.png!thumbnail)

# 17. Django相关功能-celery介绍

**获取课程源码操作方法：**

切换分支：git checkout 9a

![图片](https://uploader.shimo.im/f/MDsHTBwcX1V3NaIu.png!thumbnail)

![图片](https://uploader.shimo.im/f/dHqhixYudkNLWEaD.png!thumbnail)

# 18. Django相关功能-celery定时任务的实现

**获取课程源码操作方法：**

切换分支：git checkout 9a

![图片](https://uploader.shimo.im/f/9UgHmQeESCYPKyEp.png!thumbnail)

![图片](https://uploader.shimo.im/f/n3s9fF8qb62WNHiw.png!thumbnail)

![图片](https://uploader.shimo.im/f/c2JUVJqSWLnhH4v8.png!thumbnail)

![图片](https://uploader.shimo.im/f/tONYRa0xWZmC4WZq.png!thumbnail)

![图片](https://uploader.shimo.im/f/SlaOYd8U8DlDinUh.png!thumbnail)

# 19. Flask上下文与信号

**获取课程源码操作方法：**

切换分支：git checkout 9b

![图片](https://uploader.shimo.im/f/yvvbh6Kn8Ow8dMCW.png!thumbnail)

![图片](https://uploader.shimo.im/f/qTtoD1k7BWLzkle0.png!thumbnail)

# 20. Tornado简介与其他常见网络框架对比

**获取课程源码操作方法：**

切换分支：git checkout 9b

![图片](https://uploader.shimo.im/f/9TPrc9nYLGoRdEon.png!thumbnail)

![图片](https://uploader.shimo.im/f/7nT4qBZ7laTzUlY8.png!thumbnail)

![图片](https://uploader.shimo.im/f/t9EMFvIp8QdOqXM7.png!thumbnail)

# 本周作业

**使用 Django 的 Form、Auth 组件，实现用户登录和密码验证功能。**

**要求：**


1. 登录界面要求能够输入用户名、密码，且密码需大于 8 位。
2. 用户名、密码通过 Django 的 Auth 组件对数据库中预先存储的用户密码进行验证。
3. 如果登录失败提示用户密码错误，登录成功后跳转到首页（或其他非登录的页面）。