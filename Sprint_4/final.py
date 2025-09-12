# 141513807
def deliver(weight: list[int], limit: int) -> int:
    sorted_weight: list[int] = sorted(weight)
    left_index: int = 0
    right_index: int = len(sorted_weight) - 1
    res_min: int = 0

    while left_index <= right_index:
        if sorted_weight[left_index] + sorted_weight[right_index] <= limit:
            left_index += 1
        right_index -= 1
        res_min += 1
    return res_min


if __name__ == '__main__':
    robot_weight = list(map(int, input().split()))
    robot_limit = int(input())
    result = deliver(robot_weight, robot_limit)
    print(result)
