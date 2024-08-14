#
# @lc app=leetcode.cn id=64 lang=python3
# @lcpr version=30204
#
# [64] 最小路径和
#
# https://leetcode.cn/problems/minimum-path-sum/description/
#
# algorithms
# Medium (70.69%)
# Likes:    1703
# Dislikes: 0
# Total Accepted:    637.9K
# Total Submissions: 901.7K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
#
#
#
# 示例 1：
#
# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。
#
#
# 示例 2：
#
# 输入：grid = [[1,2,3],[4,5,6]]
# 输出：12
#
#
#
#
# 提示：
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 200
#
#
#

# @lcpr-template-start
import copy
import collections
import random
from collections import namedtuple
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush


# @lcpr-template-end
# @lc code=start
class Solution:

    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        row_len, col_len = len(grid), len(grid[0])
        dp = [[0] * col_len for _ in range(row_len)]
        dp[0][0] = grid[0][0]

        for col in range(1, col_len):
            dp[0][col] = dp[0][col - 1] + grid[0][col]

        for row in range(1, row_len):
            dp[row][0] = dp[row - 1][0] + grid[row][0]

        for row in range(1, row_len):
            for col in range(1, col_len):
                dp[row][col] += \
                    min(dp[row - 1][col], dp[row][col - 1]) + grid[row][col]

        return dp[row_len - 1][col_len - 1]


# @lc code=end

tests = [[[1, 3, 1], [1, 5, 1], [4, 2, 1]], [[1, 2, 3], [4, 5, 6]]]
ans = [7, 12]
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().minPathSum(t)
    print(f"test case {i+1}:\n"
          f"\ttest = {i+1};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# [[1,3,1],[1,5,1],[4,2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[4,5,6]]\n
# @lcpr case=end

#
