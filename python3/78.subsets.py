#
# @lc app=leetcode.cn id=78 lang=python3
# @lcpr version=30204
#
# [78] 子集
#
# https://leetcode.cn/problems/subsets/description/
#
# algorithms
# Medium (81.50%)
# Likes:    2349
# Dislikes: 0
# Total Accepted:    847.4K
# Total Submissions: 1M
# Testcase Example:  '[1,2,3]'
#
# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
#
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
#
# 示例 2：
#
# 输入：nums = [0]
# 输出：[[],[0]]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# nums 中的所有元素 互不相同
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

    def solution1(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for i in range(len(nums)):
            for j in range(len(res)):
                res.append(res[j] + [nums[i]])

        return res

    def solution2(self, nums: List[int]) -> List[List[int]]:
        sub = []
        ans = []

        nums_len = len(nums)

        for mask in range(1 << nums_len):
            sub.clear()
            for i in range(nums_len):
                if mask & (1 << i):
                    sub.append(nums[i])
            ans.append(sub[:])

        return ans

    def solution3(self, nums: List[int]) -> List[List[int]]:
        sub = []
        ans = []

        def dfs(cur, nums):
            if cur == len(nums):
                ans.append(sub[:])
                return
            sub.append(nums[cur])
            dfs(cur + 1, nums)
            sub.pop()
            dfs(cur + 1, nums)

        dfs(0, nums)

        return ans

    def subsets(self, nums: List[int]) -> List[List[int]]:
        # return self.solution1(nums)
        # return self.solution2(nums)
        return self.solution3(nums)


# @lc code=end

tests = [[1, 2, 3], [0]]
ans = [[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]], [[], [0]]]
all_pass = True
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().subsets(t)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res};")
    all_pass &= (a == res)
print(f"all pass: {all_pass}.")

#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#
