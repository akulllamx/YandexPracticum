def main(items, target):
    items_len = len(items)
    for ind_1 in range(items_len):
        for ind_2 in range(items_len):
            if ind_1 == ind_2:
                continue
            if items[ind_1] + items[ind_2] == target:
                return True

data = [1, 2]
x = 3
print(main(data, x))