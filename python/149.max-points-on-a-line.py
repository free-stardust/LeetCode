#
# @lc app=leetcode.cn id=149 lang=python3
# @lcpr version=30204
#
# [149] 直线上最多的点数
#
# https://leetcode.cn/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (40.83%)
# Likes:    564
# Dislikes: 0
# Total Accepted:    98.8K
# Total Submissions: 240.9K
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# 给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。
#
#
#
# 示例 1：
#
# 输入：points = [[1,1],[2,2],[3,3]]
# 输出：3
#
#
# 示例 2：
#
# 输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# 输出：4
#
#
#
#
# 提示：
#
#
# 1 <= points.length <= 300
# points[i].length == 2
# -10^4 <= xi, yi <= 10^4
# points 中的所有点 互不相同
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

    def maxPoints(self, points: List[List[int]]) -> int:

        def gcd(a: int, b: int) -> int:
            return gcd(b, a % b) if b else a

        len_points = len(points)
        if len_points <= 2:
            return len_points

        ans = 0

        for i in range(len_points):
            if ans > len_points - i or ans > len_points / 2:
                break

            mp = dict()
            for j in range(i + 1, len_points):
                x = points[i][0] - points[j][0]
                y = points[i][1] - points[j][1]

                if x == 0:
                    y = 1
                elif y == 0:
                    x = 1
                else:
                    if y < 0:
                        x, y = -x, -y
                    gcd_xy = gcd(abs(x), abs(y))
                    x /= gcd_xy
                    y /= gcd_xy

                mp[y + x * 20001] = mp.setdefault(y + x * 20001, 0) + 1

            max_count = 0
            for num in mp.values():
                max_count = max(max_count, num + 1)
            ans = max(max_count, ans)

        return ans


# @lc code=end

#
# @lcpr case=start
# [[1,1],[2,2],[3,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]\n
# @lcpr case=end

#
