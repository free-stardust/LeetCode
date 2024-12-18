#
# @lc app=leetcode.cn id=54 lang=python3
# @lcpr version=30204
#
# [54] 螺旋矩阵
#
# https://leetcode.cn/problems/spiral-matrix/description/
#
# algorithms
# Medium (51.39%)
# Likes:    1737
# Dislikes: 0
# Total Accepted:    568.6K
# Total Submissions: 1.1M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
#
#
#
# 示例 1：
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#
#
# 示例 2：
#
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#
#
# 提示：
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
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

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        row_len = len(matrix)
        col_len = len(matrix[0])

        left, right, top, bottom = 0, col_len - 1, 0, row_len - 1

        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            
            for i in range(top + 1, bottom + 1):
                ans.append(matrix[i][right])

            if left < right and top < bottom:
            
                for i in range(right - 1, left - 1, -1):
                    ans.append(matrix[bottom][i])

                for i in range(bottom - 1, top, -1):
                    ans.append(matrix[i][left])

            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        return ans


# @lc code=end


def print_matrix(matrix):
    for row in matrix:
        print("\t\t" + str(row))


tests = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
         [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]]
ans = [[1, 2, 3, 6, 9, 8, 7, 4, 5], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]]

for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().spiralOrder(t)
    print(f"test case {i+1}:\n"
          f"\ttest =")
    print_matrix(t)
    print(f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\n
# @lcpr case=end

#
