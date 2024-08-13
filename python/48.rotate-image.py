#
# @lc app=leetcode.cn id=48 lang=python3
# @lcpr version=30204
#
# [48] 旋转图像
#
# https://leetcode.cn/problems/rotate-image/description/
#
# algorithms
# Medium (76.64%)
# Likes:    1909
# Dislikes: 0
# Total Accepted:    617.6K
# Total Submissions: 805.1K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
#
# 你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
#
#
#
# 示例 1：
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[[7,4,1],[8,5,2],[9,6,3]]
#
#
# 示例 2：
#
# 输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# 输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
#
#
#
#
# 提示：
#
#
# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000
#
#
#
#
#

# @lcpr-template-start
import copy
import collections
from collections import namedtuple
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush


# @lcpr-template-end
# @lc code=start
class Solution:

    def base_transpose_for_rotate1(self, matrix: List[List[int]]) -> None:
        dim = len(matrix)

        for i in range(dim):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(dim):
            for j in range(dim // 2):
                matrix[i][j], matrix[i][dim - j - 1] \
                    = matrix[i][dim - j - 1], matrix[i][j]
                
    def base_transpose_for_rotate2(self, matrix: List[List[int]]) -> None:
        dim = len(matrix)

        for i in range(dim // 2):
            matrix[i], matrix[dim - i - 1] = matrix[dim - i - 1], matrix[i]

        for i in range(dim):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # self.base_transpose_for_rotate1(matrix)
        self.base_transpose_for_rotate2(matrix)


# @lc code=end


def print_matrix(matrix):
    for row in matrix:
        print("\t\t" + str(row))


tests = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
         [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]]
ans = [[[7, 4, 1], [8, 5, 2], [9, 6, 3]],
       [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]]
for i, (t, a) in enumerate(zip(tests, ans)):
    origin_matrix = copy.deepcopy(t)
    Solution().rotate(t)
    print(f"test case {i+1}:\n"
          f"\ttest = ")
    print_matrix(origin_matrix)
    print(f"\tans = ")
    print_matrix(a)
    print("\tres = ")
    print_matrix(t)
    print(f"\t{a == t}.")

#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]\n
# @lcpr case=end

#
