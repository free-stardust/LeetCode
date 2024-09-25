#
# @lc app=leetcode.cn id=228 lang=python3
# @lcpr version=30204
#
# [228] 汇总区间
#
# https://leetcode.cn/problems/summary-ranges/description/
#
# algorithms
# Easy (54.82%)
# Likes:    399
# Dislikes: 0
# Total Accepted:    183.2K
# Total Submissions: 334.2K
# Testcase Example:  '[0,1,2,4,5,7]'
#
# 给定一个  无重复元素 的 有序 整数数组 nums 。
#
# 返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表 。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于
# nums 的数字 x 。
#
# 列表中的每个区间范围 [a,b] 应该按如下格式输出：
#
#
# "a->b" ，如果 a != b
# "a" ，如果 a == b
#
#
#
#
# 示例 1：
#
# 输入：nums = [0,1,2,4,5,7]
# 输出：["0->2","4->5","7"]
# 解释：区间范围是：
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
#
#
# 示例 2：
#
# 输入：nums = [0,2,3,4,6,8,9]
# 输出：["0","2->4","6","8->9"]
# 解释：区间范围是：
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
#
#
#
#
# 提示：
#
#
# 0 <= nums.length <= 20
# -2^31 <= nums[i] <= 2^31 - 1
# nums 中的所有值都 互不相同
# nums 按升序排列
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

    def my_solution(self, nums: List[int]) -> List[str]:
        ans = []
        left, right = 0, 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                right += 1
            else:
                if left < right:
                    ans.append(f"{nums[left]}->{nums[right]}")
                else:
                    ans.append(f"{nums[left]}")
                left = right = i
        if left < right:
            ans.append(f"{nums[left]}->{nums[right]}")
        else:
            ans.append(f"{nums[left]}")
        return ans

    def zerox3f_solution(self, nums: List[int]) -> List[str]:
        ans = []
        i, nums_len = 0, len(nums)

        while i < nums_len:
            start = i
            while i < nums_len - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            scope = str(nums[start])
            if start < i:
                scope += "->" + str(nums[i])
            ans.append(scope)
            i += 1

        return ans

    def summaryRanges(self, nums: List[int]) -> List[str]:
        # return self.my_solution(nums)
        return self.zerox3f_solution(nums)


# @lc code=end

#
# @lcpr case=start
# [0,1,2,4,5,7]\n
# @lcpr case=end

# @lcpr case=start
# [0,2,3,4,6,8,9]\n
# @lcpr case=end

#
