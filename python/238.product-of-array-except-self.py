#
# @lc app=leetcode.cn id=238 lang=python3
# @lcpr version=30204
#
# [238] 除自身以外数组的乘积
#
# https://leetcode.cn/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (76.08%)
# Likes:    1862
# Dislikes: 0
# Total Accepted:    519.9K
# Total Submissions: 680.8K
# Testcase Example:  '[1,2,3,4]'
#
# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
#
# 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
#
# 请 不要使用除法，且在 O(n) 时间复杂度内完成此题。
#
#
#
# 示例 1:
#
# 输入: nums = [1,2,3,4]
# 输出: [24,12,8,6]
#
#
# 示例 2:
#
# 输入: nums = [-1,1,0,-3,3]
# 输出: [0,0,9,0,0]
#
#
#
#
# 提示：
#
#
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内
#
#
#
#
# 进阶：你可以在 O(1) 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组 不被视为 额外空间。）
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

    def use_double_point(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        ans = [1] * nums_len
        left, right = 0, nums_len - 1
        left_acc, right_acc = 1, 1

        while left < nums_len and right >= 0:
            ans[left] *= left_acc
            ans[right] *= right_acc
            left_acc *= nums[left]
            right_acc *= nums[right]
            left += 1
            right -= 1

        return ans

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.use_double_point(nums)


# @lc code=end

tests = [[1, 2, 3, 4], [-1, 1, 0, -3, 3]]
ans = [[24, 12, 8, 6], [0, 0, 9, 0, 0]]
all_pass = True
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().productExceptSelf(t)
    all_pass &= (a == res)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res};")
print(f"all pass: {all_pass}.")
#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [-1,1,0,-3,3]\n
# @lcpr case=end

#
