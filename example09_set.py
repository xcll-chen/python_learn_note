""""
    集合
    集合和列表的区别就是集合是无序性，当然也就造就了集合的不可索引，元素只能被判断是否存在与这个集合中（in，not in）
    同时集合存在糊异性，也就是元素只能在集合中存在一个
    所以集合就是一个确定的，范围内的整体
"""

#创建集合有两种方式
#通过{}来创建集合，以及通过set()函数来创建集合
set1 = {1, 2, 3, 3, 3, 2}
print(set1)

set2 = {'banana', 'pitaya', 'apple', 'apple', 'banana', 'grape'}
print(set2)

set3 = set('hello')
print(set3)

set4 = set([1, 2, 2, 3, 3, 3, 2, 1])
print(set4)
#生成式语法
set5 = {num for num in range(1, 20) if num % 3 == 0 or num % 7 == 0}
print(set5)

#当遍历整个集合时会发现集合的无序性，每次输出结果不一样
set1 = {'Python', 'C++', 'Java', 'Kotlin', 'Swift'}
for elem in set1:
    print(elem)

"""
    集合的运算有很多，成员运算，交并差集运算，比较运算
    成员运算主要是in， not in
    交集 &。并集 ｜。 差集 -  对称差 ^
"""
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}

# 交集
print(set1 & set2)                      # {2, 4, 6}
print(set1.intersection(set2))          # {2, 4, 6}

# 并集
print(set1 | set2)                      # {1, 2, 3, 4, 5, 6, 7, 8, 10}
print(set1.union(set2))                 # {1, 2, 3, 4, 5, 6, 7, 8, 10}

# 差集
print(set1 - set2)                      # {1, 3, 5, 7}
print(set1.difference(set2))            # {1, 3, 5, 7}
print(set2 - set1)

# 对称差
print(set1 ^ set2)                      # {1, 3, 5, 7, 8, 10}
print(set1.symmetric_difference(set2))  # {1, 3, 5, 7, 8, 10}

"""
    运算符可以看的更加直接，同时也可以和赋值运算构成更直观简洁的代码
    同时也有
"""
set1 = {1, 3, 5, 7}
set2 = {2, 4, 6}
set1 |= set2
# set1.update(set2)
print(set1)  # {1, 2, 3, 4, 5, 6, 7}
set3 = {3, 6, 9}
set1 &= set3
# set1.intersection_update(set3)
print(set1)  # {3, 6}
set2 -= set1
# set2.difference_update(set1)
print(set2)  # {2, 4}

"""
    比较运算
    判断==或者是！=两种关系
    判断子集以及超集，如果一个集合A元素全是另外一个集合B的元素，这就是A是B的子集，可以用issubset(),<=判断子集，<判断真子集
    反过来B就是A的超集，用issuperset()来判断
"""

set1 = {1,2,3,4,5}
set2 = {1,2,3,4,5,6,7}
set3 = {1,2,3,4,5,6,7,8,9}
print(set1 < set2)
print(set2 >= set3)

print(set1.issubset(set2))
print(set3.issuperset(set1))

"""
    set是一个可变类型，可以通过add,remove,clear方式添加删减元素,remove必须是元素存在集合中才能删除，不然会出现Key error
"""

set1 = {1,2,3,4,5,6,7}
set1.add(100)
if 2 in set1:
    set1.remove(2)
print(set1)
if 3 in set1:
    set1.discard(3)
print(set1)
#if 4 in set1:
  # a = set1.pop(4)
#print(set1)
set1.clear()
print(set1)

#还有一个isdisjoint()可以判断两个集合是否存在相同元素，没有返回True
set1 = {'Java', 'Python', 'C++', 'Kotlin'}
set2 = {'Kotlin', 'Swift', 'Java', 'Dart'}
set3 = {'HTML', 'CSS', 'JavaScript'}
print(set1.isdisjoint(set2))  # False
print(set1.isdisjoint(set3))  # True

print(hash(10))
print(hash("hello"))
print(hash((1, 2, 3)))

"""
    不可变集合frozenset
    除了不能添加和删除元素，frozenset在其他方面跟set是一样的。
"""
"""
    总结
    对于普通集合，集合是可变的，但是集合的元素是不可变的，因为集合是通过哈希值在判断元素是否存在集合中，数据如果改变，改变哈希值，就无法判断。
    列表字典集合不能放入集合，其他类型可以
"""