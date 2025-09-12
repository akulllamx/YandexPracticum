def main() -> int:
    n = int(input().strip())
    orders = list(map(int, input().split()))
    m = int(input().strip())
    samples = list(map(int, input().split()))

    orders.sort()
    samples.sort()

    count = 0
    i = 0
    j = 0

    while i < n and j < m:
        if samples[j] >= orders[i]:
            count += 1
            i += 1
            j += 1
        else:
            j += 1

    print(count)


if __name__ == '__main__':
    main()