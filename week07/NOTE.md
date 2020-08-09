# Python学习笔记Week07 by Santo

# 作业记录： 


1. 类的属性、描述器部分及类的继承通过作业初步了解，待进一步实践熟悉。 
2. 设计模式待实践掌握。。 

# 1. 类属性与对象属性 

**获取课程源码操作方法：** 

切换分支：git checkout 6a 

![图片](https://uploader.shimo.im/f/2KKAPeJHzrBo5APr.png!thumbnail)

![图片](https://uploader.shimo.im/f/TBPizjFWkRABetxd.png!thumbnail)

![图片](https://uploader.shimo.im/f/SCgj15Nu2wlnckVT.png!thumbnail)

# 2. 类的属性作用域 

**获取课程源码操作方法：** 

切换分支：git checkout 6a 

可以为类添加静态字段，直接赋值如Human.newattr=1，newattr 为新的静态字段。 

用__dict__可查看类的属性，也可用dir()查询类的属性，dir()返回的是包含属性名的列表，不含属性值（与__dict__的区别） 

![图片](https://uploader.shimo.im/f/qoiviolDo0qCKjs1.png!thumbnail)

![图片](https://uploader.shimo.im/f/QITQ9fKKPMxN7GWp.png!thumbnail)

().__class__.__bases__[0].__subclasses__() 通过tuple查看类其对应父类的所有子类 

# 3. 类方法描述器 

**获取课程源码操作方法：** 

切换分支：git checkout 6a 

![图片](https://uploader.shimo.im/f/R2wXEYfvIMSZfjra.png!thumbnail)

![图片](https://uploader.shimo.im/f/aMjtNS7Capp50iBi.png!thumbnail)

__init__为Python的初始化函数，__new__为Python的构造函数 

# 4. 静态方法描述器 

**获取课程源码操作方法：** 

切换分支：git checkout 6a 

![图片](https://uploader.shimo.im/f/xc2NoErWmDBnM6nl.png!thumbnail)

# 5. 描述器高级应用__getattribute__ 

**获取课程源码操作方法：** 

切换分支：git checkout 6a 

![图片](https://uploader.shimo.im/f/PLm1TOqyYtCBjuxt.png!thumbnail)

# 6. 描述器高级应用__getattr__ 

**获取课程源码操作方法：** 

切换分支：git checkout 6a 

# 7. 描述器原理&属性描述符 

**获取课程源码操作方法：** 

切换分支：git checkout 6a 

![图片](https://uploader.shimo.im/f/AH6PHBEwXkZNF4tn.png!thumbnail)

![图片](https://uploader.shimo.im/f/QxioxVSkGKOS7Src.png!thumbnail)

__get__ [https://docs.python.org/3/reference/datamodel.html#object.__get__](https://docs.python.org/3/reference/datamodel.html#object.__get__)

__set__ [https://docs.python.org/3/reference/datamodel.html#object.__set__](https://docs.python.org/3/reference/datamodel.html#object.__set__)

__delete__ [https://docs.python.org/3/reference/datamodel.html#object.__delete__](https://docs.python.org/3/reference/datamodel.html#object.__delete__)

@property [https://docs.python.org/3/library/functions.html#property](https://docs.python.org/3/library/functions.html#property)

# 8. 面向对象编程-继承 

**获取课程源码操作方法：** 

切换分支：git checkout 6a 

![图片](https://uploader.shimo.im/f/CiHLURCT8i3Jbl4V.png!thumbnail)

![图片](https://uploader.shimo.im/f/TqVBP97w8o0QUDQr.png!thumbnail)

![图片](https://uploader.shimo.im/f/w9KYvEaPaIHmyai4.png!thumbnail)

![图片](https://uploader.shimo.im/f/HcPHW3lgH520tfLJ.png!thumbnail)

# 9. solid设计原则与设计模式&单例模式 

**获取课程源码操作方法：** 

切换分支：git checkout 6a 

![图片](https://uploader.shimo.im/f/TR09dUhnfOgBlQgw.png!thumbnail)

![图片](https://uploader.shimo.im/f/HSANOa68yFdZE8jG.png!thumbnail)

![图片](https://uploader.shimo.im/f/9K21l4Dyc4AGkLuI.png!thumbnail)

# 10. 工厂模式 

**获取课程源码操作方法：** 

切换分支：git checkout 6a 

# 11. 元类 

**获取课程源码操作方法：** 

切换分支：git checkout 6a 

![图片](https://uploader.shimo.im/f/BSaJ5sCMFvk5r2yM.png!thumbnail)

![图片](https://uploader.shimo.im/f/z3M5Mi9BoNrlDAPX.png!thumbnail)

# 12. mixin模式 

**获取课程源码操作方法：** 

切换分支：git checkout 6a 

![图片](https://uploader.shimo.im/f/8d0GfiMR4wXgDdZv.png!thumbnail)

# 本周作业 

**背景：** 在使用 Python 进行《我是动物饲养员》这个游戏的开发过程中，有一个代码片段要求定义动物园、动物、猫三个类。 

这个类可以使用如下形式为动物园增加一只猫： 

```python
if __name__ == '__main__': 
    # 实例化动物园 
    z = Zoo('时间动物园') 
    # 实例化一只猫，属性包括名字、类型、体型、性格 
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺') 
    # 增加一只猫到动物园 
    z.add_animal(cat1) 
    # 动物园是否有猫这种动物 
    have_cat = getattr(z, 'Cat') 
```

# 
**具体要求：** 


1. 定义“动物”、“猫”、“动物园”三个类，动物类不允许被实例化。 
2. 动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。 
3. 猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，猫类继承自动物类。 
4. 动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。 

