import string
import keyword


def is_valid_variable_name(name):
    if not name or name[0].isdigit():
        return False
    if any(char in string.punctuation.replace("_", "") for char in name):
        return False
    if any(char.isupper() for char in name):
        return False
    if name in keyword.kwlist:
        return False
    return True


user_input = input("Введіть ім'я змінної: ")
print(is_valid_variable_name(user_input))