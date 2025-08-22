def list_superset(list_set_1, list_set_2):
    # Не меняйте названия функции и параметров. Напишите решение здесь.
    def equal(lst_1, lst_2):
        if len(lst_1) != len(lst_2):
            return False
        for item in lst_1:
            if item not in lst_2:
                return False
        return True

    def superset(lst_1, lst_2):
        for item in lst_2:
            if item not in lst_1:
                return False
        return True

    if equal(list_set_1, list_set_2):
        return f'Наборы равны.'
    elif superset(list_set_1, list_set_2):
        return f'Набор {list_set_1} - супермножество.'
    elif superset(list_set_2, list_set_1):
        return f'Набор {list_set_2} - супермножество.'
    else:
        return f'Супермножество не обнаружено.'

# Примеры для проверки функции.
list_set_1 = [1, 3, 5, 7]
list_set_2 = [3, 5]
list_set_3 = [5, 3, 7, 1]
list_set_4 = [5, 6]

print(list_superset(list_set_1, list_set_2))
print(list_superset(list_set_2, list_set_3))
print(list_superset(list_set_1, list_set_3))
print(list_superset(list_set_2, list_set_4))