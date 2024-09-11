#
# @lc app=leetcode.cn id=118 lang=python3
# @lcpr version=30204
#
# [118] 杨辉三角
#
# https://leetcode.cn/problems/pascals-triangle/description/
#
# algorithms
# Easy (76.24%)
# Likes:    1185
# Dislikes: 0
# Total Accepted:    559.6K
# Total Submissions: 731.9K
# Testcase Example:  '5'
#
# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
#
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
#
#
#
#
#
# 示例 1:
#
# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#
#
# 示例 2:
#
# 输入: numRows = 1
# 输出: [[1]]
#
#
#
#
# 提示:
#
#
# 1 <= numRows <= 30
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

    def generate(self, numRows: int) -> List[List[int]]:
        ans = []

        for i in range(numRows):
            tmp_ans = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    tmp_ans.append(1)
                else:
                    tmp_ans.append(ans[i - 1][j] + ans[i - 1][j - 1])
            ans.append(tmp_ans)

        return ans


# @lc code=end

tests = [5, 1]
ans = [[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]], [[1]]]
all_pass = True
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().generate(t)
    all_pass &= (a == res)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res};")
print(f"all pass: {all_pass}.")

#
# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#
