#
# @lc app=leetcode.cn id=77 lang=python3
# @lcpr version=30204
#
# [77] 组合
#
# https://leetcode.cn/problems/combinations/description/
#
# algorithms
# Medium (77.16%)
# Likes:    1657
# Dislikes: 0
# Total Accepted:    756.1K
# Total Submissions: 979.4K
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
#
# 你可以按 任何顺序 返回答案。
#
#
#
# 示例 1：
#
# 输入：n = 4, k = 2
# 输出：
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
#
# 示例 2：
#
# 输入：n = 1, k = 1
# 输出：[[1]]
#
#
#
# 提示：
#
#
# 1 <= n <= 20
# 1 <= k <= n
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

    def recursion1(self, n: int, k: int) -> List[List[int]]:
        ans = []
        tmp = []

        def dfs(cur: int) -> None:
            if len(tmp) + (n - cur + 1) < k:
                return

            if len(tmp) == k:
                ans.append(tmp.copy())
                return

            tmp.append(cur)
            dfs(cur + 1)
            tmp.pop()
            dfs(cur + 1)

        dfs(1)

        return ans

    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.recursion1(n, k)


# @lc code=end

tests = [[4, 2], [1, 1]]
ans = [[[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]], [[1]]]
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().combine(t[0], t[1])
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# 4\n2\n
# @lcpr case=end

# @lcpr case=start
# 1\n1\n
# @lcpr case=end

#
