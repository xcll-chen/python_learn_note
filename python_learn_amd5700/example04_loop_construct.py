"""循环结构
    关键字:for-in,while,break,continue
    主要通过条件判断实现循环运行
"""
import time
"""range()用于生成0~59的整数,取值不到60,
    range(1,100),从1到99
    range(1,101,2)取1~100的奇数
    range(0,101,2)取1~100的偶数
    range(100,0,-1)倒着数,最后那个数都是取不到的
"""
"""
for i in range(60,1,-1):         
    print(f"这是第{i}秒")
    time.sleep(1)
"""
#对于需要循环变量的循环结构可以将循环变量i换成”_“,需要停止对终端使用ctrl+c结束
for _ in range(3):         
    print("hello")
    time.sleep(1)

#整数求和
total = 0
for i in range(1,100):
    total  += i
print(f"1~99整数求和为{total}")

#除此以外还可以实现奇数，偶数求和，列表求和等等，使用sum（）函数可以直接求和省去循环结构
print(f"1~99整数求和为{sum(range(1,100))}")

#不确定循环次数可以采用while循环，通过判断条件实现循环
total = 0
i = 1
while i < 100:
    total += i
    i += 1
print(f"1~99整数求和为{total}")

#back，continue的使用，
#当给while的条件是True时，循环会一直执行，但是想跳出循环就需要，使用一个条件判断back,或者想跳过某些循环时，添加判断使用continue跳过这轮次的循环
total = 0
i = 1
while True:
    if i >100:
        break
    total += i
    i += 1
print(f"1~100整数求和为{total}")

#跳过奇数，求偶数和
total = 0
i = 1
while True:
    if i >100:
        break
    if i % 2:
        i += 1
        continue
    else:
        print(i)
        total += i
        i += 1
print(f"1~100偶数求和为{total}")

#循环嵌套
i,j = 0,0
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{i}×{j}={i * j}', end='\t')
    print()