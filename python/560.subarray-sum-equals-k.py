#
# @lc app=leetcode.cn id=560 lang=python3
# @lcpr version=30204
#
# [560] 和为 K 的子数组
#
# https://leetcode.cn/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (44.17%)
# Likes:    2479
# Dislikes: 0
# Total Accepted:    538.6K
# Total Submissions: 1.2M
# Testcase Example:  '[1,1,1]\n2'
#
# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
#
# 子数组是数组中元素的连续非空序列。
#
#
#
# 示例 1：
#
# 输入：nums = [1,1,1], k = 2
# 输出：2
#
#
# 示例 2：
#
# 输入：nums = [1,2,3], k = 3
# 输出：2
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7
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

    def sulution1(self, nums: List[int], k: int) -> int:
        ans = 0

        for i in range(len(nums)):
            num_sum = 0
            for j in range(i, -1, -1):
                num_sum += nums[j]
                if num_sum == k:
                    ans += 1

        return ans

    def sulution2(self, nums: List[int], k: int) -> int:
        pre_sum = collections.defaultdict(int)
        ans, pre = 0, 0

        pre_sum[0] = 1

        for num in nums:
            pre += num
            if pre - k in pre_sum:
                ans += pre_sum[pre - k]
            pre_sum[pre] += 1

        return ans

    def subarraySum(self, nums: List[int], k: int) -> int:
        # return self.sulution1(nums, k)
        return self.sulution2(nums, k)


# @lc code=end

#
# @lcpr case=start
# [1,1,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n3\n
# @lcpr case=end

# @lcpr case=start
# [-1,-1,1]\n0\n
# @lcpr case=end

#
