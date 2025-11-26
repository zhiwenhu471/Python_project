numbers = [2, 4, 6, 8]
for number in numbers:
    if number % 2 == 0:
        numbers.remove(number)
print(numbers)

numbers_1 = [2, 4, 6, 8]
for number in numbers_1[:]:  # 遍历副本，防止跳过某些元素
    if number % 2 == 0:
        numbers_1.remove(number)
print(numbers_1)

numbers_2 = [2, 1, 4, 6, 5, 8]
processed_numbers = []
for number in numbers_2:
   if number % 2 != 0:
        processed_numbers.append(number**2)
print(processed_numbers)