#
# @lc app=leetcode.cn id=202 lang=python3
# @lcpr version=30204
#
# [202] 快乐数
#
# https://leetcode.cn/problems/happy-number/description/
#
# algorithms
# Easy (64.75%)
# Likes:    1607
# Dislikes: 0
# Total Accepted:    563.6K
# Total Submissions: 867.7K
# Testcase Example:  '19'
#
# 编写一个算法来判断一个数 n 是不是快乐数。
#
# 「快乐数」 定义为：
#
#
# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果这个过程 结果为 1，那么这个数就是快乐数。
#
#
# 如果 n 是 快乐数 就返回 true ；不是，则返回 false 。
#
#
#
# 示例 1：
#
# 输入：n = 19
# 输出：true
# 解释：
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
#
# 示例 2：
#
# 输入：n = 2
# 输出：false
#
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

    def use_hash(self, n: int) -> int:

        def get_power_sum(num: int) -> int:
            pow_sum = 0

            while num > 0:
                pow_sum += pow(num % 10, 2)
                num //= 10

            return pow_sum

        pows = {}
        while n not in pows and n != 1:
            pows[n] = n
            n = get_power_sum(n)

        return n == 1

    def use_double_point(self, n: int) -> int:

        def get_next(num: int) -> int:
            sum_pow = 0

            while num > 0:
                sum_pow += pow(num % 10, 2)
                num //= 10

            return sum_pow

        slow = n
        fast = get_next(n)
        while slow != fast and fast != 1:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1

    def isHappy(self, n: int) -> bool:
        # return self.use_hash(n)
        return self.use_double_point(n)


# @lc code=end

#
# @lcpr case=start
# 19\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 7\n
# @lcpr case=end

#
