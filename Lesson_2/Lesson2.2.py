number = int(input("Введіть 5-х значне число: "))
reversed_number = number % 10 * 10000
number = number // 10
reversed_number += number % 10 * 1000
number = number // 10
reversed_number += number % 10 * 100
number = number // 10
reversed_number += number % 10 * 10
number = number // 10
reversed_number += number % 10
print(reversed_number)