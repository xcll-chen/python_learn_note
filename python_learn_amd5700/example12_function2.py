def is_even(num):
    """判断num是不是偶数"""
    return num % 2 == 0


def square(num):
    """求平方"""
    return num ** 2


old_nums = [35, 12, 8, 99, 60, 52]
new_nums = list(map(square, filter(is_even, old_nums)))
print(new_nums)  

old_strings = ['in', 'apple', 'zoo', 'waxberry', 'pear']
new_strings = sorted(old_strings)
print(new_strings)  # ['apple', 'in', 'pear', waxberry', 'zoo']

old_strings = ['in', 'apple', 'zoo', 'waxberry', 'pear']
new_strings = sorted(old_strings, key=len)

print(new_strings)  # ['in', 'zoo', 'pear', 'apple', 'waxberry']

import random
import time

from functools import wraps


def record_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间: {end - start:.2f}秒')
        return result
    return wrapper


@record_time
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')


@record_time
def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')


# 调用装饰后的函数会记录执行时间
download('MySQL从删库到跑路.avi')
upload('Python从入门到住院.pdf')
# 取消装饰器的作用不记录执行时间
download.__wrapped__('MySQL必知必会.pdf')
upload.__wrapped__('Python从新手到大师.pdf')

def fib1(n):
    if n in (1, 2):
        return 1
    return fib1(n - 1) + fib1(n - 2)


for i in range(1, 51):
    print(fib1(i))