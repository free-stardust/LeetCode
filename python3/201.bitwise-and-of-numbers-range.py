#
# @lc app=leetcode.cn id=201 lang=python3
# @lcpr version=30204
#
# [201] 数字范围按位与
#
# https://leetcode.cn/problems/bitwise-and-of-numbers-range/description/
#
# algorithms
# Medium (54.82%)
# Likes:    528
# Dislikes: 0
# Total Accepted:    99.3K
# Total Submissions: 180.6K
# Testcase Example:  '5\n7'
#
# 给你两个整数 left 和 right ，表示区间 [left, right] ，返回此区间内所有数字 按位与 的结果（包含 left 、right
# 端点）。
#
#
#
# 示例 1：
#
# 输入：left = 5, right = 7
# 输出：4
#
#
# 示例 2：
#
# 输入：left = 0, right = 0
# 输出：0
#
#
# 示例 3：
#
# 输入：left = 1, right = 2147483647
# 输出：0
#
#
#
#
# 提示：
#
#
# 0 <= left <= right <= 2^31 - 1
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

    def solution1(self, left: int, right: int) -> int:
        # 原理：只看第一个二进制位，只存在 0,1 两种情况，所以如果 left < right，区间中必然
        #      存在 left+1,那么最低位 & 一下一定等于 0，然后不停的右移，一直移到两个相等为
        #      止
        shift = 0

        while left < right:
            left >>= 1
            right >>= 1
            shift += 1

        return left << shift

    def solution2(self, left: int, right: int) -> int:
        # 这个解法基于这样一个事实：对于 left 和 right 中间的值（包括边界），公共前缀之外的
        # 位置，那必然存在一个 0，这样与之后必然位 0，而只有公共前缀为 1，且如果 right 位数
        # 比 left 位数多，必然不存在公共前缀，所以利用下面这种算法，逐步过滤掉 right 右边的
        # 1，直到 right 小于等于 left，而当 right 大于 left 时，其必然是介于原始 left 和
        # right 之间的值，而当 left 等于 right 时，则说明 right 已经将 left 右边的值与完
        # 并且结果是 left，这样的话，与 left 与必然是 left，而当 right 与之前比 left 大，
        # 与之后比 left 小，那就说明 right 的位数多于了 left，实际上对于这种情况，其结果必
        # 然为 0
        while left < right:
            right &= (right - 1)

        return right

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # return self.solution1(left, right)
        return self.solution2(left, right)


# @lc code=end

#
# @lcpr case=start
# 5\n7\n
# @lcpr case=end

# @lcpr case=start
# 0\n0\n
# @lcpr case=end

# @lcpr case=start
# 1\n2147483647\n
# @lcpr case=end

# @lcpr case=start
# 12\n12\n
# @lcpr case=end

#
