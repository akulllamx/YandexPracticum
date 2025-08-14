def binary_search(list, item):
    low = 0
    hight = len(list) - 1

    while low <= hight:
        mid = (low + hight) // 2
        if list[mid] == item:
            return mid
        elif list[mid] > item:
            hight = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]

print (binary_search(my_list, 7))