#
# @lc app=leetcode.cn id=122 lang=python3
# @lcpr version=30204
#
# [122] 买卖股票的最佳时机 II
#
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/description/
#
# algorithms
# Medium (73.95%)
# Likes:    2539
# Dislikes: 0
# Total Accepted:    1.2M
# Total Submissions: 1.6M
# Testcase Example:  '[7,1,5,3,6,4]'
#
# 给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。
#
# 在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。
#
# 返回 你能获得的 最大 利润 。
#
#
#
# 示例 1：
#
# 输入：prices = [7,1,5,3,6,4]
# 输出：7
# 解释：在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4。
# 随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6 - 3 = 3。
# 最大总利润为 4 + 3 = 7 。
#
# 示例 2：
#
# 输入：prices = [1,2,3,4,5]
# 输出：4
# 解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4。
# 最大总利润为 4 。
#
# 示例 3：
#
# 输入：prices = [7,6,4,3,1]
# 输出：0
# 解释：在这种情况下, 交易无法获得正利润，所以不参与交易可以获得最大利润，最大利润为 0。
#
#
#
# 提示：
#
#
# 1 <= prices.length <= 3 * 10^4
# 0 <= prices[i] <= 10^4
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

    def greedy(self, prices: List[int]) -> List[int]:
        max_profit = 0

        for i in range(1, len(prices)):
            max_profit += max(0, prices[i] - prices[i - 1])

        return max_profit

    def dp(self, prices: List[int]) -> int:
        dp0, dp1 = 0, -prices[0]

        for i in range(1, len(prices)):
            new_dp0 = max(dp0, dp1 + prices[i])
            new_dp1 = max(dp1, dp0 - prices[i])
            dp0, dp1 = new_dp0, new_dp1

        return dp0

    def maxProfit(self, prices: List[int]) -> int:
        # return self.greedy(prices)
        return self.dp(prices)


# @lc code=end

tests = [[7, 1, 5, 3, 6, 4], [1, 2, 3, 4, 5], [7, 6, 4, 3, 1]]
ans = [7, 4, 0]
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().maxProfit(t)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# [7,1,5,3,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

#
