#
# @lc app=leetcode.cn id=76 lang=python3
# @lcpr version=30204
#
# [76] 最小覆盖子串
#
# https://leetcode.cn/problems/minimum-window-substring/description/
#
# algorithms
# Hard (46.02%)
# Likes:    2965
# Dislikes: 0
# Total Accepted:    617.6K
# Total Submissions: 1.3M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 ""
# 。
#
#
#
# 注意：
#
#
# 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
# 如果 s 中存在这样的子串，我们保证它是唯一的答案。
#
#
#
#
# 示例 1：
#
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
#
#
# 示例 2：
#
# 输入：s = "a", t = "a"
# 输出："a"
# 解释：整个字符串 s 是最小覆盖子串。
#
#
# 示例 3:
#
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。
#
#
#
# 提示：
#
#
# ^m == s.length
# ^n == t.length
# 1 <= m, n <= 10^5
# s 和 t 由英文字母组成
#
#
#
# 进阶：你能设计一个在 o(m+n) 时间内解决此问题的算法吗？
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

    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1

        need_cnt = len(t)
        i, res = 0, (0, float("inf"))

        for j, c in enumerate(s):
            if need[c] > 0:
                need_cnt -= 1
            need[c] -= 1
            if need_cnt == 0:
                while True:
                    c = s[i]
                    if need[c] == 0:
                        break
                    need[c] += 1
                    i += 1
                if j - i < res[1] - res[0]:
                    res = (i, j)
                need[s[i]] += 1
                need_cnt += 1
                i += 1

        return "" if res[1] > len(s) else s[res[0]:res[1] + 1]


# @lc code=end

tests = [["ADOBECODEBANC", "ABC"], ["a", "a"], ["a", "aa"]]
ans = ["BANC", "a", ""]
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().minWindow(t[0], t[1])
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = \"{a}\";\n"
          f"\tres = \"{res}\";\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# "ADOBECODEBANC"\n"ABC"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"aa"\n
# @lcpr case=end

#
