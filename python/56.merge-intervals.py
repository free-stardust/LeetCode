#
# @lc app=leetcode.cn id=56 lang=python3
# @lcpr version=30204
#
# [56] 合并区间
#
# https://leetcode.cn/problems/merge-intervals/description/
#
# algorithms
# Medium (50.28%)
# Likes:    2398
# Dislikes: 0
# Total Accepted:    926.7K
# Total Submissions: 1.8M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi]
# 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
#
#
#
# 示例 1：
#
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#
#
# 示例 2：
#
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
#
#
#
# 提示：
#
#
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4
#
#
#

# @lcpr-template-start
import copy
import collections
import random
from collections import namedtuple
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush


# @lcpr-template-end
# @lc code=start
class Solution:

    def base_quicksort(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []

        def partition(left, right) -> int:
            p_i = random.randint(left, right)
            pivot = intervals[p_i]
            intervals[p_i], intervals[left] = intervals[left], intervals[p_i]

            while left < right:
                while left < right and intervals[right][0] >= pivot[0]:
                    right -= 1
                intervals[left] = intervals[right]
                while left < right and intervals[left][0] <= pivot[0]:
                    left += 1
                intervals[right] = intervals[left]

            intervals[left] = pivot

            return left

        def quick_sort(left, right):
            if left > right:
                return
            
            p_index = partition(left, right)
            quick_sort(left, p_index - 1)
            quick_sort(p_index + 1, right)

        quick_sort(0, len(intervals) - 1)

        ans = []

        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])

        return ans

    def base_sort(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = list()
        intervals.sort(key=lambda x: x[0])

        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])

        return ans

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # return self.base_sort(intervals)
        return self.base_quicksort(intervals)


# @lc code=end

tests = [[[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 4], [4, 5]]]
ans = [[[1, 6], [8, 10], [15, 18]], [[1, 5]]]

for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().merge(t)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# [[1,3],[2,6],[8,10],[15,18]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,4],[4,5]]\n
# @lcpr case=end

#
