import string


def characters_between_letters(input_str):
    alphabet = string.ascii_letters

    start_letter, end_letter = input_str.split('-')

    start_index = alphabet.index(start_letter)
    end_index = alphabet.index(end_letter)

    return alphabet[start_index:end_index + 1]


input_letters = input("Введіть дві літери через дефіс: ")
print("Символи між введеними літерами:", characters_between_letters(input_letters))
