def second_index(text, substring):
    first_index = text.find(substring)
    if first_index == -1:
        return None

    second_index = text.find(substring, first_index + 1)
    if second_index == -1:
        return None

    return second_index


text = "sims"
substring = "s"
print(second_index(text, substring))
