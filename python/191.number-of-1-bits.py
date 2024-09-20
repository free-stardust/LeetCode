#
# @lc app=leetcode.cn id=191 lang=python3
# @lcpr version=30204
#
# [191] 位1的个数
#
# https://leetcode.cn/problems/number-of-1-bits/description/
#
# algorithms
# Easy (77.76%)
# Likes:    649
# Dislikes: 0
# Total Accepted:    397.3K
# Total Submissions: 509.5K
# Testcase Example:  '11'
#
# 编写一个函数，获取一个正整数的二进制形式并返回其二进制表达式中 设置位 的个数（也被称为汉明重量）。
#
#
#
# 示例 1：
#
# 输入：n = 11
# 输出：3
# 解释：输入的二进制串 1011 中，共有 3 个设置位。
#
#
# 示例 2：
#
# 输入：n = 128
# 输出：1
# 解释：输入的二进制串 10000000 中，共有 1 个设置位。
#
#
# 示例 3：
#
# 输入：n = 2147483645
# 输出：30
# 解释：输入的二进制串 11111111111111111111111111111101 中，共有 30 个设置位。
#
#
#
# 提示：
#
#
# 1 <= n <= 2^31 - 1
#
#
#
#
#
#
#
# 进阶：
#
#
# 如果多次调用这个函数，你将如何优化你的算法？
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

    def solution1(self, n: int) -> int:
        ans = 0

        for i in range(32):
            if n & (1 << i):
                ans += 1

        return ans

    def solution2(self, n: int) -> int:
        ans = 0

        while n:
            n &= n - 1
            ans += 1

        return ans

    def hammingWeight(self, n: int) -> int:
        # return self.solution1(n)
        return self.solution2(n)


# @lc code=end

#
# @lcpr case=start
# 11\n
# @lcpr case=end

# @lcpr case=start
# 128\n
# @lcpr case=end

# @lcpr case=start
# 2147483645\n
# @lcpr case=end

#
