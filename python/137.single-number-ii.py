#
# @lc app=leetcode.cn id=137 lang=python3
# @lcpr version=30204
#
# [137] 只出现一次的数字 II
#
# https://leetcode.cn/problems/single-number-ii/description/
#
# algorithms
# Medium (72.29%)
# Likes:    1236
# Dislikes: 0
# Total Accepted:    215.5K
# Total Submissions: 297.9K
# Testcase Example:  '[2,2,3,2]'
#
# 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
#
# 你必须设计并实现线性时间复杂度的算法且使用常数级空间来解决此问题。
#
#
#
# 示例 1：
#
# 输入：nums = [2,2,3,2]
# 输出：3
#
#
# 示例 2：
#
# 输入：nums = [0,1,0,1,0,1,99]
# 输出：99
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 3 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次
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

    def use_dict(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        print(freq)
        print(freq.items())
        ans = [num for num, occ in freq.items() if occ == 1][0]
        return ans

    def use_bin(self, nums: List[int]) -> int:
        ans = 0

        for i in range(32):
            total = sum((num >> i) & 1 for num in nums)
            if total % 3:
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)

        return ans

    def singleNumber(self, nums: List[int]) -> int:
        # return self.use_dict(nums)
        return self.use_bin(nums)


# @lc code=end

tests = [[2, 2, 3, 2], [0, 1, 0, 1, 0, 1, 99]]
ans = [3, 99]
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
# [2,2,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0,1,0,1,99]\n
# @lcpr case=end

#
