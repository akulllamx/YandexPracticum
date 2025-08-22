# https://contest.yandex.ru/contest/52718/problems/B/
def function(string: str):
    max_substr = 0
    l = 0
    unique_set = set()

    for r in range(len(string)):
        while string[r] in unique_set:
            unique_set.remove(string[l])
            l += 1
        unique_set.add(string[r])
        max_substr = max(max_substr, r-l+1)
    return max_substr


test_1 = str(input())
print(function(test_1))  # abcabcabc