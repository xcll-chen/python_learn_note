"""列表list
    相关关键词：list（）
    主要是了解容器型变量的运算
"""
items1 = [35, 12, 99, 68, 55, 35, 87]
items2 = ['Python', 'Java', 'Go', 'Kotlin']
items3 = [100, 12.3, 'Python', True]
print(items1)  # [35, 12, 99, 68, 55, 35, 87]
print(items2)  # ['Python', 'Java', 'Go', 'Kotlin']
print(items3)  # [100, 12.3, 'Python', True]        列表内的变量类型不唯一

#list()函数，可以将其他东西换成列表
items4 = list(range(1,55))
items5 = list('hell0')

print(items4)
print(items5)

#列表运算 +实现两个列表的拼接，*可以实现列表次数的变化，in,not in 可以判断数据是否在列表中，返回bool值
items5 = [35, 12, 99, 45, 66]
items6 = [45, 58, 29]
items7 = ['Python', 'Java', 'JavaScript']
print(items5 + items6)
print(items6 + items7)
print(items5 * 5 )
print(99 in items5)
print(20 in items5)
print('C++' not in items7)

#使用[i]可以访问列表中的元素，正向索引是0～n-1，逆向索引为-1到-n，-1是最后一个元素
#上面是访问一个元素，但是我们会存在访问多个元素，所以就可以使用切片操作[start:end:stride]
items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
print(items8[0])   # apple
print(items8[2])   # pitaya
print(items8[4])   # watermelon

print(items8[1:3:1])    #取中间三个元素
print(items8[0::2])     #隔一个取一个
print(items8[-1:-6:-2])  #倒着取隔2个取一个

#列表的遍历除了能够对索引进行运算，采用for-in结构，第二个方法直接列表循环
for index in range(0,len(items8)):
    print(items8[index])

for item in items8:
    print(item)

import random

counters = [0] * 6
# 模拟掷色子记录每种点数出现的次数
for _ in range(6000):
    face = random.randrange(1, 7)
    counters[face - 1] += 1
# 输出每种点数出现的次数
for face in range(1, 7):
    print(f'{face}点出现了{counters[face - 1]}次')

# append（）追加元素
# insert（1，‘C++’）插入指定位置指定元素
# remove（）删除指定元素。而且是这个元素出现的第一个，
# pop()默认删除最后一个元素，也可以指定一个位置，删除指定位置的元素,删除的元素会被得到，所以有赋值操作
# del关键字也能实现删除，del languages[1]但是不会返回值。性能略优
# clear（）会清空列表

languages = ['Python', 'Java', 'C++']
languages.append('JavaScript')
languages.insert(1,'SQL')
print(languages)

temp = languages.pop(3)
print(temp)
print(languages)

languages.clear()
print(languages)

languages = ['Python', 'Java', 'C++','Python', 'Java', 'C++']
languages.remove('Python')
print(languages)

#index是索引元素的位置，也可以从指定位置开始索引元素，返回元素位置，若找不到会发生Value Error
#count是记录元素的次数
items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
print(items.index('Python'))     # 0
# 从索引位置1开始查找'Python'
print(items.index('Python', 1))  # 5
print(items.count('Python'))     # 2
print(items.count('Kotlin'))     # 1
print(items.count('Swfit'))      # 0
# 从索引位置3开始查找'Java'
#print(items.index('Java', 3))    # ValueError: 'Java' is not in list

#sort（）可以实现排序，reverse()可以实现反转
items = ['Python', 'Java', 'C++', 'Kotlin', 'Swift']
items.sort()
print(items)  # ['C++', 'Java', 'Kotlin', 'Python', 'Swift']
items.reverse()
print(items)  # ['Swift', 'Python', 'Kotlin', 'Java', 'C++']

#列表生成式
num1 = [11,22,33,44,55,66]
num2 = []
for num in num1:
    num2.append(num ** 2)
print(num2)
num2.clear()
#强烈建议使用列表生成式，代码简洁高效
num2 = [num ** 2 for num in num1]
print(num2)

num3 = [num for num in num1 if num % 2 == 0]
print(num3)

import random

scores = [[random.randrange(60, 101) for _ in range(3)] for _ in range(5)]
print(scores)

"""
双色球随机选号程序

Author: 骆昊
Version: 1.0
"""
import random

red_balls = list(range(1, 34))
print(red_balls)
selected_balls = []
# 添加6个红色球到选中列表
for _ in range(6):
    # 生成随机整数代表选中的红色球的索引位置
    index = random.randrange(len(red_balls))
    # 将选中的球从红色球列表中移除并添加到选中列表
    selected_balls.append(red_balls.pop(index))
# 对选中的红色球排序
selected_balls.sort()
# 输出选中的红色球
for ball in selected_balls:
    print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
# 随机选择1个蓝色球
blue_ball = random.randrange(1, 17)
# 输出选中的蓝色球
print(f'\033[034m{blue_ball:0>2d}\033[0m')