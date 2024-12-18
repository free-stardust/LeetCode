#
# @lc app=leetcode.cn id=135 lang=python3
# @lcpr version=30204
#
# [135] 分发糖果
#
# https://leetcode.cn/problems/candy/description/
#
# algorithms
# Hard (48.81%)
# Likes:    1552
# Dislikes: 0
# Total Accepted:    345K
# Total Submissions: 707.5K
# Testcase Example:  '[1,0,2]'
#
# n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。
#
# 你需要按照以下要求，给这些孩子分发糖果：
#
#
# 每个孩子至少分配到 1 个糖果。
# 相邻两个孩子评分更高的孩子会获得更多的糖果。
#
#
# 请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。
#
#
#
# 示例 1：
#
# 输入：ratings = [1,0,2]
# 输出：5
# 解释：你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。
#
#
# 示例 2：
#
# 输入：ratings = [1,2,2]
# 输出：4
# 解释：你可以分别给第一个、第二个、第三个孩子分发 1、2、1 颗糖果。
# ⁠    第三个孩子只得到 1 颗糖果，这满足题面中的两个条件。
#
#
#
# 提示：
#
#
# n == ratings.length
# 1 <= n <= 2 * 10^4
# 0 <= ratings[i] <= 2 * 10^4
#
#
#

# @lcpr-template-start
import copy
import collections
import random
import math
from collections import namedtuple
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush


# @lcpr-template-end
# @lc code=start
class Solution:

    def solution1(self, ratings: List[int]) -> int:
        len_ratings = len(ratings)
        left = [0] * len_ratings

        for i in range(len_ratings):
            if i > 0 and ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1

        right = ret = 0

        for i in range(len_ratings - 1, -1, -1):
            if i < len_ratings - 1 and ratings[i] > ratings[i + 1]:
                right += 1
            else:
                right = 1
            ret += max(left[i], right)

        return ret

    def solution2(self, ratings: List[int]) -> int:
        len_ratings = len(ratings)
        ret = 1
        inc, dec, pre = 1, 0, 1

        for i in range(1, len_ratings):
            if ratings[i] >= ratings[i - 1]:
                dec = 0
                pre = 1 if ratings[i] == ratings[i - 1] else pre + 1
                ret += pre
                inc = pre
            else:
                dec += 1
                if dec == inc:
                    # 这里由于是严格小于，所以增长序列和递减序列长度相等时会导致递增序
                    # 列的最后一个加 1，这里加 1 实际上就是补这个缺漏，这样在是形式上
                    # 递减序列就变长了 1
                    dec += 1
                ret += dec
                pre = 1

        return ret

    def candy(self, ratings: List[int]) -> int:
        # return self.solution1(ratings)
        return self.solution2(ratings)


# @lc code=end

tests = [[1, 0, 2], [1, 2, 2]]
ans = [5, 4]
all_pass = True
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().candy(t)
    all_pass &= a == res
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res};")
print(f"all pass: {all_pass}.")

#
# @lcpr case=start
# [1,0,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2]\n
# @lcpr case=end

#
