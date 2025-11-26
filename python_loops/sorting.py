students = {
    "Alice": 89.5,
    "Bob": 76.0,
    "Charlie": 92.3,
    "Diana": 84.7,
    "Ethan": 88.9,
    "Fiona": 95.6,
    "George": 73.4,
    "Hannah": 81.2,
}

sorted_students = sorted(
    students.items(), key = lambda item: item[1], reverse=True
)  
# sorted() set ascending, reverse = True, then it bocomes descending order
# students.items() are the object
# key is the item sorted() acts by
# key = lambda item: item[1] means retract the second item in turple such as ('Alice', 89.5)
#  
for name, grade in sorted_students:
    print(f"{name}'s average grade: {grade:->{20 - len(name)}.1f}")

    """
    格式化字符串：{grade:->{20 - len(name)}.1f}的含义是：
    1): 20 - len(name) 计算填充长度, 使冒号后的内容总宽度大致为20字符。
    2): ->：表示在成绩数字左侧使用减号-进行填充。
    3): .1f 将成绩格式化为保留一位小数的浮点数。
    """

