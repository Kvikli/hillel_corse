num1 = float(input("Введіть перше число: "))
op = input("Операція (+, -, *, /): ")
num2 = float(input("Введіть друге число: "))


if op == '+':
    print("Результат:", num1 + num2)
elif op == '-':
    print("Результат:", num1 - num2)
elif op == '*':
    print("Результат:", num1 * num2)
elif op == '/':
    if num2 != 0:
        print("Результат:", num1 / num2)
    else:
        print("Помилка: ділення на нуль!")
else:
    print("Невідома операція!")