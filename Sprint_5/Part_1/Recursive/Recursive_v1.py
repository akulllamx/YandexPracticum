def countdown(n):
    # Базовый случай
    if n <= 0:
        print("Пуск!")
        return

    # Рекурсивный случай
    print(f"Осталось: {n}")
    countdown(n - 1)


countdown(5)
