#
# @lc app=leetcode.cn id=162 lang=python3
# @lcpr version=30204
#
# [162] 寻找峰值
#
# https://leetcode.cn/problems/find-peak-element/description/
#
# algorithms
# Medium (49.52%)
# Likes:    1314
# Dislikes: 0
# Total Accepted:    425.4K
# Total Submissions: 858.9K
# Testcase Example:  '[1,2,3,1]'
#
# 峰值元素是指其值严格大于左右相邻值的元素。
#
# 给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
#
# 你可以假设 nums[-1] = nums[n] = -∞ 。
#
# 你必须实现时间复杂度为 O(log n) 的算法来解决此问题。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3,1]
# 输出：2
# 解释：3 是峰值元素，你的函数应该返回其索引 2。
#
# 示例 2：
#
# 输入：nums = [1,2,1,3,5,6,4]
# 输出：1 或 5
# 解释：你的函数可以返回索引 1，其峰值元素为 2；
# 或者返回索引 5， 其峰值元素为 6。
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 1000
# -2^31 <= nums[i] <= 2^31 - 1
# 对于所有有效的 i 都有 nums[i] != nums[i + 1]
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

    def solution1(self, nums: List[int]) -> int:
        idx = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[idx]:
                idx = i

        return idx

    def solution2(self, nums: List[int]) -> int:
        nums_len = len(nums)

        def get_value(index):
            if index == -1 or index == nums_len:
                return float('-inf')
            return nums[index]

        left, right, ans = 0, nums_len - 1, -1

        while left <= right:
            mid = (left + right) // 2

            if get_value(mid - 1) < get_value(mid) > get_value(mid + 1):
                ans = mid
                break

            if get_value(mid) < get_value(mid + 1):
                left = mid + 1
            else:
                right = mid - 1

        return ans

    def findPeakElement(self, nums: List[int]) -> int:
        # return self.solution1(nums)
        return self.solution2(nums)


# @lc code=end

#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1,3,5,6,4]\n
# @lcpr case=end

#
