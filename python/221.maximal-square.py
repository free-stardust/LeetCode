#
# @lc app=leetcode.cn id=221 lang=python3
# @lcpr version=30204
#
# [221] 最大正方形
#
# https://leetcode.cn/problems/maximal-square/description/
#
# algorithms
# Medium (50.77%)
# Likes:    1699
# Dislikes: 0
# Total Accepted:    348.1K
# Total Submissions: 685.7K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
#
#
#
# 示例 1：
#
# 输入：matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# 输出：4
#
#
# 示例 2：
#
# 输入：matrix = [["0","1"],["1","0"]]
# 输出：1
#
#
# 示例 3：
#
# 输入：matrix = [["0"]]
# 输出：0
#
#
#
#
# 提示：
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] 为 '0' 或 '1'
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

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        max_side = 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == "1":
                    if row == 0 or col == 0:
                        dp[row][col] = 1
                    else:
                        dp[row][col] = min(dp[row - 1][col], dp[row][col - 1],
                                           dp[row - 1][col - 1]) + 1
                    max_side = max(max_side, dp[row][col])

        ans = max_side * max_side
        return ans


# @lc code=end

#
# @lcpr case=start
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["0","1"],["1","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["0"]]\n
# @lcpr case=end

#
