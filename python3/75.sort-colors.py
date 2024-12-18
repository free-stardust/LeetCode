#
# @lc app=leetcode.cn id=75 lang=python3
# @lcpr version=30204
#
# [75] 颜色分类
#
# https://leetcode.cn/problems/sort-colors/description/
#
# algorithms
# Medium (61.51%)
# Likes:    1822
# Dislikes: 0
# Total Accepted:    674.1K
# Total Submissions: 1.1M
# Testcase Example:  '[2,0,2,1,1,0]'
#
# 给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地 对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
#
# 我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
#
#
#
#
# 必须在不使用库内置的 sort 函数的情况下解决这个问题。
#
#
#
# 示例 1：
#
# 输入：nums = [2,0,2,1,1,0]
# 输出：[0,0,1,1,2,2]
#
#
# 示例 2：
#
# 输入：nums = [2,0,1]
# 输出：[0,1,2]
#
#
#
#
# 提示：
#
#
# n == nums.length
# 1 <= n <= 300
# nums[i] 为 0、1 或 2
#
#
#
#
# 进阶：
#
#
# 你能想出一个仅使用常数空间的一趟扫描算法吗？
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

    def single_point(self, nums: List[int]) -> None:
        nums_len = len(nums)
        p = 0

        for i in range(nums_len):
            if nums[i] == 0:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1

        for i in range(p, nums_len):
            if nums[i] == 1:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1

    def double_point1(self, nums: List[int]) -> None:
        nums_len = len(nums)
        p0 = p1 = 0

        for i in range(nums_len):
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 < p1:
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                p1 += 1
            elif nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1

    def double_point2(self, nums: List[int]) -> None:
        p0, p2 = 0, len(nums) - 1
        i = 0

        while i <= p2:
            while i <= p2 and nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1

            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1

            i += 1

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # self.single_point(nums)
        # self.double_point1(nums)
        self.double_point2(nums)


# @lc code=end

#
# @lcpr case=start
# [2,0,2,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [2,0,1]\n
# @lcpr case=end

#
