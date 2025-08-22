def valid_mountain_array(lst: list) -> bool:
    if len(lst) < 3:
        return False

    arr_peak = lst.index(max(lst))  # индекс вершины
    if arr_peak == 0 or arr_peak == len(lst) - 1:
        return False

    for i in range(arr_peak):
        if lst[i] >= lst[i+1]:
            return False


    for i in range(arr_peak, len(lst)-1):
        if lst[i] <= lst[i+1]:
            return False

    return True


def main():
    arr = list(map(int, input().split()))
    print(valid_mountain_array(arr))

if __name__ == '__main__':
    main()
