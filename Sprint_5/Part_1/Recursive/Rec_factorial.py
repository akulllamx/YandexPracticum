def factorial(n):
    # Базовый случай
    if n <= 1:
        return 1

    # Рекурсивный случай
    fac = n * factorial(n - 1)
    return fac


print(f"5! = {factorial(5)}")  # 120
