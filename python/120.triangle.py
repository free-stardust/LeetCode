#
# @lc app=leetcode.cn id=120 lang=python3
# @lcpr version=30204
#
# [120] 三角形最小路径和
#
# https://leetcode.cn/problems/triangle/description/
#
# algorithms
# Medium (68.84%)
# Likes:    1359
# Dislikes: 0
# Total Accepted:    368.9K
# Total Submissions: 535.4K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# 给定一个三角形 triangle ，找出自顶向下的最小路径和。
#
# 每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1
# 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。
#
#
#
# 示例 1：
#
# 输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# 输出：11
# 解释：如下面简图所示：
# ⁠  2
# ⁠ 3 4
# ⁠6 5 7
# 4 1 8 3
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
#
#
# 示例 2：
#
# 输入：triangle = [[-10]]
# 输出：-10
#
#
#
#
# 提示：
#
#
# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -10^4 <= triangle[i][j] <= 10^4
#
#
#
#
# 进阶：
#
#
# 你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题吗？
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

    def dp(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [0] * n
        f[0] = triangle[0][0]

        for i in range(1, n):
            f[i] = f[i - 1] + triangle[i][i]
            for j in range(i - 1, 0, -1):
                f[j] = min(f[j - 1], f[j]) + triangle[i][j]
            print(f)
            f[0] += triangle[i][0]

        return min(f)

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.dp(triangle)


# @lc code=end

tests = [[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], [[-10]]]
ans = [11, -10]
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().minimumTotal(t)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# [[2],[3,4],[6,5,7],[4,1,8,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[-10]]\n
# @lcpr case=end

#
