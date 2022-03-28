def binary_search(numbers_list, number_to_find):
    """not recursive"""
    left_index = 0
    right_index = len(numbers_list)

    while left_index <= right_index:
        mid_index = (right_index + left_index) // 2
        mid_number = numbers_list[mid_index]
        if mid_number == number_to_find:
            return mid_index
        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1


# print(binary_search([1, 2, 3, 4, 5], 4))


def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1
    mid_index = (right_index + left_index) // 2
    mid_number = numbers_list[mid_index]
    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1
    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)


def binary_search_recursive_my(sorted_list, number_to_find):
    """doesnt show the index, only True"""
    sorted_list.sort()
    if len(sorted_list) == 1:
        if sorted_list[0] == number_to_find:
            return True
        return False
    if number_to_find == sorted_list[len(sorted_list) // 2]:
        return True

    if number_to_find > sorted_list[len(sorted_list) // 2]:
        sorted_list = sorted_list[(len(sorted_list) // 2):]

    else:
        sorted_list = sorted_list[0:(len(sorted_list) // 2)]

    return binary_search_recursive_my(sorted_list, number_to_find)


print(binary_search_recursive_my([1, 2, 3, 50, 4, 5, 9, 0], 50))
