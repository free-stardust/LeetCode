#
# @lc app=leetcode.cn id=290 lang=python3
# @lcpr version=30204
#
# [290] 单词规律
#
# https://leetcode.cn/problems/word-pattern/description/
#
# algorithms
# Easy (44.84%)
# Likes:    671
# Dislikes: 0
# Total Accepted:    202.9K
# Total Submissions: 452.5K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# 给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律。
#
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 s 中的每个非空单词之间存在着双向连接的对应规律。
#
#
#
# 示例1:
#
# 输入: pattern = "abba", s = "dog cat cat dog"
# 输出: true
#
# 示例 2:
#
# 输入:pattern = "abba", s = "dog cat cat fish"
# 输出: false
#
# 示例 3:
#
# 输入: pattern = "aaaa", s = "dog cat cat dog"
# 输出: false
#
#
#
# 提示:
#
#
# 1 <= pattern.length <= 300
# pattern 只包含小写英文字母
# 1 <= s.length <= 3000
# s 只包含小写英文字母和 ' '
# s 不包含 任何前导或尾随对空格
# s 中每个单词都被 单个空格 分隔
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

    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        match_dict = {}

        for p, word in zip(pattern, words):
            if p not in match_dict:
                if word not in match_dict.values():
                    match_dict[p] = word
                else:
                    return False
            elif match_dict[p] != word:
                return False

        return True


# @lc code=end

#
# @lcpr case=start
# "abba"\n"dog cat cat dog"\n
# @lcpr case=end

# @lcpr case=start
# "abba"\n"dog cat cat fish"\n
# @lcpr case=end

# @lcpr case=start
# "aaaa"\n"dog cat cat dog"\n
# @lcpr case=end

# @lcpr case=start
# "abba"\n"dog dog dog dog"\n
# @lcpr case=end

#
