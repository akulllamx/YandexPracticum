people = ['Антон', 'Соня', 'Коля', 'Женя', 'Тоня', 'Стёпа']

def say_to_all(func, sequence):
    for item in sequence:
        func(item)


say_to_all(lambda x: print(f'Привет, {x}!'), people)

say_to_all(lambda x: print(f'До завтра, {x}!'), people)