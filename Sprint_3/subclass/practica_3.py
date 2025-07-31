class Customer:
    def __init__(self, name: str):
        self.name = name
        self.__discount = int(10)


    def set_discount(self, new_value: int):
        self.__discount = new_value
        if new_value > 80:
            self.__discount = 80
            return new_value
        else:
            self.__discount = new_value
            return new_value


    def get_price(self, price: int) -> float:
        new_price = round(price - ((price/100)*self.__discount), 2)
        return new_price


# Проверим работу программы.
# Создаём объект покупателя:
customer = Customer('Иван Иванович')

original_price = 100

print(
    f'С исходной скидкой Иван Иванович заплатит '
    f'{customer.get_price(original_price)} рублей вместо {original_price}'
)
# Изменим скидку до неприемлемого уровня.
# Метод set_discount() должен установить размер скидки равным 80.
customer.set_discount(90)
print(
    f'С новой скидкой Иван Иванович заплатит '
    f'{customer.get_price(original_price)} рублей вместо {original_price}'
)