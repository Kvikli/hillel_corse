number = int(input("Введіть 4-х значне число: "))

a1, b = divmod(number, 1000)
a2, b = divmod(b, 100)
a3, a4 = divmod(b, 10)
print(a1)
print(a2)
print(a3)
print(a4)