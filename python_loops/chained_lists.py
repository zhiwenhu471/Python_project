from itertools import chain

first = [7, 6, 1]
second = [4, 1]
third = [8, 0, 6]
forth = []
for value in chain(first, second, third):
    forth.append(str(value ** 2))

print(forth)
