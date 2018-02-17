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


