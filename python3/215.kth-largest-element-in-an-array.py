#
# @lc app=leetcode.cn id=215 lang=python3
# @lcpr version=30204
#
# [215] 数组中的第K个最大元素
#
# https://leetcode.cn/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (61.21%)
# Likes:    2541
# Dislikes: 0
# Total Accepted:    1.2M
# Total Submissions: 1.9M
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
#
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
#
#
#
# 示例 1:
#
# 输入: [3,2,1,5,6,4], k = 2
# 输出: 5
#
#
# 示例 2:
#
# 输入: [3,2,3,1,2,4,5,5,6], k = 4
# 输出: 4
#
#
#
# 提示：
#
#
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
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

    def use_bucket_sort(self, nums: List[int], k: int) -> int:
        bucket = [0] * 20001

        for i in range(len(nums)):
            bucket[nums[i] + 10000] += 1

        for i in range(20000, -1, -1):
            k = k - bucket[i]
            if k <= 0:
                return i - 10000

        return 0

    def use_quick_sort(self, nums: List[int], k: int) -> int:

        def queck_select(left: int, right: int, k: int) -> int:
            if left == right:
                return nums[k]

            partition, l, r = nums[left], left - 1, right + 1

            while l < r:
                l += 1
                while nums[l] < partition:
                    l += 1
                r -= 1
                while nums[r] > partition:
                    r -= 1
                if l < r:
                    nums[l], nums[r] = nums[r], nums[l]
            if k <= r:
                return queck_select(left, r, k)
            else:
                return queck_select(r + 1, right, k)

        nums_len = len(nums)
        return queck_select(0, nums_len - 1, nums_len - k)

    def use_heap_sort(self, nums: List[int], k: int) -> int:
        heap_size = len(nums)

        def max_heap(i: int, heap_size: int):
            l, r, largest = 2 * i + 1, 2 * i + 2, i
            if l < heap_size and nums[l] > nums[largest]:
                largest = l
            if r < heap_size and nums[r] > nums[largest]:
                largest = r
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                max_heap(largest, heap_size)

        def build_max_heap(heap_size):
            for i in range(heap_size // 2, -1, -1):
                max_heap(i, heap_size)

        build_max_heap(heap_size)
        for i in range(heap_size - 1, heap_size - k, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heap_size -= 1
            max_heap(0, heap_size)

        return nums[0]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return self.use_quick_sort(nums, k)
        # return self.use_bucket_sort(nums, k)
        return self.use_heap_sort(nums, k)


# @lc code=end

tests = [[[3, 2, 3, 1, 2, 4, 5, 5, 6], 4], [[3, 2, 1, 5, 6, 4], 2]]
ans = [4, 5]
all_pass = True
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().findKthLargest(t[0], t[1])
    all_pass &= (a == res)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res};")
print(f"all pass: {a == res}.")

#
# @lcpr case=start
# [3,2,1,5,6,4]\n2\n
# @lcpr case=end

# @lcpr case=start
# [3,2,3,1,2,4,5,5,6]\n4\n
# @lcpr case=end

#
