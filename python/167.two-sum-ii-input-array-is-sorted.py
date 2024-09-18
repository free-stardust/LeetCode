#
# @lc app=leetcode.cn id=167 lang=python3
# @lcpr version=30204
#
# [167] 两数之和 II - 输入有序数组
#
# https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/description/
#
# algorithms
# Medium (60.25%)
# Likes:    1237
# Dislikes: 0
# Total Accepted:    733.6K
# Total Submissions: 1.2M
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给你一个下标从 1 开始的整数数组 numbers ，该数组已按 非递减顺序排列  ，请你从数组中找出满足相加之和等于目标数 target
# 的两个数。如果设这两个数分别是 numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <=
# numbers.length 。
#
# 以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。
#
# 你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。
#
# 你所设计的解决方案必须只使用常量级的额外空间。
#
#
# 示例 1：
#
# 输入：numbers = [2,7,11,15], target = 9
# 输出：[1,2]
# 解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。
#
# 示例 2：
#
# 输入：numbers = [2,3,4], target = 6
# 输出：[1,3]
# 解释：2 与 4 之和等于目标数 6 。因此 index1 = 1, index2 = 3 。返回 [1, 3] 。
#
# 示例 3：
#
# 输入：numbers = [-1,0], target = -1
# 输出：[1,2]
# 解释：-1 与 0 之和等于目标数 -1 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。
#
#
#
#
# 提示：
#
#
# 2 <= numbers.length <= 3 * 10^4
# -1000 <= numbers[i] <= 1000
# numbers 按 非递减顺序 排列
# -1000 <= target <= 1000
# 仅存在一个有效答案
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

    def use_double_point(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1

        return [-1, -1]

    def use_binary_search(self, numbers: List[int], target: int) -> List[int]:
        nums_len = len(numbers)

        for i in range(nums_len):
            left, right = i + 1, nums_len - 1
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == target - numbers[i]:
                    return [i + 1, mid + 1]
                elif numbers[mid] < target - numbers[i]:
                    left = mid + 1
                else:
                    right = mid - 1

        return [-1, -1]

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # return self.use_double_point(numbers, target)
        return self.use_binary_search(numbers, target)


# @lc code=end

#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [-1,0]\n-1\n
# @lcpr case=end

#
