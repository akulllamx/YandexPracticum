def merge_sort(array):
    len_array = len(array)

    if len_array <= 1:
        return array

    left = merge_sort(array[0 : len_array // 2])
    right = merge_sort(array[len_array // 2 : len_array])

    return merge(left, right)


def merge(left, right):  # слияние 2 sort массивов
    result = []
    left_idx, right_idx = 0, 0
    len_left, len_right = len(left), len(right)

    while left_idx < len_left and right_idx < len_right:
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    return result + left[left_idx:] + right[right_idx:]




array = [3, 4, 5, 8, 1, 7, 2, 6, 9, 10]
print(merge_sort(array))