#修改分隔符sep
print("2026","10","25",sep = "-")
#修改结尾 end,print会自动换行
print("hello python ",end = "")
print("today is 2026-10-25" )
#接受多个数据采用split
a,b = input("请输入两个数字,用空格隔开：").split(" ")
print("a = ",a,"b = ",b)

#尽量采用格式化字符串输出，{}内会被当成普通文字，同时可以在里面进行计算
age = 18
print(f"小明的年龄是{age}")
pi = 3.1415926
print(f"pi = {pi:.2f}")     #保留小数位

#map()函数是将一个函数作用于一组数据的不同数据 map(函数，数据组)
texts = ["10", "20", "30"]

result = map(int, texts)        #将一组字符串做一个转型
print(list(result))

#input（）输入为进入一个字符串类型，需要其他类型需要转型。