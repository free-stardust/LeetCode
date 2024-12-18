#
# @lc app=leetcode.cn id=84 lang=python3
# @lcpr version=30204
#
# [84] 柱状图中最大的矩形
#
# https://leetcode.cn/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (46.03%)
# Likes:    2791
# Dislikes: 0
# Total Accepted:    447.9K
# Total Submissions: 969K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
#
#
#
# 示例 1:
#
#
#
# 输入：heights = [2,1,5,6,2,3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10
#
#
# 示例 2：
#
#
#
# 输入： heights = [2,4]
# 输出： 4
#
#
#
# 提示：
#
#
# 1 <= heights.length <=10^5
# 0 <= heights[i] <= 10^4
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

    def solution1(self, heights: List[int]) -> int:
        # 解法说明：
        # 该解法主要是利用单调栈寻找当前高度左右两端第一个比自己低的高度，只要在这个高度范围内，
        # 其面积就是当前柱子的高度乘以宽度，而宽度就是右索引减去左边索引减一，因为我们只需要中
        # 间的宽度，所以需要减一；
        # 这种情况之所以可以行得通，是因为其思想是以当前柱子为高，进行左右扩展，只要两边的柱子
        # 比自己高或者和自己等高，那么就可以构成矩形，所以寻找左右两边比自己低的第一个柱子，就
        # 刚好是以当前柱高构成矩形的极限，因此，探索左边索引，栈为空时赋值为-1，而探索右边，栈
        # 为空时赋值为序列长度，就是因为这俩是边界

        nums_len = len(heights)
        left, right = [0] * nums_len, [0] * nums_len

        mono_stack = list()
        for i in range(nums_len):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)

        mono_stack.clear()
        for i in range(nums_len - 1, -1, -1):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            right[i] = mono_stack[-1] if mono_stack else nums_len
            mono_stack.append(i)

        res = max(heights[i] * (right[i] - left[i] - 1)
                  for i in range(nums_len)) if nums_len > 0 else 0

        return res

    def solution2(self, heights: List[int]) -> int:
        # 解法说明：
        # 该解法主要是利用单调栈寻找当前高度左右两端第一个比自己低的高度，只要在这个高度范围内，
        # 其面积就是当前柱子的高度乘以宽度，而宽度就是右索引减去左边索引减一，因为我们只需要中
        # 间的宽度，所以需要减一；
        # 这种情况之所以可以行得通，是因为其思想是以当前柱子为高，进行左右扩展，只要两边的柱子
        # 比自己高或者和自己等高，那么就可以构成矩形，所以寻找左右两边比自己低的第一个柱子，就
        # 刚好是以当前柱高构成矩形的极限，因此，探索左边索引，栈为空时赋值为-1，而探索右边，栈
        # 为空时赋值为序列长度，就是因为这俩是边界
        # 相比解法一，这个解法进行了优化，其原理是由于正向遍历时，用的单调栈，导致栈弹出的情况
        # 就是当前位置的柱子比栈顶的柱子矮，而这个弹出只会弹出一次，所以如果这个被弹出，必然是
        # 遇到了栈顶索引位置处柱子右边第一个比它矮的柱子，故直接把当前索引赋值给右边索引即可

        nums_len = len(heights)
        left, right = [0] * nums_len, [nums_len] * nums_len

        mono_stack = list()
        for i in range(nums_len):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                right[mono_stack[-1]] = i
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)

        res = max(heights[i] * (right[i] - left[i] - 1)
                  for i in range(nums_len)) if nums_len > 0 else 0

        return res

    def largestRectangleArea(self, heights: List[int]) -> int:
        # return self.solution1(heights)
        return self.solution2(heights)


# @lc code=end

tests = [[2, 1, 5, 6, 2, 3], [2, 4], [2, 1, 2], [1, 3, 3, 1]]
ans = [10, 4, 3, 6]
all_pass = True
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().largestRectangleArea(t)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res};")
    all_pass &= (a == res)
print(f"all pass: {all_pass}.")

#
# @lcpr case=start
# [2,1,5,6,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,4]\n
# @lcpr case=end

#
