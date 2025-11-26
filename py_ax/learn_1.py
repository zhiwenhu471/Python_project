# 读写文件
with open("main.py") as f:
    print(f.read())

# 一个简单的类
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)

x.counter = 1
if x.counter < 10:
    x.counter = x.counter * 2
    print(x.counter)
else:
    print("x.counter >= 10")