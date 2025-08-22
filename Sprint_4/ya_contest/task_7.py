# https://contest.yandex.ru/contest/52718/problems/?nc=9BVXnpAD
def calculation(nums):
    nums_res = []

    for i in nums:
        count = 0
        for j in nums:
            if j < i:
                count += 1
        nums_res.append(str(count))
    return ' '.join(nums_res)


test_1 = list(map(int, input().split()))  # 6 5 4 8 // 2 1 0 3
print(calculation(test_1))

