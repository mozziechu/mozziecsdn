#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 输出
print('I am pig')
# 输入
# name = input()
# print(name)

# 注释 转译
# 不论是否用r''表示''内部的字符串默认不转义，注意''内部\为基数时，后面必须跟字符
# 不然报错： EOL while scanning string literal
print(r'\\\\')
print('\、\\\\')
# 用\n写在一行里不好阅读，允许用'''...'''的格式表示多行内容
print('''line1  \n ... line2... line3''')
print(r'''hello,\nworld''')

# Python数据类型：
# # 字符串:'String'
# # 整数，没有大小限制:1,2,-3,0,0xff00，0xa5b4c3d2
# # 浮点，没有大小限制:1.1,0.0001,-0.2,1.23e9
# # 布尔值:True,False    注意大小写
True and False  # and运算是与运算，只有所有都为True，and运算结果才是True
5 > 3 and 3 > 1  # and运算是与运算，只有所有都为True，and运算结果才是True
True or True  # or运算是或运算，只要其中有一个为True，or运算结果就是True
5 > 3 or 1 > 3  # or运算是或运算，只要其中有一个为True，or运算结果就是True
not True  # not运算是非运算，它是一个单目运算符，把True变成False，False变成True
not 1 > 2  # not运算是非运算，它是一个单目运算符，把True变成False，False变成True
# # 空值：None    注意大小写
# # 还提供了列表、字典等多种数据类型，还允许创建自定义数据类型

# 变量
# 可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量,定义变量且赋值时：
# # 1-在内存中创建了一个'ABC'的字符串；
# # 2-在内存中创建了一个名为a的变量，并把它指向'ABC'。
# 这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。
# 静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。例如Java是静态语言
a = 1
print(a)
a = True
print(a)
# 常量：值不能变的变量。在Python中，通常用全部大写的变量名表示常量
PI = 3.14159265359

# 运算符
# # 除法 有三种
# # # 浮点数:/
print('浮点数除法:', 10/3)
print('浮点数除法:', 9/3)
# # # 地板除：//
print('地板除法:', 10//3)
print('地板除法:', 9//3)
# # # 取余：%
print('取余:', 10 % 3)
print('取余:', 9 % 3)

# 字符编码 Python 3.0+ 字符串以Unicode编码
print('\u4e2d\u6587') # 打印十六进制的等同于“中文”
print('中文')
# str 转 bytes 的理论实践知识，由于学习方向的原因，略

# 格式化字符串
# # 格式化字符串：%s
# # 格式化整数：%d
# # 格式化浮点数：%f
# # 格式化十六进制：%x
print('妈妈叫%s下午%d点用%fs/m的速度回家睡觉。' % ('XM',16.0,2.6))
# # # 整数和浮点数还可以指定是否补0和整数与小数的位数
print('妈妈叫%s下午%03d点用%.3fs/m的速度回家睡觉。' % ('XM',16,2.6))
print('妈妈叫%s下午%04d点用%.3fs/m的速度回家睡觉。' % ('XM',16,2.6))
# # # 不清楚类型可以用 %s代替所有类型
# # 字符串的format()方法
print('妈妈叫{0}下午{1:03d}点用{2:.2f}s/m的速度回家睡觉。'.format('XM',16,2.6))

# list 和 tuple
list = [1,2,3,4,5,6,7,8,9]
print(list,
'\nlist的长度：',len(list),
'\n索引list中的指定元素[0]', list[0],
'\n最后一个索引是[len(list)-1]，用[-1]表示', list[-1],
'\n以此类推倒数第2个就是[-2]', list[-2])
# # list是一个可变的有序表
print('追加一个元素0',list,'\n追加的方法 > list.append(0):',list.append(0))
# # 把元素插入到指定的位置
print('把元素插入到指定的位置',list,'\n插入的方法 > list.insert(11,11):',list.insert(11, 11))
# # 要删除list末尾的元素
print('要删除list末尾的元素',list,'\n插入的方法 > list.pop():',list.pop())
# # 要删除list指定的位置的元素
print('要删除list指定的位置的元素',list,'\n插入的方法 > list.pop(9):',list.pop(9))
# # 某个元素替换成别的元素，可以直接赋值给对应的索引位置
list[0]=10
print('把索引第0个换成10吧', list, '\n替换的方法 > list[0] = 10')

tuple_1 = (0,)
tuple_2 = (0,1,2,3,4,[5,6,7],[8,9,10])
print(tuple_1,tuple_2)

# 条件判断
ifs = 20
if ifs<=15:
    print('<= 15')
else:
    print('> 15')

if ifs < 15:
    print('< 15')
elif ifs >= 15:
    print('>= 15')
else:
    print('= 15')

#  数据类型转换
s = input('birth: ')
# # str 转 int()型数据
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
# # Python提供一个range()函数，可以生成一个整数序列
print(range(5))
# # list()函数，把序列转list类型


# 循环
# # for
arrays = ['ma', 'ms', 'mi']
for arr in arrays:
    print(arr)
# # while
whiles = 0
w = 9
while w > 0:
    whiles = whiles + w
    w = w - 2
print(whiles)
# # break语句可以提前退出循环
b = 1
while b <= 100:
    if b > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(b)
    b = b + 1
print('break END')
# # continue语句，跳过当前的这次循环，直接开始下一次循环
c = 0
while c < 10:
    c = c + 1
    if c % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(c)
# # break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环
# # 并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。

# dict
# # Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map
# # 使用键-值（key-value）存储，具有极快的查找速度
dicts = {'a': 9, 'b': 8}
print(dicts['a'])
# # 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print('a' in dicts)
# # 通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
dicts.get('c', 99)
print(dicts,'dicts.get("c", 99)')
# # 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
print(dicts.pop('a'))
# # # dict的key必须是不可变对象,这个通过key计算位置的算法称为哈希算法（Hash）要保证hash的正确性，作为key的对象就不能变。
# # # ist比较，dict有以下几个特点：
# # # # 查找和插入的速度极快，不会随着key的增加而变慢；
# # # # 需要占用大量的内存，内存浪费多。

# set
# # 和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
sets = set([1,2,3])
print(sets)
# # 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
sets.add(4)
print(sets)
# # 通过remove(key)方法可以删除元素
sets.remove(4)
print(sets)
# # 做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)
# # 当把tuple这个不变对象，放入dict & set中测试其结果

# 函数 python本身内置了很多函数
# python的函数官网 >>>
# http://docs.python.org/3/library/functions.html
# # 以数据类型转换位列
print(int('123'))
print(int(12.34))
print(float('12'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(''))

# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回
def my_abs(x):
    if not isinstance(x, (int, float)): # 对参数类型做检查，只允许整数和浮点数类型的参数
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-12))
# 空函数
# pass语句什么都不做
# 实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
def nop():
    pass

