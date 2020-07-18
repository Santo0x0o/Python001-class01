# Python学习笔记Week03 by Santo

# 作业记录

1. argparse中[metavar](https://docs.python.org/zh-cn/3.7/library/argparse.html#metavar)的作用待了解！

[https://docs.python.org/zh-cn/3.7/library/argparse.html#metavar](https://docs.python.org/zh-cn/3.7/library/argparse.html#metavar)

1. 使用yield from, Python3.3新出现的句法替代内层for循环

[https://www.jianshu.com/p/87da832730f5](https://www.jianshu.com/p/87da832730f5)

1. 进程锁暂未用上，待温习老师内容，再实践。
2. 作业贴图

ping测试结果：

![图片](https://uploader.shimo.im/f/bmkEDzLNrUM4RHAa.png!thumbnail)

![图片](https://uploader.shimo.im/f/7V38YzgIWlmL0vrC.png!thumbnail)

tcp 测试结果

![图片](https://uploader.shimo.im/f/Wxaa0TcNonFvUQY4.png!thumbnail)

![图片](https://uploader.shimo.im/f/eZprSxVacwbkXDeT.png!thumbnail)











# 1. Scrapy 并发参数优化原理

**1. 获取课程源码操作方法：**

切换分支：git checkout 3c

**2. Twisted 学习参考文档：**

[https://pypi.org/project/Twisted/](https://pypi.org/project/Twisted/)

**3. asyncio — 异步 I/O 学习文档**

[https://docs.python.org/zh-cn/3.7/library/asyncio.htm](https://docs.python.org/zh-cn/3.7/library/asyncio.html)

# 2. 多进程：进程的创建

**1. 获取课程源码操作方法：**

切换分支：git checkout 3c

**2. os 模块学习文档：**

[https://docs.python.org/zh-cn/3.7/tutorial/stdlib.html#operating-system-interface](https://docs.python.org/zh-cn/3.7/tutorial/stdlib.html#operating-system-interface)

**3. multiprocessing – 基于进程的并行学习文档：**[ https://docs.python.org/zh-cn/3.7/library/multiprocessing.html](https://docs.python.org/zh-cn/3.7/library/multiprocessing.html)

# 3. 多进程：多进程程序调试技巧

**1. 获取课程源码操作方法：**

切换分支：git checkout 3c

**2. 补充说明：**

课程中 18 分 11 秒处，应更改为 进程 0 1 是当前进程的子进程

#Windows下运行p6_class.py报错

```python
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "D:\ProgramData\Anaconda3\lib\multiprocessing\spawn.py", line 105, in spawn_main
    exitcode = _main(fd)
Traceback (most recent call last):
  File "D:\ProgramData\Anaconda3\lib\multiprocessing\spawn.py", line 114, in _main
  File "<string>", line 1, in <module>
    prepare(preparation_data)
  File "D:\ProgramData\Anaconda3\lib\multiprocessing\spawn.py", line 225, in prepare
  File "D:\ProgramData\Anaconda3\lib\multiprocessing\spawn.py", line 105, in spawn_main
    _fixup_main_from_path(data['init_main_from_path'])
    exitcode = _main(fd)
  File "D:\ProgramData\Anaconda3\lib\multiprocessing\spawn.py", line 277, in _fixup_main_from_path
  File "D:\ProgramData\Anaconda3\lib\multiprocessing\spawn.py", line 114, in _main
    run_name="__mp_main__")
    prepare(preparation_data)
  File "D:\ProgramData\Anaconda3\lib\runpy.py", line 263, in run_path
  File "D:\ProgramData\Anaconda3\lib\multiprocessing\spawn.py", line 225, in prepare
    pkg_name=pkg_name, script_name=fname)
  File "D:\ProgramData\Anaconda3\lib\runpy.py", line 96, in _run_module_code
    _fixup_main_from_path(data['init_main_from_path'])
    mod_name, mod_spec, pkg_name, script_name)
  File "D:\ProgramData\Anaconda3\lib\multiprocessing\spawn.py", line 277, in _fixup_main_from_path
  File "D:\ProgramData\Anaconda3\lib\runpy.py", line 85, in _run_code
    run_name="__mp_main__")
  File "D:\ProgramData\Anaconda3\lib\runpy.py", line 263, in run_path
    exec(code, run_globals)
  File "d:\Learning\Coding\Python\pythontrain\1进程\p6_class.py", line 18, in <module>
    pkg_name=pkg_name, script_name=fname)
  File "D:\ProgramData\Anaconda3\lib\runpy.py", line 96, in _run_module_code
    p.start()
    mod_name, mod_spec, pkg_name, script_name)
  File "D:\ProgramData\Anaconda3\lib\multiprocessing\process.py", line 112, in start
  File "D:\ProgramData\Anaconda3\lib\runpy.py", line 85, in _run_code
    self._popen = self._Popen(self)
  File "D:\ProgramData\Anaconda3\lib\multiprocessing\context.py", line 223, in _Popen
    exec(code, run_globals)
  File "d:\Learning\Coding\Python\pythontrain\1进程\p6_class.py", line 18, in <module>
    return _default_context.get_context().Process._Popen(process_obj)
  File "D:\ProgramData\Anaconda3\lib\multiprocessing\context.py", line 322, in _Popen
    p.start()
  File "D:\ProgramData\Anaconda3\lib\multiprocessing\process.py", line 112, in start
    return Popen(process_obj)
    self._popen = self._Popen(self)
  File "D:\ProgramData\Anaconda3\lib\multiprocessing\popen_spawn_win32.py", line 46, in __init__
  File "D:\ProgramData\Anaconda3\lib\multiprocessing\context.py", line 223, in _Popen
    prep_data = spawn.get_preparation_data(process_obj._name)
  File "D:\ProgramData\Anaconda3\lib\multiprocessing\spawn.py", line 143, in get_preparation_data
    return _default_context.get_context().Process._Popen(process_obj)
  File "D:\ProgramData\Anaconda3\lib\multiprocessing\context.py", line 322, in _Popen
    _check_not_importing_main()
  File "D:\ProgramData\Anaconda3\lib\multiprocessing\spawn.py", line 136, in _check_not_importing_main
    return Popen(process_obj)
    is not going to be frozen to produce an executable.''')
  File "D:\ProgramData\Anaconda3\lib\multiprocessing\popen_spawn_win32.py", line 46, in __init__
RuntimeError:
        An attempt has been made to start a new process before the
        current process has finished its bootstrapping phase.
        This probably means that you are not using fork to start your
        child processes and you have forgotten to use the proper idiom
        in the main module:
            if __name__ == '__main__':
                freeze_support()
                ...
        The "freeze_support()" line can be omitted if the program
        is not going to be frozen to produce an executable.    prep_data = spawn.get_preparation_data(process_obj._na
  File "D:\ProgramData\Anaconda3\lib\multiprocessing\spawn.py", line 143, in get_preparation_data
    _check_not_importing_main()
  File "D:\ProgramData\Anaconda3\lib\multiprocessing\spawn.py", line 136, in _check_not_importing_main
    is not going to be frozen to produce an executable.''')
RuntimeError:
        An attempt has been made to start a new process before the
        An attempt has been made to start a new process before the
        child processes and you have forgotten to use the proper idiom
        in the main module:
            if __name__ == '__main__':
                freeze_support()
                ...
        The "freeze_support()" line can be omitted if the program
        is not going to be frozen to produce an executable.
```

# 4. 多进程：使用队列实现进程间的通信

**1. 获取课程源码操作方法：**

切换分支：git checkout 3c

**2. 进程之间的两种通信通道：**

[https://docs.python.org/zh-cn/3.7/library/multiprocessing.html#exchanging-objects-between-processes](https://docs.python.org/zh-cn/3.7/library/multiprocessing.html#exchanging-objects-between-processes)

# 5. 多进程：管道共享内存

**1. 获取课程源码操作方法：**

切换分支：git checkout 3c

**2. 进程之间的两种通信通道：**

[https://docs.python.org/zh-cn/3.7/library/multiprocessing.html#exchanging-objects-between-processes](https://docs.python.org/zh-cn/3.7/library/multiprocessing.html#exchanging-objects-between-processes)

**3. 管道和队列参考文档：**

[https://docs.python.org/zh-cn/3.7/library/multiprocessing.html#pipes-and-queues](https://docs.python.org/zh-cn/3.7/library/multiprocessing.html#pipes-and-queues)

# 6. 多进程：锁机制解决资源抢占

**1. 获取课程源码操作方法：**

切换分支：git checkout 3c

**2. 进程间的同步学习文档：**

[https://docs.python.org/zh-cn/3.7/library/multiprocessing.html#synchronization-between-processes](https://docs.python.org/zh-cn/3.7/library/multiprocessing.html#synchronization-between-processes)

# 7. 多进程：进程池

**1. 获取课程源码操作方法：**

切换分支：git checkout 3c

**2. 进程池学习文档：**

[https://docs.python.org/zh-cn/3.7/library/multiprocessing.html#module-multiprocessing.pool](https://docs.python.org/zh-cn/3.7/library/multiprocessing.html#module-multiprocessing.pool)

**3. 迭代器学习文档：**

[https://docs.python.org/zh-cn/3.7/library/stdtypes.html#iterator-types](https://docs.python.org/zh-cn/3.7/library/stdtypes.html#iterator-types)

# 8. 多线程：创建线程

**1. 获取课程源码操作方法：**

切换分支：git checkout 3c

**2. 基于线程的并行学习文档：**

[https://docs.python.org/zh-cn/3.7/library/threading.html](https://docs.python.org/zh-cn/3.7/library/threading.html)

**3. 基于进程的并行学习文档：**

[https://docs.python.org/zh-cn/3.7/library/multiprocessing.html](https://docs.python.org/zh-cn/3.7/library/multiprocessing.html)

**4. 底层多线程 API：**

[https://docs.python.org/zh-cn/3.7/library/_thread.html](https://docs.python.org/zh-cn/3.7/library/_thread.html)

# 9. 多线程：线程锁

**1. 获取课程源码操作方法：**

切换分支：git checkout 3c

**2. 锁对象学习文档：**

[https://docs.python.org/zh-cn/3.7/library/threading.html#lock-objects](https://docs.python.org/zh-cn/3.7/library/threading.html#lock-objects)

**3. 递归锁对象：**

[https://docs.python.org/zh-cn/3.7/library/threading.html#rlock-objects](https://docs.python.org/zh-cn/3.7/library/threading.html#rlock-objects)

# 10. 多线程：队列

**1. 获取课程源码操作方法：**

切换分支：git checkout 3c

2. queue 学习文档：

[https://docs.python.org/zh-cn/3.7/library/queue.html](https://docs.python.org/zh-cn/3.7/library/queue.html)

# 11. 多线程：线程池

**1. 获取课程源码操作方法：**

切换分支：git checkout 3c

**2. concurrent.futures - 线程池执行器：**[ https://docs.python.org/zh-cn/3.7/library/concurrent.futures.html#threadpoolexecutor](https://docs.python.org/zh-cn/3.7/library/concurrent.futures.html#threadpoolexecutor)

**3. concurrent.futures - 进程池执行器：**

[https://docs.python.org/zh-cn/3.7/library/concurrent.futures.html#processpoolexecutor](https://docs.python.org/zh-cn/3.7/library/concurrent.futures.html#processpoolexecutor)

# 12. 多线程：GIL 锁与多线程的性能瓶颈

**1. 获取课程源码操作方法：**

切换分支：git checkout 3c

![图片](https://uploader.shimo.im/f/cXyl5ShYsgtyJl8u.png!thumbnail)

多线程在I/O密集型场景下优势较大

# 13. 迷你 Scrapy 项目实践

1. 获取课程源码操作方法：

切换分支：git checkout 3c

# 本周作业

**作业一：**

背景： 网络安全工具中有一个常用软件称作端口扫描器，即通过一台主机发起向另一主机的常用端口发起连接，探测目标主机是否开放了指定端口（1-1024），用于改善目标主机的安全状况。

**要求：编写一个基于多进程或多线程模型的主机扫描器。**

1. 使用扫描器可以基于 ping 命令快速检测一个 IP 段是否可以 ping 通，如果可以 ping 通返回主机 IP，如果无法 ping 通忽略连接。
2. 使用扫描器可以快速检测一个指定 IP 地址开放了哪些 tcp 端口，并在终端显示该主机全部开放的端口。
3. IP 地址、使用 ping 或者使用 tcp 检测功能、以及并发数量，由命令行参数传入。
4. 需考虑网络异常、超时等问题，增加必要的异常处理。
5. 因网络情况复杂，避免造成网络拥堵，需支持用户指定并发数量。

**命令行参数举例如下：**

`pmap.py -n 4 -f ping -ip 192.168.0.1-192.168.0.100`

`pmap.py -n 10 -f tcp -ip 192.168.0.1 -w result.json`

**说明：**

1. 因大家学习的操作系统版本不同，建立 tcp 连接的工具不限，可以使用 telnet、nc 或 Python 自带的 socket 套接字。
2. -n：指定并发数量。
3. -f ping：进行 ping 测试
4. -f tcp：进行 tcp 端口开放、关闭测试。
5. -ip：连续 IP 地址支持 192.168.0.1-192.168.0.100 写法。
6. -w：扫描结果进行保存。

**选做：**

1. 通过参数 [-m proc|thread] 指定扫描器使用多进程或多线程模型。
2. 增加 -v 参数打印扫描器运行耗时 (用于优化代码)。
3. 扫描结果显示在终端，并使用 json 格式保存至文件。

**作业二：（选做）**

**背景： **在数据分析的完整流程中 (数据收集、存储、清洗、展示)，数据收集的多少对最终分析结果有着直接影响，因此需要对外网的数据进行收集并整理，用于支持后续的分析。

**要求：**改造基于 requests 爬虫，增加多线程功能，实现通过拉勾网，获取 北、上、广、深四地 Python 工程师的平均薪水待遇，并将获取结果存入数据库。

1. 通过多线程实现 requests 库的多线程方式。
2. 获取北京、上海、广州、深圳四个地区，各地区 100 个 Python 工程师职位的职位名称和薪资水平。
3. 相同地区、相同职位及相同待遇的职位需去重。
4. 将获取的内容存入数据库中。

**选做：**

1. 使用图形库展示各地区 Python 工程师薪资分布情况，使用不同颜色代表该地区 Python 工程师薪资高低情况（建议使用 echart 或 matplotlib，具体图形库不限）。

**说明：**

1. 如果网页提示“操作太频繁”等提示，需清理 cookie ，重新获取 URL，降低频率或采用其他反爬虫方式解决。
2. 禁止爬取网站中的个人信息。

 

