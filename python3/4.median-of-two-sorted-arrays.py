#
# @lc app=leetcode.cn id=4 lang=python3
# @lcpr version=30204
#
# [4] 寻找两个正序数组的中位数
#
# https://leetcode.cn/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (42.24%)
# Likes:    7130
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 2.6M
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
#
# 算法的时间复杂度应该为 O(log (m+n)) 。
#
#
#
# 示例 1：
#
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
#
#
# 示例 2：
#
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
#
#
#
#
#
#
# 提示：
#
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
#
#
#

# @lcpr-template-start
import math
from operator import index
from turtle import left
from typing import List
from typing import Optional

from numpy import Infinity
from pyparsing import infix_notation


# @lcpr-template-end
# @lc code=start
class Solution:

    def normalSolution(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        lens = len1 + len2
        left, right = -1, -1
        start1, start2 = 0, 0
        for i in range(lens // 2 + 1):
            left = right
            if start1 < len1 and (start2 >= len2
                                  or nums1[start1] < nums2[start2]):
                right = nums1[start1]
                start1 += 1
            else:
                right = nums2[start2]
                start2 += 1

        if (lens & 1) == 0:
            return (left + right) / 2
        else:
            return right

    def getMedianFromKth(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)

        def getKthValue(k: int) -> float:
            index1, index2 = 0, 0
            while True:
                if index1 == len1:
                    return nums2[index2 + k - 1]
                if index2 == len2:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                pivotIndex1 = min(index1 + k // 2 - 1, len1 - 1)
                pivotIndex2 = min(index2 + k // 2 - 1, len2 - 1)
                pivot1, pivot2 = nums1[pivotIndex1], nums2[pivotIndex2]
                if pivot1 <= pivot2:
                    k -= pivotIndex1 - index1 + 1
                    index1 = pivotIndex1 + 1
                else:
                    k -= pivotIndex2 - index2 + 1
                    index2 = pivotIndex2 + 1

        lens = len1 + len2
        if (lens & 1) == 1:
            return getKthValue((lens + 1) // 2)
        else:
            return (getKthValue(lens // 2) + getKthValue(lens // 2 + 1)) / 2

    def divideArrays(
        self,
        nums1: List[int],
        nums2: List[int],
    ) -> float:
        if (len(nums1) > len(nums2)):
            return self.divideArrays(nums2, nums1)

        infinty = 2**40
        len1 = len(nums1)
        len2 = len(nums2)
        median1, median2 = 0, 0
        left, right = 0, len1

        while left <= right:
            i = (left + right) // 2
            j = (len1 + len2 + 1) // 2 - i

            num_left1 = -infinty if i == 0 else nums1[i - 1]
            num_left2 = -infinty if j == 0 else nums2[j - 1]

            num_right1 = infinty if i == len1 else nums1[i]
            num_right2 = infinty if j == len2 else nums2[j]

            if num_left1 <= num_right2:
                median1, median2 = max(num_left1,
                                       num_left2), min(num_right1, num_right2)
                left = i + 1
            else:
                right = i - 1

        if (len1 + len2) & 1:
            return median1
        else:
            return (median1 + median2) / 2

    def zero_xf3_double_point(self, nums1: List[int],
                              nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        len1, len2 = len(nums1), len(nums2)
        nums1 = [-math.inf] + nums1 + [math.inf]
        nums2 = [-math.inf] + nums2 + [math.inf]

        i, j = 0, (len1 + len2 + 1) // 2
        while True:
            if nums1[i] <= nums2[j + 1] and nums1[i + 1] > nums2[j]:
                max1 = max(nums1[i], nums2[j])
                min2 = min(nums1[i + 1], nums2[j + 1])
                return max1 if (len1 + len2) & 1 else (max1 + min2) / 2

            i += 1
            j -= 1

    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        # return self.normalSolution(nums1, nums2)
        # return self.getMedianFromKth(nums1, nums2)
        # return self.divideArrays(nums1, nums2)
        return self.zero_xf3_double_point(nums1, nums2)


# @lc code=end

tests = [[[], [1]], [[1, 3], [2]], [[1, 2], [3, 4]]]
for nums1, nums2 in tests:
    result = Solution().findMedianSortedArrays(nums1, nums2)
    print(f"test: {nums1}, {nums2}; result: {result}")

#
# @lcpr case=start
# [1,3]\n[2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[3,4]\n
# @lcpr case=end

#
