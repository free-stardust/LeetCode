#
# @lc app=leetcode.cn id=74 lang=python3
# @lcpr version=30204
#
# [74] 搜索二维矩阵
#
# https://leetcode.cn/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (49.98%)
# Likes:    959
# Dislikes: 0
# Total Accepted:    439.3K
# Total Submissions: 877.7K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3'
#
# 给你一个满足下述两条属性的 m x n 整数矩阵：
#
#
# 每行中的整数从左到右按非严格递增顺序排列。
# 每行的第一个整数大于前一行的最后一个整数。
#
#
# 给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# 输出：true
#
#
# 示例 2：
#
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# 输出：false
#
#
#
#
# 提示：
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4
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

    def two_bin_search(self, matrix: List[List[int]], target: int) -> bool:

        def bin_search_first_col() -> int:
            low, high = -1, len(matrix) - 1
            while low < high:
                mid = low + (high - low + 1) // 2
                if matrix[mid][0] <= target:
                    low = mid
                else:
                    high = mid - 1
            return low

        def bin_search_second_row(row: int) -> bool:
            left, right = 0, len(matrix[0]) - 1

            while left <= right:
                mid = left + (right - left) // 2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return False

        row = bin_search_first_col()

        if row < 0:
            return False

        ans = bin_search_second_row(row)

        return ans

    def bin_search(self, matrix: List[List[int]], target: int) -> bool:
        row_len, col_len = len(matrix), len(matrix[0])
        left, right = 0, row_len * col_len - 1

        while left <= right:
            mid = left + (right - left) // 2
            value = matrix[mid // col_len][mid % col_len]
            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # return self.two_bin_search(matrix, target)
        return self.bin_search(matrix, target)


# @lc code=end

tests = [[[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3],
         [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13], [[[1, 3]],
                                                                    3]]
ans = [True, False, True]
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().searchMatrix(t[0], t[1])
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3\n
# @lcpr case=end

# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n13\n
# @lcpr case=end

#
