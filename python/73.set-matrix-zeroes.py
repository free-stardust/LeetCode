#
# @lc app=leetcode.cn id=73 lang=python3
# @lcpr version=30204
#
# [73] 矩阵置零
#
# https://leetcode.cn/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (67.55%)
# Likes:    1093
# Dislikes: 0
# Total Accepted:    408.3K
# Total Submissions: 602.8K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：[[1,0,1],[0,0,0],[1,0,1]]
# 
# 
# 示例 2：
# 
# 输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# 输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
# 
# 
# 
# 
# 提示：
# 
# 
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -2^31 <= matrix[i][j] <= 2^31 - 1
# 
# 
# 
# 
# 进阶：
# 
# 
# 一个直观的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
# 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
# 你能想出一个仅使用常量空间的解决方案吗？
# 
# 
#


# @lcpr-template-start
import copy
import collections
import random
import math
from collections import namedtuple
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush
# @lcpr-template-end
# @lc code=start
class Solution:
    def use_arrays(self, matrix: List[List[int]]) -> None:
        row_len, col_len = len(matrix), len(matrix[0])

        mark_row, mark_col = [0] * row_len, [0] * col_len
        for i in range(row_len):
            for j in range(col_len):
                if matrix[i][j] == 0:
                    mark_row[i] = mark_col[j] = 1
        
        for i in range(row_len):
            for j in range(col_len):
                if mark_row[i] or mark_col[j]:
                    matrix[i][j] = 0

    
    def use_two_mark(self, matrix: List[List[int]]) -> None:
        row_len, col_len = len(matrix), len(matrix[0])

        first_row_zero = any(matrix[0][j] == 0 for j in range(col_len))
        first_col_zero = any(matrix[i][0] == 0 for i in range(row_len))

        for i in range(1, row_len):
            for j in range(1, col_len):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        for i in range(1, row_len):
            for j in range(1, col_len):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_zero:
            for i in range(col_len):
                matrix[0][i] = 0
        
        if first_col_zero:
            for i in range(row_len):
                matrix[i][0] = 0


    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # self.use_arrays(matrix)
        self.use_two_mark(matrix)
# @lc code=end

tests = [[[1,1,1],[1,0,1],[1,1,1]], [[0,1,2,0],[3,4,5,2],[1,3,1,5]]]
ans = [[[1,0,1],[0,0,0],[1,0,1]], [[0,0,0,0],[0,4,5,0],[0,3,1,0]]]
for i,(t,a) in enumerate(zip(tests,ans)):
    test = t
    Solution().setZeroes(t)
    print(f"test case {i+1}:\n"
          f"\ttest = {test};\n"
          f"\tans = {a};\n"
          f"\tres = {t};\n"
          f"\t{a == t}.")

#
# @lcpr case=start
# [[1,1,1],[1,0,1],[1,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1,2,0],[3,4,5,2],[1,3,1,5]]\n
# @lcpr case=end

#

