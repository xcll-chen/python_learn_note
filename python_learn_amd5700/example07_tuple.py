"""
tuple是一种容器型变量,但是他是一种不可变
"""

#定义
# 定义一个三元组
t1 = (35, 12, 98)
# 定义一个四元组
t2 = ('骆昊', 45, True, '四川成都')

#注意定义单个元素为元组时需要后面加逗号
# 查看变量的类型
print(type(t1))  # <class 'tuple'>
print(type(t2))  # <class 'tuple'>
print(len(t1))
#索引
print(t1[1])
#切片索引
print(t2[0:3:2])
#拼接
t3 = t1+t2
print(t3)
#比较

#打包与解包
#如果解包出来的元素个数和变量个数不对应，会引发ValueError异常
print(t1 == t3)
a = 1, 10, 100
print(type(a))  # <class 'tuple'>
print(a)        # (1, 10, 100)
# 解包操作
i, j, k = a
print(i, j, k)  # 1 10 100

#python中交换变量值可以不用借助第三变量
t1,t2 = t2,t1
print(f"{t1}and{t2}")