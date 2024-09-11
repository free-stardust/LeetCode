#
# @lc app=leetcode.cn id=131 lang=python3
# @lcpr version=30204
#
# [131] 分割回文串
#
# https://leetcode.cn/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (73.75%)
# Likes:    1842
# Dislikes: 0
# Total Accepted:    451K
# Total Submissions: 609.7K
# Testcase Example:  '"aab"'
#
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
#
#
#
# 示例 1：
#
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
#
#
# 示例 2：
#
# 输入：s = "a"
# 输出：[["a"]]
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 16
# s 仅由小写英文字母组成
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

    def solution1(self, s: str) -> List[List[str]]:
        s_len = len(s)
        f = [[True] * s_len for _ in range(s_len)]

        for i in range(s_len - 1, -1, -1):
            for j in range(i + 1, s_len):
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]

        ans = []
        sub_ans = []

        def dfs(index: int):
            if index == s_len:
                ans.append(sub_ans[:])
                return

            for j in range(index, s_len):
                if f[index][j]:
                    sub_ans.append(s[index:j + 1])
                    dfs(j + 1)
                    sub_ans.pop()

        dfs(0)

        return ans

    def partition(self, s: str) -> List[List[str]]:
        return self.solution1(s)


# @lc code=end

tests = ["aab", "a"]
ans = [[["a", "a", "b"], ["aa", "b"]], [["a"]]]
all_pass = True
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().partition(t)
    all_pass &= (a == res)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res};")
print(f"all pass: {all_pass}.")

#
# @lcpr case=start
# "aab"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n
# @lcpr case=end

#
