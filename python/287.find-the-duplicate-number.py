#
# @lc app=leetcode.cn id=287 lang=python3
# @lcpr version=30204
#
# [287] 寻找重复数
#
# https://leetcode.cn/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (64.67%)
# Likes:    2466
# Dislikes: 0
# Total Accepted:    420.5K
# Total Submissions: 648K
# Testcase Example:  '[1,3,4,2,2]'
#
# 给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。
#
# 假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。
#
# 你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。
#
#
#
# 示例 1：
#
# 输入：nums = [1,3,4,2,2]
# 输出：2
#
#
# 示例 2：
#
# 输入：nums = [3,1,3,4,2]
# 输出：3
#
#
# 示例 3 :
#
# 输入：nums = [3,3,3,3,3]
# 输出：3
#
#
#
#
#
#
# 提示：
#
#
# 1 <= n <= 10^5
# nums.length == n + 1
# 1 <= nums[i] <= n
# nums 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次
#
#
#
#
# 进阶：
#
#
# 如何证明 nums 中至少存在一个重复的数字?
# 你可以设计一个线性级时间复杂度 O(n) 的解决方案吗？
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

    def use_binary_search(self, nums: List[int]) -> int:
        num_len = len(nums)
        left, right, ans = 1, num_len - 1, -1

        while left <= right:
            mid = (left + right) >> 1
            cnt = 0

            for i in range(num_len):
                cnt += 1 if nums[i] <= mid else 0

            if cnt <= mid:
                left = mid + 1
            else:
                right = mid - 1
                ans = mid

        return ans

    def use_double_point(self, nums: List[int]) -> int:
        slow = fast = 0
        slow = nums[slow]
        fast = nums[nums[fast]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        pre1, pre2 = 0, slow

        while pre1 != pre2:
            pre1 = nums[pre1]
            pre2 = nums[pre2]

        return pre1

    def findDuplicate(self, nums: List[int]) -> int:
        # return self.use_binary_search(nums)
        return self.use_double_point(nums)


# @lc code=end

#
# @lcpr case=start
# [1,3,4,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,1,3,4,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,3,3,3]\n
# @lcpr case=end

#
