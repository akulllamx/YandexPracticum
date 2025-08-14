wins = [1223125, 2128437, 2128500, 2741001, 4567687, 4567890, 7495938, 9314543]


def find_element(sorted_numbers, element):
    """Находит индекс element в отсортированном списке sorted_numbers."""
    left = 0
    right = len(sorted_numbers)

    while left < right:
        mid = (left + right) // 2
        result = sorted_numbers[mid]
        if result == element:
            return mid
        elif result > element:
            right = mid
        elif result < element:
            left = mid + 1
    return None


# Проверим, что ваш код успешно находит все значения,
# которые есть в списке wins: в качестве искомого элемента
# поочерёдно передадим в функцию все значения из списка.
for item in wins:
    print(find_element(wins, item))