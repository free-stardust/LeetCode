#
# @lc app=leetcode.cn id=957 lang=python3
# @lcpr version=30204
#
# [957] N 天后的牢房
#
# https://leetcode.cn/problems/prison-cells-after-n-days/description/
#
# algorithms
# Medium (37.85%)
# Likes:    153
# Dislikes: 0
# Total Accepted:    21.4K
# Total Submissions: 56.4K
# Testcase Example:  '[0,1,0,1,1,0,0,1]\n7'
#
# 监狱中 8 间牢房排成一排，每间牢房可能被占用或空置。
#
# 每天，无论牢房是被占用或空置，都会根据以下规则进行变更：
#
#
# 如果一间牢房的两个相邻的房间都被占用或都是空的，那么该牢房就会被占用。
# 否则，它就会被空置。
#
#
# 注意：由于监狱中的牢房排成一行，所以行中的第一个和最后一个牢房不存在两个相邻的房间。
#
# 给你一个整数数组 cells ，用于表示牢房的初始状态：如果第 i 间牢房被占用，则 cell[i]==1，否则 cell[i]==0 。另给你一个整数
# n 。
#
# 请你返回 n 天后监狱的状况（即，按上文描述进行 n 次变更）。
#
#
#
# 示例 1：
#
# 输入：cells = [0,1,0,1,1,0,0,1], n = 7
# 输出：[0,0,1,1,0,0,0,0]
# 解释：下表总结了监狱每天的状况：
# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
#
#
# 示例 2：
#
# 输入：cells = [1,0,0,1,0,0,1,0], n = 1000000000
# 输出：[0,0,1,1,1,1,1,0]
#
#
#
#
# 提示：
#
#
# cells.length == 8
# cells[i] 为 0 或 1
# 1 <= n <= 10^9
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

    def solution1(self, cells: List[int], n: int) -> List[int]:

        def nextday(cells):
            new = [0] * 8
            for i in range(8):
                new[i] = int(i > 0 and i < 7 and cells[i - 1] == cells[i + 1])
            return new

        seen = {}
        while n > 0:
            c = tuple(cells)

            if c in seen:
                n %= seen[c] - n

            seen[c] = n

            if n >= 1:
                n -= 1
                cells = nextday(cells)

        return cells

    def solution2(self, cells: List[int], n: int) -> List[int]:

        def nextday(cells):
            new = [0] * 8
            for i in range(8):
                new[i] = int(i > 0 and i < 7 and cells[i - 1] == cells[i + 1])
            return new

        n_remains = n % 14
        n = n_remains if n_remains != 0 else 14

        while n > 0:
            cells = nextday(cells)
            n -= 1

        return cells

    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        # return self.solution1(cells, n)
        return self.solution2(cells, n)


# @lc code=end

#
# @lcpr case=start
# [0,1,0,1,1,0,0,1]\n7\n
# @lcpr case=end

# @lcpr case=start
# [1,0,0,1,0,0,1,0]\n1000000000\n
# @lcpr case=end

# @lcpr case=start
# [1,1,0,1,1,0,0,1]\n300663720\n
# @lcpr case=end

#
