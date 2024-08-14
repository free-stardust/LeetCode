#
# @lc app=leetcode.cn id=63 lang=python3
# @lcpr version=30204
#
# [63] 不同路径 II
#
# https://leetcode.cn/problems/unique-paths-ii/description/
#
# algorithms
# Medium (41.54%)
# Likes:    1275
# Dislikes: 0
# Total Accepted:    518.5K
# Total Submissions: 1.2M
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。
#
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
#
# 网格中的障碍物和空位置分别用 1 和 0 来表示。
#
#
#
# 示例 1：
#
# 输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# 输出：2
# 解释：3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
#
#
# 示例 2：
#
# 输入：obstacleGrid = [[0,1],[0,0]]
# 输出：1
#
#
#
#
# 提示：
#
#
# m == obstacleGrid.length
# n == obstacleGrid[i].length
# 1 <= m, n <= 100
# obstacleGrid[i][j] 为 0 或 1
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

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row_len, col_len = len(obstacleGrid), len(obstacleGrid[0])
        ans = [0] * col_len
        ans[0] = 1

        for i in range(row_len):
            for j in range(col_len):
                if obstacleGrid[i][j] == 1:
                    ans[j] = 0
                    continue
                if j - 1 >= 0 and obstacleGrid[i][j - 1] == 0:
                    ans[j] += ans[j - 1]

        return ans[-1]


# @lc code=end


def print_map(matrix: List[int]) -> str:
    for row in matrix:
        print("\t\t" + str(row))


tests = [[[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 1], [0, 0]],
         [[0,1,1,1,0,0,0],[0,0,0,0,0,1,0],[1,1,1,1,0,1,0]]]
ans = [2, 1, 1]
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().uniquePathsWithObstacles(t)
    print(f"test case {i+1}:\n"
          f"\ttest =")
    print_map(t)
    print(f"\tans = {a};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# [[0,0,0],[0,1,0],[0,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1],[0,0]]\n
# @lcpr case=end

#
