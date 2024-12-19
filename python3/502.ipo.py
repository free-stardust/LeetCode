#
# @lc app=leetcode.cn id=502 lang=python3
# @lcpr version=30204
#
# [502] IPO
#
# https://leetcode.cn/problems/ipo/description/
#
# algorithms
# Hard (45.99%)
# Likes:    335
# Dislikes: 0
# Total Accepted:    52.9K
# Total Submissions: 115.1K
# Testcase Example:  '2\n0\n[1,2,3]\n[0,1,1]'
#
# 假设 力扣（LeetCode）即将开始 IPO 。为了以更高的价格将股票卖给风险投资公司，力扣 希望在 IPO 之前开展一些项目以增加其资本。
# 由于资源有限，它只能在 IPO 之前完成最多 k 个不同的项目。帮助 力扣 设计完成最多 k 个不同项目后得到最大总资本的方式。
#
# 给你 n 个项目。对于每个项目 i ，它都有一个纯利润 profits[i] ，和启动该项目需要的最小资本 capital[i] 。
#
# 最初，你的资本为 w 。当你完成一个项目时，你将获得纯利润，且利润将被添加到你的总资本中。
#
# 总而言之，从给定项目中选择 最多 k 个不同项目的列表，以 最大化最终资本 ，并输出最终可获得的最多资本。
#
# 答案保证在 32 位有符号整数范围内。
#
#
#
# 示例 1：
#
# 输入：k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
# 输出：4
# 解释：
# 由于你的初始资本为 0，你仅可以从 0 号项目开始。
# 在完成后，你将获得 1 的利润，你的总资本将变为 1。
# 此时你可以选择开始 1 号或 2 号项目。
# 由于你最多可以选择两个项目，所以你需要完成 2 号项目以获得最大的资本。
# 因此，输出最后最大化的资本，为 0 + 1 + 3 = 4。
#
#
# 示例 2：
#
# 输入：k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
# 输出：6
#
#
#
#
# 提示：
#
#
# 1 <= k <= 10^5
# 0 <= w <= 10^9
# n == profits.length
# n == capital.length
# 1 <= n <= 10^5
# 0 <= profits[i] <= 10^4
# 0 <= capital[i] <= 10^9
#
#
#

# @lcpr-template-start
import copy
import collections
import heapq
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

    def copilot_solution(self, k: int, w: int, profits: List[int],
                         capital: List[int]) -> int:
        # use max heap and greedy algorithm
        n = len(profits)
        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort(key=lambda x: x[0])
        heap = []
        i = 0
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heappush(heap, -projects[i][1])
                i += 1
            if heap:
                w -= heappop(heap)
            else:
                break
        return w

    def max_head_solution(self, k: int, w: int, profits: List[int],
                          capital: List[int]) -> int:
        n = len(profits)
        # 将profits和capital组合起来，并按本金排序，这样保证我们总能选取所有小于等于当前资本的
        projects = sorted(zip(profits, capital), key=lambda x: x[1])
        cur = []
        idx = 0
        while k:
            # 将所有需要的本金小于等于当前资本的项目加入最大堆
            while idx < n and projects[idx][1] <= w:
                heapq.heappush(cur, -projects[idx][0])
                idx += 1
            # 如果有项目在当前的大顶堆中，我们做利益最大的那一个。
            if cur:
                w -= heapq.heappop(cur)
            else:
                break
            k -= 1
        return w

    def my_ex(self, k: int, w: int, profits: List[int],
              capital: List[int]) -> int:
        n = len(profits)
        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort(key=lambda x: x[0])
        heap = []
        i = 0
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heappush(heap, -projects[i][1])
                i += 1
            if heap:
                w -= heappop(heap)
            else:
                break
        return w

    def findMaximizedCapital(self, k: int, w: int, profits: List[int],
                             capital: List[int]) -> int:
        # return self.copilot_solution(k, w, profits, capital)
        # return self.max_head_solution(k, w, profits, capital)
        return self.my_ex(k, w, profits, capital)


# @lc code=end

tests = [
    [2, 0, [1, 2, 3], [0, 1, 1]],
    [3, 0, [1, 2, 3], [0, 1, 2]],
]
ans = [4, 6]
all_pass = True
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().findMaximizedCapital(t[0], t[1], t[2], t[3])
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res};")
    all_pass &= (a == res)
print(f"all pass: {all_pass}.")

#
# @lcpr case=start
# 2\n0\n[1,2,3]\n[0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# 3\n0\n[1,2,3]\n[0,1,2]\n
# @lcpr case=end

#
