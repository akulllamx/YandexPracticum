def fibonacci(n):
    sequence = [0, 1]  # Начальные значения
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])  # Формула из задания
    return sequence[:n]

sequence = fibonacci(10)
for number in sequence:
    print(number)