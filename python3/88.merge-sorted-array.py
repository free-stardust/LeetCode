#
# @lc app=leetcode.cn id=88 lang=python3
# @lcpr version=30204
#
# [88] 合并两个有序数组
#
# https://leetcode.cn/problems/merge-sorted-array/description/
#
# algorithms
# Easy (53.89%)
# Likes:    2503
# Dislikes: 0
# Total Accepted:    1.4M
# Total Submissions: 2.5M
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
#
# 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
#
# 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m
# 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
#
#
#
# 示例 1：
#
# 输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# 输出：[1,2,2,3,5,6]
# 解释：需要合并 [1,2,3] 和 [2,5,6] 。
# 合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
#
#
# 示例 2：
#
# 输入：nums1 = [1], m = 1, nums2 = [], n = 0
# 输出：[1]
# 解释：需要合并 [1] 和 [] 。
# 合并结果是 [1] 。
#
#
# 示例 3：
#
# 输入：nums1 = [0], m = 0, nums2 = [1], n = 1
# 输出：[1]
# 解释：需要合并的数组是 [] 和 [1] 。
# 合并结果是 [1] 。
# 注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。
#
#
#
#
# 提示：
#
#
# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -10^9 <= nums1[i], nums2[j] <= 10^9
#
#
#
#
# 进阶：你可以设计实现一个时间复杂度为 O(m + n) 的算法解决此问题吗？
#
#

# @lcpr-template-start
import copy
import collections
import random
import math
from collections import namedtuple
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush


# @lcpr-template-end
# @lc code=start
class Solution:

    def use_sort(self, nums1: List[int], m: int, nums2: List[int],
                 n: int) -> None:

        nums1[m:] = nums2
        nums1.sort()

    def double_point(self, nums1: List[int], m: int, nums2: List[int],
                     n: int) -> None:

        res = []
        p1, p2 = 0, 0

        while p1 < m or p2 < n:
            if p1 == m:
                res.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                res.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
            else:
                res.append(nums2[p2])
                p2 += 1

        nums1[:] = res

    def reverse_double_point(self, nums1: List[int], m: int, nums2: List[int],
                             n: int) -> None:

        p1, p2 = m - 1, n - 1
        tail = m + n - 1

        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1

    def merge(self, nums1: List[int], m: int, nums2: List[int],
              n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # self.use_sort(nums1, m, nums2, n)
        # self.double_point(nums1, m, nums2, n)
        self.reverse_double_point(nums1, m, nums2, n)


# @lc code=end

tests = [[[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3], [[1], 1, [], 0],
         [[0], 0, [1], 1]]
ans = [[1, 2, 2, 3, 5, 6], [1], [1]]
for i, (t, a) in enumerate(zip(tests, ans)):
    tmp_t = t[0].copy()
    Solution().merge(t[0], t[1], t[2], t[3])
    print(f"test case {i+1}:\n"
          f"\ttest = {[tmp_t] + t[1:]};\n"
          f"\tans = {a};\n"
          f"\tres = {t[0]};\n"
          f"\t{a == t[0]}.")

#
# @lcpr case=start
# [1,2,3,0,0,0]\n3\n[2,5,6]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n[]\n0\n
# @lcpr case=end

# @lcpr case=start
# [0]\n0\n[1]\n1\n
# @lcpr case=end

#
