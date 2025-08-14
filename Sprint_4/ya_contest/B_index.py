def main():
    list_massive = list(map(int, input().split()))
    item = int(input())
    left = 0
    right = len(list_massive) - 1

    while left <= right:
        mid = (left + right) // 2
        if list_massive[mid] == item:
            while mid > 0 and list_massive[mid - 1] == item:
                mid -= 1
            return print(mid)
        elif list_massive[mid] < item:
            left = mid + 1
        elif list_massive[mid] > item:
            right = mid - 1
    return print(left)

if __name__ == '__main__':
    main()
