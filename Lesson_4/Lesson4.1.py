def move_zeroes(forward):
    zero = 0

    for num in forward:
        if num != 0:
            forward[zero] = num
            zero += 1

    while zero < len(forward):
        forward[zero] = 0
        zero += 1


forward = [0, 1, 0, 3, 12]
move_zeroes(forward)
print(forward)
