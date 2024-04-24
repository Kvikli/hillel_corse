def move_last_to_first(lst):
    if len(lst) > 1:
        last_element = lst.pop()
        lst.insert(0, last_element)

my_list = [1, 2, 3, 4, 5]
move_last_to_first(my_list)
print(my_list)