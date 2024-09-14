#
# @lc app=leetcode.cn id=347 lang=python3
# @lcpr version=30204
#
# [347] 前 K 个高频元素
#
# https://leetcode.cn/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (63.86%)
# Likes:    1889
# Dislikes: 0
# Total Accepted:    604.3K
# Total Submissions: 944.1K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
#
#
#
# 示例 1:
#
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#
#
# 示例 2:
#
# 输入: nums = [1], k = 1
# 输出: [1]
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# k 的取值范围是 [1, 数组中不相同的元素的个数]
# 题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的
#
#
#
#
# 进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。
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
from heapq import heapify, heappop, heappush, heappushpop


# @lcpr-template-end
# @lc code=start
class Solution:

    def use_minheap(self, nums: List[int], k: int) -> List[int]:
        ans = []
        occur = collections.defaultdict(int)
        freq_heap = []

        for num in nums:
            occur[num] += 1

        for num, freq in occur.items():
            if len(freq_heap) < k:
                heappush(freq_heap, (freq, num))
            elif freq > freq_heap[0][0]:
                heappushpop(freq_heap, (freq, num))

        ans = [num for _, num in freq_heap]

        return ans

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.use_minheap(nums, k)


# @lc code=end

#
# @lcpr case=start
# [1,1,1,2,2,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#
