def common_elements():
    multiples_of_3 = [x for x in range(100) if x % 3 == 0]
    multiples_of_5 = [x for x in range(100) if x % 5 == 0]

    set_3 = set(multiples_of_3)
    set_5 = set(multiples_of_5)

    common_set = set_3.intersection(set_5)

    print("Перетин множин, що містять числа, кратні як 3, так і 5:")
    print(common_set)

    return common_set


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
