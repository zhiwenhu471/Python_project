import os # os 模块提供了与操作系统交互的功能
print(os.getcwd()) # 返回当前工作目录
# os.system("mkdir today")  # make a directory named today
print(dir(os)) # dir() 函数返回当前模块的属性和方法列表

import sys # sys 模块提供对 Python 解释器使用或维护的一些变量和函数的访问
if __name__ == "__main__":
    print(sys.argv)

import math # 数学函数模块
print(math.cos(math.pi / 4))
print(math.log(1024, 2))

import random # 进行随机数操作
print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10)) # 从指定范围内获取指定数量的随机数
print(random.random()) # 生成一个0到1之间的随机数
print(random.randrange(6)) # 生成一个0到6之间的随机整数

import statistics # 统计函数模块
