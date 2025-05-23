from typing import List


def func(n):
    res = []
    path = []

    def dfs(left, right):
        if len(path) == 2 * n:
            res.append("".join(path))
            return

        if left == right:
            path.append("(")
            dfs(left + 1, right)
        elif left < n:
            path.append("(")
            dfs(left + 1, right)
            path.pop()
            path.append(")")
            dfs(left, right + 1)
        else:
            path.append(")")
            dfs(left, right + 1)

        path.pop()

    dfs(0, 0)

    return res


def func2(target: int, nums: List[int]):
    res = 0

    def dfs(tmp_t, start):
        nonlocal res

        if tmp_t == 0:
            res += 1
            return

        for i in range(start, len(nums)):
            if tmp_t - nums[i] < 0:
                break
            dfs(tmp_t - nums[i], i)

    dfs(target, 0)

    return res


def func3(target: int, nums: List[int]):
    dp = [1] + [0] * target

    for num in nums:
        for i in range(num, target + 1):
            dp[i] += dp[i - num]

    return dp[target]


N = [1, 2, 3]
for n in N:
    res = func(n)
    print(n, res)

print("********************************")

tests = [[5, [1, 2, 4, 5]], [5, []], [5, [5]], [3, [1, 2, 3]]]
for target, nums in tests:
    res = func3(target, nums)
    print(res)
