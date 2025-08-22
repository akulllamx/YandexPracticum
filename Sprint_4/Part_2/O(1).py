days_temp = [-1, -4, 8, -7, 3, 0, 1, -7, -7, 0, 0, -4, 1, 8, 1, -5, 4, 0, 7, 1]

# Передаём в функцию полный массив значений и границы исследуемого участка:
def calculate_positive(sequence, left, right):
    count = 0
    for item in sequence[left:right]:
        if item > 0:
            count += 1
    return count

print(calculate_positive(days_temp, 9, 14))