#
# @lc app=leetcode.cn id=85 lang=python3
# @lcpr version=30204
#
# [85] 最大矩形
#
# https://leetcode.cn/problems/maximal-rectangle/description/
#
# algorithms
# Hard (55.48%)
# Likes:    1702
# Dislikes: 0
# Total Accepted:    208.8K
# Total Submissions: 376.3K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
#
#
#
# 示例 1：
#
# 输入：matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# 输出：6
# 解释：最大矩形如上图所示。
#
#
# 示例 2：
#
# 输入：matrix = [["0"]]
# 输出：0
#
#
# 示例 3：
#
# 输入：matrix = [["1"]]
# 输出：1
#
#
#
#
# 提示：
#
#
# rows == matrix.length
# cols == matrix[0].length
# 1 <= row, cols <= 200
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

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in range(rows):
            # 更新每列的高度
            for col in range(cols):
                if matrix[row][col] == "1":
                    heights[col] += 1
                else:
                    heights[col] = 0

            # 计算当前行的最大矩形面积
            stack = []
            for i in range(cols + 1):
                h = heights[i] if i < cols else 0
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    width = i - stack[-1] - 1 if stack else i
                    max_area = max(max_area, height * width)
                stack.append(i)

        return max_area


# @lc code=end

tests = [
    [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ],
    [
        ["0"],
    ],
    [
        ["1"],
    ],
]
ans = [6, 0, 1]
all_pass = True
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().maximalRectangle(t)
    print(f"test case {i + 1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")
    all_pass &= a == res
print(f"all pass: {all_pass}.")
#
# @lcpr case=start
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["1"]]\n
# @lcpr case=end

#
