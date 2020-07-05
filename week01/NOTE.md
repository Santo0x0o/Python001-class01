### Python学习笔记Week01 by Santo

### 作业心得

1. 爬取数据限制为10条记录，可在同一个页面爬取处理，只取30条记录中的前10条。
2. BeautifulSoup库除find_all, find方法还有其他如find_parent等，还是要多看相关库定义了解其丰富功能和用法。
3. 作业2改造pipeline进一步理解了pipeline按每个item处理的机制。
4. scrapy crawl spiders --nolog增加的nolog参数会把scrpy运行加载的日志等去掉，爬虫本身的错误也会被过滤。
5. selector通过xpath参数过滤后返回的对象需进一步处理提取其中的文本，通过extract()、extract_first()方法可实现。待确认extract()具体定义。



附笔记：

# 1. 用requests写一个最简单的爬虫

### **requests 官方文档链接**：[ https://requests.readthedocs.io/zh_CN/latest/](https://requests.readthedocs.io/zh_CN/latest/)

### **获取课程源码操作方法**

  * git clone [https://github.com/wilsonyin123/geekbangtrain.git](https://github.com/wilsonyin123/geekbangtrain.git)
* cd geekbangtrain
* git checkout 1a

提出需求

编码

代码run起来

修复、完善

# ![图片](https://uploader.shimo.im/f/CrZB27P1FnQU7Ma1.png!thumbnail)2. 使用BeautifulSoup解析爬取到的网页

### **Beautiful Soup 官方文档链接：**[ https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/)

### **获取课程源码操作方法**

切换分支：git checkout 1b

# 3. 使用XPath解析网页

### **获取课程源码操作方法**

切换分支：git checkout 1c

# 4. 实现爬虫的自动翻页功能

# 5. Python基础语法回顾

### **python 基础语法**

* Python 简介： [https://docs.python.org/zh-cn/3.7/tutorial/introduction.html](https://docs.python.org/zh-cn/3.7/tutorial/introduction.html)
* Python 数据结构： [https://docs.python.org/zh-cn/3.7/tutorial/datastructures.html](https://docs.python.org/zh-cn/3.7/tutorial/datastructures.html)
* Python 其他流程控制工具 :[ https://docs.python.org/zh-cn/3.7/tutorial/controlflow.html](https://docs.python.org/zh-cn/3.7/tutorial/controlflow.html)
* Python 中的类：[ https://docs.python.org/zh-cn/3.7/tutorial/classes.html](https://docs.python.org/zh-cn/3.7/tutorial/classes.html)
* Python 定义函数：[ https://docs.python.org/zh-cn/3.7/tutorial/controlflow.html#defining-functions](https://docs.python.org/zh-cn/3.7/tutorial/controlflow.html#defining-functions)

### Python关键字

![图片](https://uploader.shimo.im/f/p83eTXuoIiUutyoI.png!thumbnail)

### 基本数据类型

![图片](https://uploader.shimo.im/f/bjm1ikfhHzRAOdUv.png!thumbnail)

推导式

![图片](https://uploader.shimo.im/f/nGkKojm8NmhPNXXc.png!thumbnail)

# 6. 前端基础：HTML基本结构

**W3C 标准：**

[https://www.w3.org/standards/](https://www.w3.org/standards/)

![图片](https://uploader.shimo.im/f/Ext9UJYF5Gc9mp4f.png!thumbnail)

W3C定义了网页的结构、表现、行为。

# 7. 前端基础：HTTP协议

HTML协议的标签：

a、span、img

# 8. Scrapy框架结构解析

Scrapy 架构官方文档介绍：[ https://docs.scrapy.org/en/latest/topics/architecture.html](https://docs.scrapy.org/en/latest/topics/architecture.html)

![图片](https://uploader.shimo.im/f/6hJKn9iljQ3ZucSV.png!thumbnail)

![图片](https://uploader.shimo.im/f/yv8riFanGkZnRaD3.png!thumbnail)

![图片](https://uploader.shimo.im/f/HVkUtRLyLEaHUoNr.png!thumbnail)

![图片](https://uploader.shimo.im/f/de5VsIE7bHF14XQU.png!thumbnail)

# 9. Scrapy爬虫目录结构解析

**获取课程源码操作方法**

切换分支：git checkout 2a

![图片](https://uploader.shimo.im/f/iyHT2Q0kW7BeBFDB.png!thumbnail)

scrapy startproject spiders # create project *spiders*

cd spiders

scrapy genspider maoyan maoyan.com # generate spider maoyan in domain maoyan.com

# 10. 将requests爬虫改写为Scrapy爬虫

**获取课程源码操作方法**

切换分支：git checkout 2b

scrapy crawl maoyan # start the spider, maoyan is the name of spider

# 11. 通过Scrapy爬虫爬取电影详情页信息

**获取课程源码操作方法**

切换分支：git checkout 2b

# 12. XPath详解

**1. 获取课程源码操作方法**

切换分支：git checkout 2c

**2. Scrapy Xpath 官方学习文档：**[ https://docs.scrapy.org/en/latest/topics/selectors.html#working-with-xpaths](https://docs.scrapy.org/en/latest/topics/selectors.html#working-with-xpaths)

**3. Xpath 中文文档：**

[https://www.w3school.com.cn/xpath/index.asp](https://www.w3school.com.cn/xpath/index.asp)

**4. Xpath 英文文档：**

[https://www.w3.org/TR/2017/REC-xpath-31-20170321/#nt-bnf](https://www.w3.org/TR/2017/REC-xpath-31-20170321/#nt-bnf)

**5. 补充说明：**

1. 12 分 32 秒处“打印的选择器信息用 **元祖** 括起来”，此处有一点小的问题，相信细心的同学已经察觉到了，注意我们需把 **元祖** 改成 **列表**。
2. 18 分 18 秒处视频中讲述 “ dont_filter 设置为 True 后，不会受到 allowed_domains 的限制”。更正为 dont_filter 设置为 True，是用来解除去重功能。Scrapy 自带 url 去重功能，第二次请求之前会将已发送的请求自动进行过滤处理。所以将 dont_filter 设置为 True 起到的作用是解除去重功能，一旦设置成重 True，将不会去重，直接发送请求。
3. 相信细心的同学们已经发现了这些小问题，稍后我们会对课程及视频进行相应的修订，望周知哦！

# 13. yield与推导式

**1. 获取课程源码操作方法**

切换分支：git checkout 2d

**2. yield 表达式官方文档：**

[https://docs.python.org/zh-cn/3.7/reference/expressions.html#yieldexpr](https://docs.python.org/zh-cn/3.7/reference/expressions.html#yieldexpr)

**3. yield 语句官方文档**

[https://docs.python.org/zh-cn/3.7/reference/simple_stmts.html#yield](https://docs.python.org/zh-cn/3.7/reference/simple_stmts.html#yield)

**4. Python 推导式官方文档：**

[https://docs.python.org/zh-cn/3.7/tutorial/datastructures.html#list-comprehensions](https://docs.python.org/zh-cn/3.7/tutorial/datastructures.html#list-comprehensions)

**5. 补充说明：**

视频中老师所讲 yield 返回的是单独的一个值，更准确的说返回的值必须是对象，在此章节我们暂定只把它理解返回一个值。在后面的章节多线程部分，我们会结合课程再对 yield 进行详解。

# 本周作业

**作业一：**

安装并使用 requests、bs4 库，爬取[猫眼电影](https://maoyan.com/films?showType=3)的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。

**作业二：**

使用 Scrapy 框架和 XPath 抓取[猫眼电影](https://maoyan.com/films?showType=3)的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。

**要求：**必须使用 Scrapy 框架及其自带的 item pipeline、选择器功能，不允许使用 bs4 进行页面内容的筛选