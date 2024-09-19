#
# @lc app=leetcode.cn id=42 lang=python3
# @lcpr version=30204
#
# [42] 接雨水
#
# https://leetcode.cn/problems/trapping-rain-water/description/
#
# algorithms
# Hard (63.91%)
# Likes:    5254
# Dislikes: 0
# Total Accepted:    1M
# Total Submissions: 1.6M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 示例 1：
#
#
#
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
#
#
# 示例 2：
#
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#
#
#
#
# 提示：
#
#
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
#
#
#

# @lcpr-template-start
import copy
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush


# @lcpr-template-end
# @lc code=start
class Solution:

    def dp(self, height: List[int]) -> int:
        ans = 0
        h_len = len(height)
        left_max = [height[0]] + [0] * (h_len - 1)
        right_max = [0] * (h_len - 1) + [height[-1]]
        for i in range(1, h_len):
            if height[i] > left_max[i - 1]:
                left_max[i] = height[i]
            else:
                left_max[i] = left_max[i - 1]

        for i in range(h_len - 2, -1, -1):
            if height[i] > right_max[i + 1]:
                right_max[i] = height[i]
            else:
                right_max[i] = right_max[i + 1]

        for i in range(h_len):
            ans += min(left_max[i], right_max[i]) - height[i]

        return ans

    def use_stack(self, height: List[int]) -> int:
        ans = 0
        stack = list()

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                cur_width = i - left - 1
                cur_height = min(height[left], h) - height[top]
                ans += cur_width * cur_height
            stack.append(i)

        return ans

    def use_double_point(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < right_max:
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1

        return ans

    def trap(self, height: List[int]) -> int:
        # return self.dp(height)
        # return self.use_stack(height)
        return self.use_double_point(height)


# @lc code=end

tests = [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], [4, 2, 0, 3, 2, 5]]
ans = [6, 9]
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().trap(t)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,0,3,2,5]\n
# @lcpr case=end

#
