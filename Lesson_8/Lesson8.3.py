def find_unique_value(some_list):
    # Створюємо пустий словник для зберігання кількості зустрічень кожного числа
    count_dict = {}

    # Заповнюємо словник, підраховуючи кількість зустрічень кожного числа у списку
    for num in some_list:
        count_dict[num] = count_dict.get(num, 0) + 1

    # Перевіряємо, яке число зустрілося лише один раз і повертаємо його
    for num, count in count_dict.items():
        if count == 1:
            return num


# Перевірка
assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
