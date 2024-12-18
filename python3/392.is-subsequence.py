#
# @lc app=leetcode.cn id=392 lang=python3
# @lcpr version=30204
#
# [392] 判断子序列
#
# https://leetcode.cn/problems/is-subsequence/description/
#
# algorithms
# Easy (52.66%)
# Likes:    1091
# Dislikes: 0
# Total Accepted:    486.7K
# Total Submissions: 924.2K
# Testcase Example:  '"abc"\n"ahbgdc"'
#
# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
#
#
# 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
#
# 进阶：
#
# 如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T
# 的子序列。在这种情况下，你会怎样改变代码？
#
# 致谢：
#
# 特别感谢 @pbrother 添加此问题并且创建所有测试用例。
#
#
#
# 示例 1：
#
# 输入：s = "abc", t = "ahbgdc"
# 输出：true
#
#
# 示例 2：
#
# 输入：s = "axc", t = "ahbgdc"
# 输出：false
#
#
#
#
# 提示：
#
#
# 0 <= s.length <= 100
# 0 <= t.length <= 10^4
# 两个字符串都只由小写字符组成。
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

    def my_solution(self, s: str, t: str) -> bool:
        s_len, t_len = len(s), len(t)

        if s_len > t_len:
            return False

        ans = True
        i = 0

        for c in s:
            while i < t_len and c != t[i]:
                i += 1
            if i < t_len:
                i += 1
            else:
                return False

        return ans

    def use_double_pion(self, s: str, t: str) -> bool:
        s_len, t_len = len(s), len(t)
        i, j = 0, 0

        while i < s_len and j < t_len:
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == s_len

    def isSubsequence(self, s: str, t: str) -> bool:
        # return self.my_solution(s, t)
        return self.use_double_pion(s, t)


# @lc code=end

#
# @lcpr case=start
# "abc"\n"ahbgdc"\n
# @lcpr case=end

# @lcpr case=start
# "axc"\n"ahbgdc"\n
# @lcpr case=end

# @lcpr case=start
# "bb"\n"ahbgdc"\n
# @lcpr case=end

#
