#
# @lc app=leetcode.cn id=438 lang=python3
# @lcpr version=30204
#
# [438] 找到字符串中所有字母异位词
#
# https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (53.38%)
# Likes:    1506
# Dislikes: 0
# Total Accepted:    506.8K
# Total Submissions: 948.1K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
#
# 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
#
#
#
# 示例 1:
#
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
#
#
# 示例 2:
#
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
#
#
#
#
# 提示:
#
#
# 1 <= s.length, p.length <= 3 * 10^4
# s 和 p 仅包含小写字母
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

    def use_slide_win(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)

        if s_len < p_len:
            return []

        ans = []
        s_count = [0] * 26
        p_count = [0] * 26

        for i in range(p_len):
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1

        if s_count == p_count:
            ans.append(0)

        for i in range(s_len - p_len):
            s_count[ord(s[i]) - 97] -= 1
            s_count[ord(s[i + p_len]) - 97] += 1

            if s_count == p_count:
                ans.append(i + 1)

        return ans

    def use_slide_win_optim(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)

        if s_len < p_len:
            return []

        ans = []
        count = [0] * 26

        for i in range(p_len):
            count[ord(s[i]) - 97] += 1
            count[ord(p[i]) - 97] -= 1

        differ = [c != 0 for c in count].count(True)

        if differ == 0:
            ans.append(0)

        for i in range(s_len - p_len):
            if count[ord(s[i]) - 97] == 1:
                differ -= 1
            elif count[ord(s[i]) - 97] == 0:
                differ += 1

            count[ord(s[i]) - 97] -= 1

            if count[ord(s[i + p_len]) - 97] == -1:
                differ -= 1
            elif count[ord(s[i + p_len]) - 97] == 0:
                differ += 1

            count[ord(s[i + p_len]) - 97] += 1

            if differ == 0:
                ans.append(i + 1)

        return ans

    def findAnagrams(self, s: str, p: str) -> List[int]:
        # return self.use_slide_win(s, p)
        return self.use_slide_win_optim(s, p)


# @lc code=end

#
# @lcpr case=start
# "cbaebabacd"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abab"\n"ab"\n
# @lcpr case=end

#
