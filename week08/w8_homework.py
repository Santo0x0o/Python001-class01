# Homework1
# 容器序列：list, tuple, dict, collections.deque
# 扁平序列：str
# 可变序列：list, dict, collections.deque
# 不可变序列：str, tuple


# Homework2
def new_map(func, arglist):
    for i in arglist:
        yield func(i)


def add_one(n):
    return n+1


# Test
test_list = [1, 3, 5, 7, 9]
new_list = list(new_map(add_one, test_list))
print(new_list)


# Homework3
import time


def timer(func):
    def inner(*args, **kwargs):
        s = time.time()
        res = func(*args, **kwargs)
        t = time.time()
        diff = t-s
        print(f'The running time is {diff} s')
        return res
    return inner


@timer
def test_timer(a, b, c=3, d=4):
    total = a+b*c-d
    return total


print(test_timer(1, 2, c=5, d=3))
