#
# @lc app=leetcode.cn id=918 lang=python3
# @lcpr version=30204
#
# [918] 环形子数组的最大和
#
# https://leetcode.cn/problems/maximum-sum-circular-subarray/description/
#
# algorithms
# Medium (43.63%)
# Likes:    767
# Dislikes: 0
# Total Accepted:    103.8K
# Total Submissions: 237.8K
# Testcase Example:  '[1,-2,3,-2]'
#
# 给定一个长度为 n 的环形整数数组 nums ，返回 nums 的非空 子数组 的最大可能和 。
#
# 环形数组 意味着数组的末端将会与开头相连呈环状。形式上， nums[i] 的下一个元素是 nums[(i + 1) % n] ， nums[i]
# 的前一个元素是 nums[(i - 1 + n) % n] 。
#
# 子数组 最多只能包含固定缓冲区 nums 中的每个元素一次。形式上，对于子数组 nums[i], nums[i + 1], ..., nums[j]
# ，不存在 i <= k1, k2 <= j 其中 k1 % n == k2 % n 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,-2,3,-2]
# 输出：3
# 解释：从子数组 [3] 得到最大和 3
#
#
# 示例 2：
#
# 输入：nums = [5,-3,5]
# 输出：10
# 解释：从子数组 [5,5] 得到最大和 5 + 5 = 10
#
#
# 示例 3：
#
# 输入：nums = [3,-2,2,-3]
# 输出：3
# 解释：从子数组 [3] 和 [3,-2,2] 都可以得到最大和 3
#
#
#
#
# 提示：
#
#
# n == nums.length
# 1 <= n <= 3 * 10^4
# -3 * 10^4 <= nums[i] <= 3 * 10^4​​​​​​​
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
        n = len(nums)
        ans = max(nums)

        for win in range(2, len(nums) + 1):
            tmp_sum = sum(nums[:win])
            ans = max(ans, tmp_sum)
            for i in range(win, n + win - 1):
                tmp_sum += nums[i % n] - nums[(i - win) % n]
                ans = max(ans, tmp_sum)

        return ans

    def solution2(self, nums: List[int]) -> int:
        max_s = -math.inf  # 最大子数组和，不能为空
        min_s = 0  # 最小子数组和，可以为空
        max_f = min_f = 0
        for x in nums:
            # 以 nums[i-1] 结尾的子数组选或不选（取 max）+ x = 以 x 结尾的最大子数组和
            max_f = max(max_f, 0) + x
            max_s = max(max_s, max_f)
            # 以 nums[i-1] 结尾的子数组选或不选（取 min）+ x = 以 x 结尾的最小子数组和
            min_f = min(min_f, 0) + x
            min_s = min(min_s, min_f)
        if sum(nums) == min_s:
            return max_s
        return max(max_s, sum(nums) - min_s)

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # return self.solution1(nums)
        return self.solution2(nums)


# @lc code=end

tests = [[1, -2, 3, -2], [5, -3, 5], [3, -2, 2, -3], [3, 1, 3, 2, 6]]
ans = [3, 10, 3, 15]
all_pass = True
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().maxSubarraySumCircular(t)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res};")
    all_pass &= a == res
print(f"all pass: {all_pass}.")

#
# @lcpr case=start
# [1,-2,3,-2]\n
# @lcpr case=end

# @lcpr case=start
# [5,-3,5]\n
# @lcpr case=end

# @lcpr case=start
# [3,-2,2,-3]\n
# @lcpr case=end

#
