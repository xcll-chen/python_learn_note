# 通过关键字def定义求阶乘的函数
# 自变量（参数）num是一个非负整数
# 因变量（返回值）是num的阶乘
"""
def fac(num):
    result = 1
    for n in range(2, num + 1):
        result *= n
    return result

m = int(input('m = '))
n = int(input('n = '))

# 计算C(M,N)的值
print(fac(m) // fac(n) // fac(m - n))

"""
#位置参数，就是按照位置指定的地方进行传参
def make_judgement(a,b,c):
    print(f"a = {a},b = {b},c = {c}")
    return a+b>c and b+c>a and a+c>b

print(make_judgement(1,2,3))
print(make_judgement(5,4,3))

#如果对于不想按照位置传参，可以采用关键字参数。通过“参数名 = 参数值”形式进行传参
print(make_judgement(c = 1, b = 2,a = 3))

#在定义函数可以通过参数列表用/设置强制位置参数  用*设置命名关键字参数 也就是说强制位置参数只能通过位置进行传参，
#通过*设置的命名关键字传参，只能通过参数名=参数值的方式进行传参。（强制位置参数是python3.8引入的）

#参数默认值，带默认值的参数必须放在不带默认值的参数之后
#要骰子的程序
from random import randrange

# 定义摇色子的函数
# 函数的自变量（参数）n表示色子的个数，默认值为2
# 函数的因变量（返回值）表示摇n颗色子得到的点数
def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randrange(1, 7)
    return total


# 如果没有指定参数，那么n使用默认值2，表示摇两颗色子
print(roll_dice())
# 传入参数3，变量n被赋值为3，表示摇三颗色子获得点数
print(roll_dice(3))

#可变参数，就是可以通过*在调用函数时传入0个或者任意个参数
# 调用函数时传入的n个参数会组装成一个n元组赋给args
# 如果一个参数都没有传入，那么args会是一个空元组
def add(*args):
    total = 0
    # 对保存可变参数的元组进行循环遍历
    for val in args:
        # 对参数进行了类型检查（数值型的才能求和）
        if type(val) in (int, float):
            total += val
    return total


# 在调用add函数时可以传入0个或任意多个参数
print(add())         # 0
print(add(1))        # 1
print(add(1, 2, 3))  # 6
print(add(1, 2, 'hello', 3.45, 6))  # 12.45

#如果是想传入多个关键字参数，就需要使用**kwargs的形式，kwargs是一个字典，保存了所有的关键字参数
def person(name, age, **kwargs):
    print(f"name = {name}, age = {age}, other = {kwargs}")

person("Alice", 25, city="Beijing", job="Engineer")

##因为给变量以及函数命名很痛苦，切容易冲突。所以每个python文件下都代表一个模块
#通过import导入模块利用模块名.函数名来区分函数

import module1
import module2

module1.foo()  # 调用module1模块中的foo函数
module2.foo()  # 调用module2模块中的foo函数

#当然也可以直接导入需要的函数，
from module1 import foo as foo1
from module2 import foo as foo2 
foo1()  # 调用module1模块中的foo函数
foo2()  # 调用module2模块中的foo函数