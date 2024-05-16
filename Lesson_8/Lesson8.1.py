def add_one(some_list):
    # Перетворюємо список цифр у число, додаємо 1, а потім знову перетворюємо число в список цифр
    num = int(''.join(map(str, some_list))) + 1
    result = [int(digit) for digit in str(num)]
    return result


# Перевірка
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
