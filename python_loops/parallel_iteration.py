numbers = [1, 2, 3]
letters = ["a", "b", "c"]

for number, letter in zip(numbers, letters, strict=False):
    print(number, "->", letter)

# strict = False: 静默忽略较长对象中多出的元素，不报错

