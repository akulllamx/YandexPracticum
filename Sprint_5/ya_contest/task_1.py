def measure(version: int) -> int:

    if version == 0 or version == 1:
        return 1

    return measure(version - 1) + measure(version - 2)


print(measure(int(input())))
