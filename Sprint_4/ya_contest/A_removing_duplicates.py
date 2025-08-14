def main():
    n = int(input())  # длина множества
    arr = list(map(int, input().split()))

    unique_list = set()
    result = []

    for x in arr:
        if x not in unique_list:
            unique_list.add(x)
            result.append(x)
        else:
            result.append('_')

    unique_element = [x for x in result if x != '_']
    underscores = ['_'] * (n - len(unique_element))


    print(*unique_element, *underscores)

if __name__ == '__main__':
    main()
