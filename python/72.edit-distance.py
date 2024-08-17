#
# @lc app=leetcode.cn id=72 lang=python3
# @lcpr version=30204
#
# [72] 编辑距离
#
# https://leetcode.cn/problems/edit-distance/description/
#
# algorithms
# Medium (62.98%)
# Likes:    3451
# Dislikes: 0
# Total Accepted:    522.2K
# Total Submissions: 828.7K
# Testcase Example:  '"horse"\n"ros"'
#
# 给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。
#
# 你可以对一个单词进行如下三种操作：
#
#
# 插入一个字符
# 删除一个字符
# 替换一个字符
#
#
#
#
# 示例 1：
#
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
#
#
# 示例 2：
#
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#
#
#
#
# 提示：
#
#
# 0 <= word1.length, word2.length <= 500
# word1 和 word2 由小写英文字母组成
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

    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)

        if len1 * len2 == 0:
            return len1 + len2

        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for i in range(len1 + 1):
            dp[i][0] = i

        for i in range(len2 + 1):
            dp[0][i] = i

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                left = dp[i - 1][j] + 1
                down = dp[i][j - 1] + 1
                left_down = dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    left_down += 1
                dp[i][j] = min(left, down, left_down)

        return dp[len1][len2]


# @lc code=end

tests = [["horse", "ros"], ["intention", "execution"]]
ans = [3, 5]
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().minDistance(t[0], t[1])
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# "horse"\n"ros"\n
# @lcpr case=end

# @lcpr case=start
# "intention"\n"execution"\n
# @lcpr case=end

#
