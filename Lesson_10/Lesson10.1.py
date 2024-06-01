from inspect import isgenerator


def some_gen(begin, n, func):
    """
    begin: перший елемент послідовності
    n: кількість елементів у послідовності
    func: функція, яка формує значення для послідовності
    """
    current = begin
    for _ in range(n):
        yield current
        current = func(current)


# Функція для тестування
def pow(x):
    return x ** 2


# Перевірка, чи функція є генератором
gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
