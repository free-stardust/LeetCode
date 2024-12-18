#
# @lc app=leetcode.cn id=169 lang=python3
# @lcpr version=30204
#
# [169] 多数元素
#
# https://leetcode.cn/problems/majority-element/description/
#
# algorithms
# Easy (66.46%)
# Likes:    2275
# Dislikes: 0
# Total Accepted:    1M
# Total Submissions: 1.6M
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
#
#
# 示例 1：
#
# 输入：nums = [3,2,3]
# 输出：3
#
# 示例 2：
#
# 输入：nums = [2,2,1,1,1,2,2]
# 输出：2
#
#
#
# 提示：
#
#
# n == nums.length
# 1 <= n <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
#
#
#
#
# 进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
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

    def use_hash_map1(self, nums: List[int]) -> int:
        nums_len = len(nums)
        counts = collections.defaultdict(int)
        ans = nums[0]

        for num in nums:
            counts[num] += 1
            if counts[num] > nums_len // 2:
                ans = num
                break

        return ans

    def use_hash_map2(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

    def use_sort(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

    def use_random(self, nums: List[int]) -> int:
        majority = len(nums) // 2

        while True:
            candidate = random.choice(nums)
            if sum(1 for num in nums if num == candidate) > majority:
                return candidate

    def use_boyer_moore(self, nums: List[int]) -> int:
        count, candidate = 0, nums[0]

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate

    def divide_and_conquer(self, nums: List[int]) -> int:

        def get_sub_majority(left, right) -> int:
            if left == right:
                return nums[left]

            mid = (left + right) // 2
            left_maj = get_sub_majority(left, mid)
            right_maj = get_sub_majority(mid + 1, right)

            if left_maj == right_maj:
                return left_maj

            left_maj_count = sum(1 for i in range(left, right + 1)
                                 if nums[i] == left_maj)
            right_maj_count = sum(1 for i in range(left, right + 1)
                                  if nums[i] == right_maj)

            return left_maj if left_maj_count > right_maj_count else right_maj

        return get_sub_majority(0, len(nums) - 1)

    def majorityElement(self, nums: List[int]) -> int:
        # return self.use_hash_map1(nums)
        # return self.use_hash_map2(nums)
        # return self.use_sort(nums)
        # return self.use_random(nums)
        return self.use_boyer_moore(nums)
        # return self.divide_and_conquer(nums)


# @lc code=end

tests = [[3, 2, 3], [2, 2, 1, 1, 1, 2, 2]]
ans = [3, 2]
all_pass = True
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().majorityElement(t)
    all_pass &= (a == res)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res};")
print(f"all pass: {all_pass}.")
#
# @lcpr case=start
# [3,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,1,1,1,2,2]\n
# @lcpr case=end

#
