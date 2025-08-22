def find_two_indexes(data, expected_result):
    # В начале работы
    # - левый указатель указывает на первый элемент списка (с индексом 0):
    left_pointer = 0
    # - правый указатель указывает на последний элемент списка.
    # Индекс этого элемента на единицу меньше длины списка.
    right_pointer = len(data) - 1
    # Пока индекс левого указателя меньше индекса правого указателя.
    while left_pointer < right_pointer:
        summa = data[left_pointer] + data[right_pointer]
        if summa == expected_result:
            return (left_pointer, right_pointer)
        if summa > expected_result:
            right_pointer -= 1
        if summa < expected_result:
            left_pointer += 1
    return None

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 11]
    expected_result = 10
    print(find_two_indexes(data, expected_result))