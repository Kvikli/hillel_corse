def sum_even_index_elements(arr):
    if not arr:
        return 0

    sum_even = sum(arr[i] for i in range(0, len(arr), 2))

    result = sum_even * arr[-1]

    return result


arr = [1, 2, 3, 4, 5]
print(sum_even_index_elements(arr))
