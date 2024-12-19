#
# @lc app=leetcode.cn id=452 lang=python3
# @lcpr version=30204
#
# [452] 用最少数量的箭引爆气球
#
# https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/description/
#
# algorithms
# Medium (52.32%)
# Likes:    1041
# Dislikes: 0
# Total Accepted:    324.9K
# Total Submissions: 620.9K
# Testcase Example:  '[[10,16],[2,8],[1,6],[7,12]]'
#
# 有一些球形气球贴在一堵用 XY 平面表示的墙面上。墙面上的气球记录在整数数组 points ，其中points[i] = [xstart, xend]
# 表示水平直径在 xstart 和 xend之间的气球。你不知道气球的确切 y 坐标。
#
# 一支弓箭可以沿着 x 轴从不同点 完全垂直 地射出。在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足
# xstart ≤ x ≤ xend，则该气球会被 引爆 。可以射出的弓箭的数量 没有限制 。 弓箭一旦被射出之后，可以无限地前进。
#
# 给你一个数组 points ，返回引爆所有气球所必须射出的 最小 弓箭数 。
#
#
# 示例 1：
#
# 输入：points = [[10,16],[2,8],[1,6],[7,12]]
# 输出：2
# 解释：气球可以用2支箭来爆破:
# -在x = 6处射出箭，击破气球[2,8]和[1,6]。
# -在x = 11处发射箭，击破气球[10,16]和[7,12]。
#
# 示例 2：
#
# 输入：points = [[1,2],[3,4],[5,6],[7,8]]
# 输出：4
# 解释：每个气球需要射出一支箭，总共需要4支箭。
#
# 示例 3：
#
# 输入：points = [[1,2],[2,3],[3,4],[4,5]]
# 输出：2
# 解释：气球可以用2支箭来爆破:
# - 在x = 2处发射箭，击破气球[1,2]和[2,3]。
# - 在x = 4处射出箭，击破气球[3,4]和[4,5]。
#
#
#
#
#
# 提示:
#
#
# 1 <= points.length <= 10^5
# points[i].length == 2
# -2^31 <= xstart < xend <= 2^31 - 1
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

    def copilot_solution(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        ans = 1
        pre = points[0]
        for i in range(1, len(points)):
            if points[i][0] > pre[1]:
                ans += 1
                pre = points[i]
        return ans

    def my_solution(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: p[1])
        ans = 0
        pre = -math.inf
        for start, end in points:
            if start > pre:
                ans += 1
                pre = end
        return ans

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # return self.copilot_solution(points)
        return self.my_solution(points)


# @lc code=end

tests = [
    [[10, 16], [2, 8], [1, 6], [7, 12]],
    [[1, 2], [3, 4], [5, 6], [7, 8]],
    [[1, 2], [2, 3], [3, 4], [4, 5]],
]
ans = [2, 4, 2]
all_pass = True
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().findMinArrowShots(t)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res};")
    all_pass &= (a == res)
print(f"all pass: {all_pass}.")

#
# @lcpr case=start
# [[10,16],[2,8],[1,6],[7,12]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[3,4],[5,6],[7,8]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[2,3],[3,4],[4,5]]\n
# @lcpr case=end

#
