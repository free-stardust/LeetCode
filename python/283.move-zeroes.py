#
# @lc app=leetcode.cn id=283 lang=python3
# @lcpr version=30204
#
# [283] 移动零
#
# https://leetcode.cn/problems/move-zeroes/description/
#
# algorithms
# Easy (63.65%)
# Likes:    2446
# Dislikes: 0
# Total Accepted:    1.5M
# Total Submissions: 2.4M
# Testcase Example:  '[0,1,0,3,12]'
#
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。
#
#
#
# 示例 1:
#
# 输入: nums = [0,1,0,3,12]
# 输出: [1,3,12,0,0]
#
#
# 示例 2:
#
# 输入: nums = [0]
# 输出: [0]
#
#
#
# 提示:
#
#
#
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1
#
#
#
#
# 进阶：你能尽量减少完成的操作次数吗？
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

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = right = 0

        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1


# @lc code=end

tests = [[0, 1, 0, 3, 12], [0]]
ans = [[1, 3, 12, 0, 0], [0]]
all_pass = True
for i, (t, a) in enumerate(zip(tests, ans)):
    test_t = copy.deepcopy(t)
    Solution().moveZeroes(t)
    all_pass &= (a == t)
    print(f"test case {i+1}:\n"
          f"\ttest = {test_t};\n"
          f"\tans = {a};\n"
          f"\tres = {t};\n"
          f"\t{a == t};")
print(f"all pass: {all_pass}.")

#
# @lcpr case=start
# [0,1,0,3,12]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#
