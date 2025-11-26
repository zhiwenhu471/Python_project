# 定义一个函数
def add_function(x, y):
    z = x + y
    print(z)
if __name__ == '__main__':
        add_function(3,4)

# name()只是用来输出名字
def name():
    print("zhiwen hu")
name()

def add(x, y):
    print (x + y) # 此处使用return(并不会输出)
add(7, 8)


a = 1
b = 2
a, b = b, a + b
print("a = " + str(a), "b = " + str(b))

# 定义一个斐波拉契数列
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
fibonacci(10)

def fibonacci_iterative(n):
    '''
    这是斐波拉契数列的迭代实现
    '''
    if n < 0:
        raise ValueError("输入必须为非负整数")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    print(a, b)
fibonacci_iterative(10)


# 动态生成斐波拉契序列
def fibonacci_dynamic( ):
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
# 生成前十项
fib = fibonacci_dynamic()
print([next(fib) for _ in range(20)]) # 打印前n项

# 建立一个计算圆面积的函数
import math # 导入 math 模块
def circle_area(r):
    print(math.pi * r ** 2)
    
# r = 4
circle_area(4)

# 在这个函数中添加输入验证
def circle_area(r):
    if r < 0:
        raise ValueError("半径不能为负数")
    print(math.pi * r ** 2)

# r = -1
# circle_area(-1)

# r = 6
circle_area(6)

# python 之禅
import this

# 访问本地命名空间
# print(locals())
# 全局
# print(globals())

# help(math)

# sys 模块与 python 解释器密切相关
import sys
# print(sys.__doc__)

# os 模块
import os
os.getcwd() # 输出当前目录所在
os.listdir() # 列出当前目录下的文件
# help(os)

# time 模块
import time
print(time.ctime()) # 查看当下时间

import calendar
cal = calendar.month(2025, 11) # 像日历一般整齐排列
print(cal)

calendar.isleap(2025) # 判断是否为闰年

table = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 8637678}
for name, phone in table.items():
    print(f"{name:10} ==> {phone:10d}")

print("hello world")  # 省电模式会禁用后台的代码补全和语法高亮等行为