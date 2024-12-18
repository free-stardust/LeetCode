#
# @lc app=leetcode.cn id=279 lang=python3
# @lcpr version=30204
#
# [279] 完全平方数
#
# https://leetcode.cn/problems/perfect-squares/description/
#
# algorithms
# Medium (67.12%)
# Likes:    2026
# Dislikes: 0
# Total Accepted:    577K
# Total Submissions: 857.2K
# Testcase Example:  '12'
#
# 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
#
# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11
# 不是。
#
#
#
# 示例 1：
#
# 输入：n = 12
# 输出：3
# 解释：12 = 4 + 4 + 4
#
# 示例 2：
#
# 输入：n = 13
# 输出：2
# 解释：13 = 4 + 9
#
#
# 提示：
#
#
# 1 <= n <= 10^4
#
#
#

# @lcpr-template-start
import copy
import collections
import random
import math
from functools import reduce
from collections import namedtuple
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush


# @lcpr-template-end
# @lc code=start
class Solution:

    def use_dp(self, n: int) -> int:
        f = [0] * (n + 1)

        for i in range(1, n + 1):
            min_f = math.inf
            j = 1
            while j * j <= i:
                min_f = min(min_f, f[i - j * j])
                j += 1
            f[i] = min_f + 1

        return f[n]

    def numSquares(self, n: int) -> int:
        return self.use_dp(n)


# @lc code=end

#
# @lcpr case=start
# 12\n
# @lcpr case=end

# @lcpr case=start
# 13\n
# @lcpr case=end

#
