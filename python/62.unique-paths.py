#
# @lc app=leetcode.cn id=62 lang=python3
# @lcpr version=30204
#
# [62] 不同路径
#
# https://leetcode.cn/problems/unique-paths/description/
#
# algorithms
# Medium (68.49%)
# Likes:    2079
# Dislikes: 0
# Total Accepted:    843.2K
# Total Submissions: 1.2M
# Testcase Example:  '3\n7'
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
#
# 问总共有多少条不同的路径？
#
#
#
# 示例 1：
#
# 输入：m = 3, n = 7
# 输出：28
#
# 示例 2：
#
# 输入：m = 3, n = 2
# 输出：3
# 解释：
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向下
#
#
# 示例 3：
#
# 输入：m = 7, n = 3
# 输出：28
#
#
# 示例 4：
#
# 输入：m = 3, n = 3
# 输出：6
#
#
#
# 提示：
#
#
# 1 <= m, n <= 100
# 题目数据保证答案小于等于 2 * 10^9
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

    def dfs(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        return self.dfs(m - 1, n) + self.dfs(m, n - 1)

    def dp1(self, m: int, n: int) -> int:
        f = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]

        return f[m - 1][n - 1]

    def dp2(self, m: int, n: int) -> int:
        f = [1] * n

        for _ in range(1, m):
            for j in range(1, n):
                f[j] += f[j - 1]

        return f[n - 1]

    def uniquePaths(self, m: int, n: int) -> int:
        # return self.dfs(m, n)
        # return self.dp1(m, n)
        return self.dp2(m, n)


# @lc code=end

#
# @lcpr case=start
# 3\n7\n
# @lcpr case=end

# @lcpr case=start
# 3\n2\n
# @lcpr case=end

# @lcpr case=start
# 7\n3\n
# @lcpr case=end

# @lcpr case=start
# 3\n3\n
# @lcpr case=end

# @lcpr case=start
# 23\n12\n
# @lcpr case=end
#
