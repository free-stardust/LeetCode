#
# @lc app=leetcode.cn id=383 lang=python3
# @lcpr version=30204
#
# [383] 赎金信
#
# https://leetcode.cn/problems/ransom-note/description/
#
# algorithms
# Easy (65.48%)
# Likes:    915
# Dislikes: 0
# Total Accepted:    541.5K
# Total Submissions: 826.8K
# Testcase Example:  '"a"\n"b"'
#
# 给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
#
# 如果可以，返回 true ；否则返回 false 。
#
# magazine 中的每个字符只能在 ransomNote 中使用一次。
#
#
#
# 示例 1：
#
# 输入：ransomNote = "a", magazine = "b"
# 输出：false
#
#
# 示例 2：
#
# 输入：ransomNote = "aa", magazine = "ab"
# 输出：false
#
#
# 示例 3：
#
# 输入：ransomNote = "aa", magazine = "aab"
# 输出：true
#
#
#
#
# 提示：
#
#
# 1 <= ransomNote.length, magazine.length <= 10^5
# ransomNote 和 magazine 由小写英文字母组成
#
#
#

# @lcpr-template-start
import copy
import collections
import random
import math
from functools import reduce
from collections import namedtuple, Counter
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush


# @lcpr-template-end
# @lc code=start
class Solution:

    def my_solution(self, ransomNote: str, magazine: str) -> bool:
        ans = True
        m_dict = {}

        for c in magazine:
            if c not in m_dict:
                m_dict[c] = 0
            else:
                m_dict[c] += 1

        for c in ransomNote:
            if c in m_dict and m_dict[c] >= 0:
                m_dict[c] -= 1
            else:
                ans = False
                break

        return ans

    def use_counter(self, ransomNote: str, magazine: str) -> bool:
        return Counter(ransomNote) <= Counter(magazine)

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # return self.my_solution(ransomNote, magazine)
        return self.use_counter(ransomNote, magazine)


# @lc code=end

#
# @lcpr case=start
# "a"\n"b"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"ab"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"aab"\n
# @lcpr case=end

#
