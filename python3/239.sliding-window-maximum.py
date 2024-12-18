#
# @lc app=leetcode.cn id=239 lang=python3
# @lcpr version=30204
#
# [239] 滑动窗口最大值
#
# https://leetcode.cn/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (48.99%)
# Likes:    2870
# Dislikes: 0
# Total Accepted:    680.6K
# Total Submissions: 1.4M
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k
# 个数字。滑动窗口每次只向右移动一位。
#
# 返回 滑动窗口中的最大值 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
#
#
# 示例 2：
#
# 输入：nums = [1], k = 1
# 输出：[1]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
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

    def use_heap(self, nums: List[int], k: int) -> List[int]:
        nums_len = len(nums)

        q = [(-nums[i], i) for i in range(k)]
        heapify(q)

        ans = [-q[0][0]]
        for i in range(k, nums_len):
            heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heappop(q)
            ans.append(-q[0][0])

        return ans

    def use_deque(self, nums: List[int], k: int) -> List[int]:
        nums_len = len(nums)
        q = collections.deque()

        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        ans = [nums[q[0]]]

        for i in range(k, nums_len):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])

        return ans

    def use_prefix_sufix(self, nums: List[int], k: int) -> List[int]:
        nums_len = len(nums)
        prefix_max, suffix_max = [0] * nums_len, [0] * nums_len

        for i in range(nums_len):
            if i % k == 0:
                prefix_max[i] = nums[i]
            else:
                prefix_max[i] = max(prefix_max[i - 1], nums[i])

        for i in range(nums_len - 1, -1, -1):
            if i == nums_len - 1 or (i + 1) % k == 0:
                suffix_max[i] = nums[i]
            else:
                suffix_max[i] = max(suffix_max[i + 1], nums[i])

        ans = [
            max(suffix_max[i], prefix_max[i + k - 1])
            for i in range(nums_len - k + 1)
        ]

        return ans

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # return self.use_heap(nums, k)
        # return self.use_deque(nums, k)
        return self.use_prefix_sufix(nums, k)


# @lc code=end

#
# @lcpr case=start
# [1,3,-1,-3,5,3,6,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#
