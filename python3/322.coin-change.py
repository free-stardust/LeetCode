#
# @lc app=leetcode.cn id=322 lang=python3
# @lcpr version=30204
#
# [322] 零钱兑换
#
# https://leetcode.cn/problems/coin-change/description/
#
# algorithms
# Medium (48.80%)
# Likes:    2887
# Dislikes: 0
# Total Accepted:    903.7K
# Total Submissions: 1.8M
# Testcase Example:  '[1,2,5]\n11'
#
# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
#
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
#
# 你可以认为每种硬币的数量是无限的。
#
#
#
# 示例 1：
#
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1
#
# 示例 2：
#
# 输入：coins = [2], amount = 3
# 输出：-1
#
# 示例 3：
#
# 输入：coins = [1], amount = 0
# 输出：0
#
#
#
#
# 提示：
#
#
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4
#
#
#

# @lcpr-template-start
import copy
import collections
import functools
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

    def use_dp(self, coins: List[int], amount: int) -> int:
        self.coins = coins

        @functools.lru_cache(amount)
        def dp(rem) -> int:
            if rem < 0: return -1
            if rem == 0: return 0

            min_i = int(1e9)
            for coin in self.coins:
                res = dp(rem - coin)
                if res >= 0 and res < min_i:
                    min_i = res + 1
            return min_i if min_i < int(1e9) else -1

        if amount < 1: return 0
        return dp(amount)

    def use_dp2(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        count = [0] * amount

        def dp(rem) -> int:
            if rem < 0: return -1
            if rem == 0: return 0
            if count[rem - 1] != 0: return count[rem - 1]
            min_i = int(1e9)
            for coin in self.coins:
                res = dp(rem - coin)
                if res >= 0 and res < min_i:
                    min_i = res + 1
            count[rem - 1] = min_i if min_i < int(1e9) else -1
            return count[rem - 1]

        if amount < 1: return 0
        return dp(amount)

    def use_dp(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[amount] if dp[amount] != math.inf else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        # return self.use_dp(coins, amount)
        # return self.use_dp2(coins, amount)
        return self.use_dp(coins, amount)


# @lc code=end

#
# @lcpr case=start
# [1, 2, 5]\n11\n
# @lcpr case=end

# @lcpr case=start
# [2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#
