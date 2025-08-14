wins = ['алгоритмы', 'будут', 'главным', 'доводом', 'профессионального', 'разработчика']


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

print(find_element(wins, 'доводом'))

