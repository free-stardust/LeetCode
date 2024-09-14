#
# @lc app=leetcode.cn id=416 lang=python3
# @lcpr version=30204
#
# [416] 分割等和子集
#
# https://leetcode.cn/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (52.61%)
# Likes:    2148
# Dislikes: 0
# Total Accepted:    610.5K
# Total Submissions: 1.2M
# Testcase Example:  '[1,5,11,5]'
#
# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
#
#
#
# 示例 1：
#
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。
#
# 示例 2：
#
# 输入：nums = [1,2,3,5]
# 输出：false
# 解释：数组不能分割成两个元素和相等的子集。
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
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

    def use_dp1(self, nums: List[int]) -> bool:
        nums_len = len(nums)
        if nums_len < 2:
            return False

        total = sum(nums)
        max_num = max(nums)
        if max_num > total:
            return False

        if total & 1:
            return False

        target = total // 2
        dp = [[False] * (target + 1) for _ in range(nums_len)]

        for i in range(nums_len):
            dp[i][0] = True

        for i in range(nums_len):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[nums_len - 1][target]

    def use_dp2(self, nums: List[int]) -> bool:
        nums_len = len(nums)
        if nums_len < 2:
            return False

        total = sum(nums)
        max_num = max(nums)
        if max_num > total:
            return False

        if total & 1:
            return False

        target = total // 2
        dp = [True] + [False] * target
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] |= dp[i - num]

        return dp[target]

    def canPartition(self, nums: List[int]) -> bool:
        # return self.use_dp1(nums)
        return self.use_dp2(nums)


# @lc code=end

#
# @lcpr case=start
# [1,5,11,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,5]\n
# @lcpr case=end

#
