import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open(html_file, 'r', encoding='utf-8') as file:
        html = file.read()

        # Використовуємо регулярний вираз для вилучення html-тегів
        cleaned_text = re.sub(r'<[^>]*>', '', html)

        # Записуємо очищений текст у вказаний файл
        with open(result_file, 'w', encoding='utf-8') as result:
            result.write(cleaned_text)


# Приклад використання
delete_html_tags('draft.html', 'cleaned.txt')
