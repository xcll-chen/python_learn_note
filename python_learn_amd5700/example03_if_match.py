"""分支结构
    关键字要是if,else,elif,match,case
    通过条件判断实现不同的分支执行
"""
#if else elif做bmi判断
height,weight = map(float,input("please input your height and weight(space-separated):").split(" "))
bmi = weight/(height / 100) ** 2
print(f"your bmi is:{bmi:.1f}",end  = ",")

if   18.4<= bmi < 24:
    print("你的身材很棒！")
elif bmi <18.4  :
    print("你需要吃点好的")
else:
    print("你需要减肥")


#match case 等同于C语言switch case
status_code = int(input('响应状态码: '))
match status_code:
    case 400 | 405: description = 'Invalid Request'     #可以个将400，405归位一个分支
    case 401: description = 'Unauthorized'
    case 403: description = 'Forbidden'
    case 404: description = 'Not Found'
    #case 405: description = 'Method Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown Status Code'         #“_”通配符  = default
print('状态码描述:', description)

