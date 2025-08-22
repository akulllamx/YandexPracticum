class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

def solution(node, idx):
    lst_node = []

    while node is not None:
        lst_node.append(node)
        node = node.next_item

    lst_node.pop(idx)

    for i in range(len(lst_node) - 1):
        lst_node[i].next_item = lst_node[i + 1]

    if lst_node:
        lst_node[-1].next_item = None
        return lst_node[0]
    else:
        return None


# Тестирующая функция для проверки решения.
# Не изменяйте её, она не требует вашего внимания.

node3 = Node("Задача 4: Обследовать грунт в радиусе 3 м", None)
node2 = Node("Задача 3: Измерить температуру атмосферы", node3)
node1 = Node("Задача 2: Пробурить скважину глубиной 0.5 м", node2)
node0 = Node("Задача 1: Фотосъёмка 360°", node1)

new_head = solution(node0, 1)