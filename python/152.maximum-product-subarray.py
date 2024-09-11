#
# @lc app=leetcode.cn id=152 lang=python3
# @lcpr version=30204
#
# [152] 乘积最大子数组
#
# https://leetcode.cn/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (42.20%)
# Likes:    2307
# Dislikes: 0
# Total Accepted:    468.6K
# Total Submissions: 1.1M
# Testcase Example:  '[2,3,-2,4]'
#
# 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续 子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
#
# 测试用例的答案是一个 32-位 整数。
#
#
#
# 示例 1:
#
# 输入: nums = [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#
#
# 示例 2:
#
# 输入: nums = [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
#
#
#
# 提示:
#
#
# 1 <= nums.length <= 2 * 10^4
# -10 <= nums[i] <= 10
# nums 的任何子数组的乘积都 保证 是一个 32-位 整数
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

    def maxProduct(self, nums: List[int]) -> int:
        ans = min_mul = max_mul = nums[0]

        for i in range(1, len(nums)):
            mul1, mul2 = nums[i] * max_mul, nums[i] * min_mul
            max_mul = max(mul1, mul2, nums[i])
            min_mul = min(mul1, mul2, nums[i])
            ans = ans if max_mul <= ans else max_mul

        return ans


# @lc code=end

tests = [[2, 3, -2, 4], [-2, 0, -1], [-2], [-4, -3, -2]]
ans = [6, 0, -2, 12]
all_pass = True
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().maxProduct(t)
    all_pass &= (a == res)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres= {res};\n"
          f"\t{a == res};")
print(f"all pass: {all_pass}.")

#
# @lcpr case=start
# [2,3,-2,4]\n
# @lcpr case=end

# @lcpr case=start
# [-2,0,-1]\n
# @lcpr case=end

#
