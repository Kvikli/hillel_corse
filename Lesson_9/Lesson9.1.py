def popular_words(text, words):
    # Приведемо текст до нижнього регістру
    text = text.lower()

    # Розіб'ємо текст на слова
    word_list = text.split()

    # Створимо словник для зберігання результатів
    word_count = {word: 0 for word in words}

    # Підрахуємо кількість появ кожного слова з списку шуканих слів
    for word in word_list:
        if word in word_count:
            word_count[word] += 1

    return word_count


# Тестування функції
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
