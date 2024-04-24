def divide_list(input_list):
    if len(input_list) == 0:
        return [[], []]
    elif len(input_list) % 2 == 0:

        midpoint = len(input_list) // 2
        return [input_list[:midpoint], input_list[midpoint:]]
    else:

        midpoint = len(input_list) // 2 + 1
        return [input_list[:midpoint], input_list[midpoint:]]

my_list = [1, 2, 3, 4, 5, 6, 7]
divided_lists = divide_list(my_list)
print(divided_lists)