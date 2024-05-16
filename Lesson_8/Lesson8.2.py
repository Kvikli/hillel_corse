import re


def is_palindrome(text):
    # Перетворення рядка на нижній регістр і видалення знаків пунктуації та пробілів
    text = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    # Перевірка, чи рядок дорівнює своєму оберненому
    return text == text[::-1]


# Перевірка
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
