class MushroomsCollector:

    def __init__(self):
        self.mushrooms = []

    # Исправьте ошибку в этом методе.
    def is_poisonous(self, mushroom_name):
        if mushroom_name in ['Мухомор', 'Поганка']:
            print(f'Нельзя добавить ядовитый гриб')
            return True
        else:
            return False

    # Допишите метод.
    def add_mushroom(self, name):
        self.name = name
        if self.is_poisonous(name) == True:
            return
        else:
            self.mushrooms.append(name)


    # Напишите магический метод __str__,
    # возвращающий перечень грибов из списка mushrooms
    # через запятую.
    def __str__(self):
        return ', '.join(self.mushrooms)


# Пример запуска для самопроверки
collector_1 = MushroomsCollector()
collector_1.add_mushroom('Мухомор')
collector_1.add_mushroom('Подосиновик')
collector_1.add_mushroom('Белый')
print(collector_1)

collector_2 = MushroomsCollector()
collector_2.add_mushroom('Поганка')
collector_2.add_mushroom('Лисичка')
print(collector_2)