def create_hashtag(sentence):
    words = sentence.split()
    words = [word.capitalize() for word in words]

    hashtag = '#' + ''.join(words)

    hashtag = hashtag[:140]

    return hashtag


input_sentence = input("Введіть рядок: ")
result_hashtag = create_hashtag(input_sentence)
print("hashtag:", result_hashtag)