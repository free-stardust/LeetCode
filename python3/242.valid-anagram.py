#
# @lc app=leetcode.cn id=242 lang=python3
# @lcpr version=30204
#
# [242] 有效的字母异位词
#
# https://leetcode.cn/problems/valid-anagram/description/
#
# algorithms
# Easy (66.96%)
# Likes:    950
# Dislikes: 0
# Total Accepted:    846.1K
# Total Submissions: 1.3M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的 字母异位词。
#
#
#
# 示例 1:
#
# 输入: s = "anagram", t = "nagaram"
# 输出: true
#
#
# 示例 2:
#
# 输入: s = "rat", t = "car"
# 输出: false
#
#
#
# 提示:
#
#
# 1 <= s.length, t.length <= 5 * 10^4
# s 和 t 仅包含小写字母
#
#
#
#
# 进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
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

    def use_sort(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

    def use_hash1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        table = [0] * 26

        for i in range(len(s)):
            table[ord(s[i]) - ord('a')] += 1

        for i in range(len(t)):
            table[ord(t[i]) - ord('a')] -= 1
            if table[ord(t[i]) - ord('a')] < 0:
                return False

        return True

    def use_hash2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        table = collections.defaultdict(int)

        for c in s:
            table[c] += 1

        for c in t:
            if c not in table:
                return False
            else:
                table[c] -= 1
                if table[c] < 0:
                    return False

        return True

    def isAnagram(self, s: str, t: str) -> bool:
        # return self.use_sort(s, t)
        # return self.use_hash1(s, t)
        return self.use_hash2(s, t)


# @lc code=end

s, t = "anagram", "nagaram"
res = Solution().isAnagram(s, t)
print(res)

#
# @lcpr case=start
# "anagram"\n"nagaram"\n
# @lcpr case=end

# @lcpr case=start
# "rat"\n"car"\n
# @lcpr case=end

#
