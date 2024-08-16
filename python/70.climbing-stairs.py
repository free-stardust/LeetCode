#
# @lc app=leetcode.cn id=70 lang=python3
# @lcpr version=30204
#
# [70] 爬楼梯
#
# https://leetcode.cn/problems/climbing-stairs/description/
#
# algorithms
# Easy (54.73%)
# Likes:    3581
# Dislikes: 0
# Total Accepted:    1.6M
# Total Submissions: 2.8M
# Testcase Example:  '2'
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
#
#
# 示例 1：
#
# 输入：n = 2
# 输出：2
# 解释：有两种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶
# 2. 2 阶
#
# 示例 2：
#
# 输入：n = 3
# 输出：3
# 解释：有三种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶 + 1 阶
# 2. 1 阶 + 2 阶
# 3. 2 阶 + 1 阶
#
#
#
#
# 提示：
#
#
# 1 <= n <= 45
#
#
#

# @lcpr-template-start
import copy
import collections
import random
import math
from collections import namedtuple
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush


# @lcpr-template-end
# @lc code=start
class Solution:

    def dp(self, n: int) -> int:
        step1, step2, step3 = 0, 0, 1

        for _ in range(n):
            step1 = step2
            step2 = step3
            step3 = step1 + step2

        return step3

    def bin_exponentiation(self, n: int) -> int:

        def matrix_multiply(a, b):
            ans = [[0, 0], [0, 0]]

            for i in range(2):
                for j in range(2):
                    ans[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]

            return ans

        def matrix_pow(matrix, n):
            res = [[1, 0], [0, 1]]

            while n > 0:
                if n & 1 == 1:
                    res = matrix_multiply(res, matrix)

                n >>= 1
                matrix = matrix_multiply(matrix, matrix)

            return res

        matrix = [[1, 1], [1, 0]]
        ans = matrix_pow(matrix, n)

        return ans[0][0]

    def general_formula(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        ans = math.pow((1 + sqrt5) / 2, n + 1) - math.pow(
            (1 - sqrt5) / 2, n + 1)
        return int(round(ans / sqrt5))

    def climbStairs(self, n: int) -> int:
        # return self.dp(n)
        # return self.bin_exponentiation(n)
        return self.general_formula(n)


# @lc code=end

tests = [2, 3]
ans = [2, 3]
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().climbStairs(t)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#
