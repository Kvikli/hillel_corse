def correct_sentence(text):
    if not text[0].isupper():
        text = text[0].upper() + text[1:]

    if text[-1] != '.':
        text += '.'

    return text


sentence1 = "це речення починається з малої літери."
sentence2 = "А це речення уже починається з великої."
sentence3 = "А це речення без крапки в кінці"
sentence4 = "а ось це речення без крапки в кінці і з маленької"
print(correct_sentence(sentence1))
print(correct_sentence(sentence2))
print(correct_sentence(sentence3))
print(correct_sentence(sentence4))
