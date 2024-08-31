#
# @lc app=leetcode.cn id=125 lang=python3
# @lcpr version=30204
#
# [125] 验证回文串
#
# https://leetcode.cn/problems/valid-palindrome/description/
#
# algorithms
# Easy (47.35%)
# Likes:    758
# Dislikes: 0
# Total Accepted:    634.1K
# Total Submissions: 1.3M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# 如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。
#
# 字母和数字都属于字母数字字符。
#
# 给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
# 输入: s = "A man, a plan, a canal: Panama"
# 输出：true
# 解释："amanaplanacanalpanama" 是回文串。
#
#
# 示例 2：
#
# 输入：s = "race a car"
# 输出：false
# 解释："raceacar" 不是回文串。
#
#
# 示例 3：
#
# 输入：s = " "
# 输出：true
# 解释：在移除非字母数字字符之后，s 是一个空字符串 "" 。
# 由于空字符串正着反着读都一样，所以是回文串。
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 2 * 10^5
# s 仅由可打印的 ASCII 字符组成
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

    def solution1(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]

    def solution2(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        s_len = len(sgood)
        left, right = 0, s_len - 1

        while left < right:
            if sgood[left] != sgood[right]:
                return False
            left, right = left + 1, right - 1

        return True

    def isPalindrome(self, s: str) -> bool:
        # return self.solution1(s)
        return self.solution2(s)


# @lc code=end

tests = ["A man, a plan, a canal: Panama", "race a car", " "]
ans = [True, False, True]
all_pass = True
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().isPalindrome(t)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res};")
    all_pass &= (a == res)
print(f"all pass: {all_pass}.")

#
# @lcpr case=start
# "A man, a plan, a canal: Panama"\n
# @lcpr case=end

# @lcpr case=start
# "race a car"\n
# @lcpr case=end

# @lcpr case=start
# " "\n
# @lcpr case=end

#
