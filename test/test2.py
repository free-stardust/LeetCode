from typing import List


def func(ls: List[int], target: int):
    left = 0
    right = len(ls) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if ls[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if left == len(ls) or ls[left] != target:
        return -1

    return left


ls = [1, 1, 2, 3, 3, 4, 4]
res = func(ls, 1)
print(res)
res = func(ls, 3)
print(res)
res = func(ls, 4)
print(res)
res = func(ls, 5)
print(res)
