#求解100内的素数

for i in range(2,101):
    is_prime = True
    for j in range(2,i):
        if i%j == 0:
            is_prime = False
            break
    if is_prime:
        print(i,"是素数")

#斐波那契数列
a,b = 0,1
for _ in range(10):
    a, b = b, a + b     #采用同时赋值
    print(a)

#寻找水仙花数

for num in range(100,1000):
    a = num % 10
    b = num // 10 %10
    c = num // 100
    if a**3 + b**3 + c**3 == num:
        print(num,"是水仙花数")

for i in range(0,21):
    for j in range(0,34):
        for k in range(0,100,3):
            if 5*i + 3*j + k // 3 == 100 and i+j+k == 100:
                print(f"100元能买{i}只公鸡，{j}只母鸡，{k}只小鸡")