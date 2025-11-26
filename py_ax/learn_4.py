# coding = utf-8

# 只是引用
a = [1, 2, 3, 4]
b = a
print(a)
print(b)

# 对 b 进行操作，看 a 是否有改变
b.append(5)
print(b)
print(a) # 修改 b 的同时，a 也被修改

# 复制一个副本
b = a[:]
print(b)

# 对 b 进行操作，看 a 是否有改变
b.append(6)
print(b)
print(a) # 修改 b 的同时，a 不被修改