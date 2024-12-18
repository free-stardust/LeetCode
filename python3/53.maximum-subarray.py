#
# @lc app=leetcode.cn id=53 lang=python3
# @lcpr version=30204
#
# [53] 最大子数组和
#
# https://leetcode.cn/problems/maximum-subarray/description/
#
# algorithms
# Medium (55.50%)
# Likes:    6737
# Dislikes: 0
# Total Accepted:    1.8M
# Total Submissions: 3.3M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 子数组 是数组中的一个连续部分。
#
#
#
# 示例 1：
#
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
#
#
# 示例 2：
#
# 输入：nums = [1]
# 输出：1
#
#
# 示例 3：
#
# 输入：nums = [5,4,-1,7,8]
# 输出：23
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#
#
# 进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。
#
#

# @lcpr-template-start
import copy
import collections
from collections import namedtuple
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush


# @lcpr-template-end
# @lc code=start
class Solution:

    def dp(self, nums: List[int]) -> int:
        pre, max_ans = 0, nums[0]

        for num in nums:
            pre = max(pre + num, num)
            max_ans = max(max_ans, pre)

        return max_ans

    def divide_and_conquer(self, nums: List[int]) -> int:

        class Status:

            def __init__(self, lSum, rSum, iSum, mSum):
                self.lSum = lSum
                self.rSum = rSum
                self.iSum = iSum
                self.mSum = mSum

        def push_up(l: Status, r: Status) -> Status:
            iSum = l.iSum + r.iSum
            lSum = max(l.lSum, l.iSum + r.lSum)
            rSum = max(l.rSum + r.iSum, r.rSum)
            mSum = max(max(l.mSum, r.mSum), l.rSum + r.lSum)
            return Status(lSum, rSum, iSum, mSum)

        def get(nums: List[int], l: int, r: int) -> Status:
            if l == r:
                return Status(nums[l], nums[l], nums[l], nums[l])

            m = (l + r) >> 1
            lSub = get(nums, l, m)
            rSub = get(nums, m + 1, r)

            return push_up(lSub, rSub)

        return get(nums, 0, len(nums) - 1).mSum

    def maxSubArray(self, nums: List[int]) -> int:
        # return self.dp(nums)
        return self.divide_and_conquer(nums)


# @lc code=end

tests = [[-2, 1, -3, 4, -1, 2, 1, -5, 4], [1], [5, 4, -1, 7, 8]]
ans = [6, 1, 23]
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().maxSubArray(t)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# [-2,1,-3,4,-1,2,1,-5,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,-1,7,8]\n
# @lcpr case=end

#
