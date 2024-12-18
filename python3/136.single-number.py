#
# @lc app=leetcode.cn id=136 lang=python3
# @lcpr version=30204
#
# [136] 只出现一次的数字
#
# https://leetcode.cn/problems/single-number/description/
#
# algorithms
# Easy (74.02%)
# Likes:    3199
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 1.5M
# Testcase Example:  '[2,2,1]'
#
# 给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
# 你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。
#
#
#
#
#
# 示例 1 ：
#
# 输入：nums = [2,2,1]
# 输出：1
#
#
# 示例 2 ：
#
# 输入：nums = [4,1,2,1,2]
# 输出：4
#
#
# 示例 3 ：
#
# 输入：nums = [1]
# 输出：1
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 3 * 10^4
# -3 * 10^4 <= nums[i] <= 3 * 10^4
# 除了某个元素只出现一次以外，其余每个元素均出现两次。
#
#
#
#
#

# @lcpr-template-start
import copy
import collections
from functools import reduce
import random
import math
from collections import namedtuple
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush


# @lcpr-template-end
# @lc code=start
class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


# @lc code=end

tests = [[2, 2, 1], [4, 1, 2, 1, 2], [1]]
ans = [1, 4, 1]
all_pass = True
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().singleNumber(t)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res};")
    all_pass &= a == res
print(f"all pass: {all_pass}.")

#
# @lcpr case=start
# [2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,1,2,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#
