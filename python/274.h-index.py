#
# @lc app=leetcode.cn id=274 lang=python3
# @lcpr version=30204
#
# [274] H 指数
#
# https://leetcode.cn/problems/h-index/description/
#
# algorithms
# Medium (46.22%)
# Likes:    530
# Dislikes: 0
# Total Accepted:    226.2K
# Total Submissions: 489.4K
# Testcase Example:  '[3,0,6,1,5]'
#
# 给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数。计算并返回该研究者的 h 指数。
#
# 根据维基百科上 h 指数的定义：h 代表“高引用次数” ，一名科研人员的 h 指数 是指他（她）至少发表了 h 篇论文，并且 至少 有 h
# 篇论文被引用次数大于等于 h 。如果 h 有多种可能的值，h 指数 是其中最大的那个。
#
#
#
# 示例 1：
#
# 输入：citations = [3,0,6,1,5]
# 输出：3
# 解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
# 由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3。
#
# 示例 2：
#
# 输入：citations = [1,3,1]
# 输出：1
#
#
#
#
# 提示：
#
#
# n == citations.length
# 1 <= n <= 5000
# 0 <= citations[i] <= 1000
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

    def use_count_sort(self, citations: List[int]) -> int:
        n = len(citations)
        total = 0
        count = [0] * (n + 1)
        for c in citations:
            if c >= n:
                count[n] += 1
            else:
                count[c] += 1

        for i in range(n, -1, -1):
            total += count[i]
            if total >= i:
                return i

        return 0

    def hIndex(self, citations: List[int]) -> int:
        return self.use_count_sort(citations)


# @lc code=end

#
# @lcpr case=start
# [3,0,6,1,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,1]\n
# @lcpr case=end

#
