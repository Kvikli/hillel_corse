def multiply_digits_until_nine(number):
    result = 1

    while number >= 9:
        digit = number % 10

        result *= digit

        number //= 10

    return result


user_number = int(input("Введіть ціле число: "))
print("Результат множення цифр до отримання числа менше або дорівнює 9:", multiply_digits_until_nine(user_number))
