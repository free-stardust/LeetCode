#
# @lc app=leetcode.cn id=172 lang=python3
# @lcpr version=30204
#
# [172] 阶乘后的零
#
# https://leetcode.cn/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Medium (50.53%)
# Likes:    850
# Dislikes: 0
# Total Accepted:    209.8K
# Total Submissions: 414.8K
# Testcase Example:  '3'
#
# 给定一个整数 n ，返回 n! 结果中尾随零的数量。
#
# 提示 n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1
#
#
#
# 示例 1：
#
# 输入：n = 3
# 输出：0
# 解释：3! = 6 ，不含尾随 0
#
#
# 示例 2：
#
# 输入：n = 5
# 输出：1
# 解释：5! = 120 ，有一个尾随 0
#
#
# 示例 3：
#
# 输入：n = 0
# 输出：0
#
#
#
#
# 提示：
#
#
# 0 <= n <= 10^4
#
#
#
#
# 进阶：你可以设计并实现对数时间复杂度的算法来解决此问题吗？
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

    def solution1(self, n: int) -> int:
        ans = 0

        for i in range(5, n + 1, 5):
            while i % 5 == 0:
                i //= 5
                ans += 1

        return ans

    def solution2(self, n: int) -> int:
        ans = 0

        while n:
            n //= 5
            ans += n

        return ans

    def trailingZeroes(self, n: int) -> int:
        # return self.solution1(n)
        return self.solution2(n)


# @lc code=end

#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 0\n
# @lcpr case=end

# @lcpr case=start
# 1574\n
# @lcpr case=end

#
