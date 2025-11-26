for number in range(1, 12):
    for product in range(number, number * 12, number):
        print(f"{product:>4d}", end="")
    print()
