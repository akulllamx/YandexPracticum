example_array = [6, 5, 3, 1, 8, 7, 2, 4]


def bubble_sort(data):
    for last_index in range(len(data) - 1, 0, -1):
        swapped = False
        for item_index in range(last_index):
            if data[item_index] > data[item_index + 1]:
                data[item_index], data[item_index + 1] = (
                    data[item_index + 1], data[item_index]
                )
                swapped = True
        if not swapped:
            break
    return data


print(bubble_sort(example_array))