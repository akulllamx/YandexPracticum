from collections import Counter

# Считываем данные
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
template = list(map(int, input().split()))

# Подсчёт количества каждого числа в arr
counter = Counter(arr)
result = []

# Сортировка по шаблону
for num in template:
    if num in counter:
        result += [num] * counter[num]
        del counter[num]

# Оставшиеся числа не из шаблона: сортируем и добавляем в конец
remaining = sorted(counter.elements())
result += remaining

# Вывод результата
print(*result)