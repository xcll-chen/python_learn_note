#用斜杠来转义，\t表示制表\n表示换行
s1 = '\it \is \time \to \read \now'
s2 = r'\it \is \time \to \read \now'
print(s1)
print(s2)
print(r'\it')

#可以在\后跟随一个八进制或者是16进制表示字符\141以及\x61都是小写字母a
#跟随u就是Unicode编码
s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1)
print(s2)

#字符串可以进行运算，+可以做拼接，*可以重复字符串的内容
s1 = 'hello' + ', ' + 'world'
print(s1)    # hello, world
s2 = '!' * 3
print(s2)    # !!!
s1 += s2
print(s1)    # hello, world!!!
s1 *= 2
print(s1)    # hello, world!!!hello, world!!!

#in以及not in 判断是否字符串是否存在于另外一个字符串内
s1 = 'hello, world'
s2 = 'goodbye, world'
print('wo' in s1)      # True
print('wo' not in s2)  # False
print(s2 in s1)        # False

#len()函数可以获取字符串长度
s = 'hello, world'
print(len(s))                 # 12
print(len('goodbye, world'))  # 14

#[].[:]索引以及切片，跟列表以及元组相同，但是注意不要越界

#遍历整个字符串
s = 'hello'
for elem in s:
    print(elem)

#python中自带对字符串的操作通过对象引用调用对象方法的语法
s1 = 'hello,world！'

#首字母大写
print(s1.capitalize())
#单词首字母大写
print(s1.title())
#全大写
print(s1.upper())
#全小写
s2 = 'GOODBYE'
print(s2.lower())
#注意字符串是不可变类型，所以做的一切都是重新构建了一个新的字符串，而不是原来字符串的改变

#f用于格式化输出字符串

#strip()只拆卸两端的符号或者空格

s5 = '  ~hello,world!~  '
print(s5.strip(' '))
print(s5.lstrip(' '))

#replace（）可以替换掉字符串中间的内容，如果指定第几个就替换第几个，但是没有就不替换
s = 'hello, good world'
print(s.replace('o', '@'))     # hell@, g@@d w@rld
print(s.replace('o', '@', 1))  # hell@, good world

#拆分以及合并
#split（）就是拆分的意思，讲一长串字符串拆分成单词,拆分的结果放在列表中，默认对空格进行拆分，但是也可以指定其他字符进行拆分，以及控制拆分次数
#join（）

s = 'I love you'
words = s.split()
print(words)            # ['I', 'love', 'you']
print(' '.join(words))  # I~love~you
s = 'I#love#you#so#much'
words = s.split('#')
print(words)  # ['I', 'love', 'you', 'so', 'much']
words = s.split('#', 2)
print(words)  # ['I', 'love', 'you#so#much']

#字节串：二进制数据
#由0个或者多个字节组合成的有序序列，字符串的encode（）
a = '陈自强'
b = a.encode('utf-8')
c = a.encode('gbk')
print(b)                  
print(c)            
#dencode进行解码      
print(b.decode('utf-8'))  
print(c.decode('gbk'))    
