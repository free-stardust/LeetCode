#
# @lc app=leetcode.cn id=219 lang=python3
# @lcpr version=30204
#
# [219] 存在重复元素 II
#
# https://leetcode.cn/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (47.62%)
# Likes:    726
# Dislikes: 0
# Total Accepted:    332.2K
# Total Submissions: 697.5K
# Testcase Example:  '[1,2,3,1]\n3'
#
# 给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i
# - j) <= k 。如果存在，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3,1], k = 3
# 输出：true
#
# 示例 2：
#
# 输入：nums = [1,0,1,1], k = 1
# 输出：true
#
# 示例 3：
#
# 输入：nums = [1,2,3,1,2,3], k = 2
# 输出：false
#
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 0 <= k <= 10^5
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

    def use_hash(self, nums: List[int], k: int) -> bool:
        data = {}

        for i, num in enumerate(nums):
            if num in data and i - data[num] <= k:
                return True
            data[num] = i

        return False

    def use_slide_win(self, nums: List[int], k: int) -> bool:
        s = set()

        for i, num in enumerate(nums):
            if i > k:
                s.remove(nums[i - k - 1])
            if num in s:
                return True
            s.add(num)

        return False

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # return self.use_hash(nums, k)
        return self.use_slide_win(nums, k)


# @lc code=end

#
# @lcpr case=start
# [1,2,3,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1,2,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6,7,8,9,10]\n15\n
# @lcpr case=end

#
