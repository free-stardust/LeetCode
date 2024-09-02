#
# @lc app=leetcode.cn id=139 lang=python3
# @lcpr version=30204
#
# [139] 单词拆分
#
# https://leetcode.cn/problems/word-break/description/
#
# algorithms
# Medium (56.04%)
# Likes:    2568
# Dislikes: 0
# Total Accepted:    640.8K
# Total Submissions: 1.1M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。
#
# 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
#
#
#
# 示例 1：
#
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
#
#
# 示例 2：
#
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
# 注意，你可以重复使用字典中的单词。
#
#
# 示例 3：
#
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s 和 wordDict[i] 仅由小写英文字母组成
# wordDict 中的所有字符串 互不相同
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

    def solution1(self, s: str, wordDict: List[str]) -> bool:
        s_len = len(s)
        dp = [True] + [False] * s_len
        for i in range(s_len):
            for j in range(i + 1, s_len + 1):
                if dp[i] and (s[i:j] in wordDict):
                    dp[j] = True
        return dp[-1]

    def solution2(self, s: str, wordDict: List[str]) -> bool:
        s_len = len(s)
        dp = [True] + [False] * s_len
        for i in range(1, s_len + 1):
            for j in range(i):
                if dp[j] and (s[j:i] in wordDict):
                    dp[i] = True
                    break
        return dp[-1]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # return self.solution1(s, wordDict)
        return self.solution2(s, wordDict)


# @lc code=end

#
# @lcpr case=start
# "leetcode"\n["leet", "code"]\n
# @lcpr case=end

# @lcpr case=start
# "applepenapple"\n["apple", "pen"]\n
# @lcpr case=end

# @lcpr case=start
# "catsandog"\n["cats", "dog", "sand", "and", "cat"]\n
# @lcpr case=end

#
