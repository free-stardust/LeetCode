#
# @lc app=leetcode.cn id=57 lang=python3
# @lcpr version=30204
#
# [57] 插入区间
#
# https://leetcode.cn/problems/insert-interval/description/
#
# algorithms
# Medium (42.64%)
# Likes:    909
# Dislikes: 0
# Total Accepted:    222.8K
# Total Submissions: 522.6K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# 给你一个 无重叠的 ，按照区间起始端点排序的区间列表 intervals，其中 intervals[i] = [starti, endi] 表示第 i
# 个区间的开始和结束，并且 intervals 按照 starti 升序排列。同样给定一个区间 newInterval = [start, end]
# 表示另一个区间的开始和结束。
# 
# 在 intervals 中插入区间 newInterval，使得 intervals 依然按照 starti
# 升序排列，且区间之间不重叠（如果有必要的话，可以合并区间）。
# 
# 返回插入之后的 intervals。
# 
# 注意 你不需要原地修改 intervals。你可以创建一个新数组然后返回它。
# 
# 
# 
# 示例 1：
# 
# 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出：[[1,5],[6,9]]
# 
# 
# 示例 2：
# 
# 输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出：[[1,2],[3,10],[12,16]]
# 解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^5
# intervals 根据 starti 按 升序 排列
# newInterval.length == 2
# 0 <= start <= end <= 10^5
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
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = list()
        left, right = newInterval
        inserted = False

        for li, ri in intervals:
            if li > right:
                if not inserted:
                    ans.append([left, right])
                    inserted = True
                ans.append([li, ri])
            elif ri < left:
                ans.append([li, ri])
            else:
                left = min(left, li)
                right = max(right, ri)
        
        if not inserted:
            ans.append([left, right])

        return ans
# @lc code=end

tests = [[[[1,3],[6,9]],[2,5]], [[[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]]]
ans = [[[1,5],[6,9]], [[1,2],[3,10],[12,16]]]
for i,(t,a) in enumerate(zip(tests,ans)):
    res = Solution().insert(t[0], t[1])
    print(f"test case {i+1}:\n"
          f"\ttest = {t[0]}, {t[1]};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")


#
# @lcpr case=start
# [[1,3],[6,9]]\n[2,5]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[3,5],[6,7],[8,10],[12,16]]\n[4,8]\n
# @lcpr case=end

#

