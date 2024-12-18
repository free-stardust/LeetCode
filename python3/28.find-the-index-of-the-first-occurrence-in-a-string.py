#
# @lc app=leetcode.cn id=28 lang=python3
# @lcpr version=30204
#
# [28] 找出字符串中第一个匹配项的下标
#
# https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
#
# algorithms
# Easy (43.97%)
# Likes:    2265
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 2.5M
# Testcase Example:  '"sadbutsad"\n"sad"'
#
# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0
# 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。
#
#
#
# 示例 1：
#
# 输入：haystack = "sadbutsad", needle = "sad"
# 输出：0
# 解释："sad" 在下标 0 和 6 处匹配。
# 第一个匹配项的下标是 0 ，所以返回 0 。
#
#
# 示例 2：
#
# 输入：haystack = "leetcode", needle = "leeto"
# 输出：-1
# 解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
#
#
#
#
# 提示：
#
#
# 1 <= haystack.length, needle.length <= 10^4
# haystack 和 needle 仅由小写英文字符组成
#
#
#

# @lcpr-template-start
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush


# @lcpr-template-end
# @lc code=start
class Solution:

    def normal(self, haystack: str, needle: str) -> int:
        i, j = 0, 0
        len1, len2 = len(haystack), len(needle)
        while i < len1:
            if j == len2 - 1 and haystack[i] == needle[j]:
                return i - j
            elif j < len2 - 1 and haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                i = i - j + 1
                j = 0
        return -1

    def kmp(self, haystack: str, needle: str) -> int:

        def build_next(patt) -> List[int]:
            next_patt = [0]
            prefix_len = 0
            i = 1
            while i < len(patt):
                if patt[prefix_len] == patt[i]:
                    prefix_len += 1
                    next_patt.append(prefix_len)
                    i += 1
                else:
                    if prefix_len == 0:
                        next_patt.append(0)
                        i += 1
                    else:
                        prefix_len = next_patt[prefix_len - 1]
            return next_patt

        next_patt = build_next(needle)
        i, j = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j > 0:
                j = next_patt[j - 1]
            else:
                i += 1
            if j == len(needle):
                return i - j
        return -1

    def strStr(self, haystack: str, needle: str) -> int:
        # return self.normal(haystack, needle)
        return self.kmp(haystack, needle)


# @lc code=end

tests = [["sadbutsad", "sad"], ["leetcode", "leeto"], ["mississippi", "issip"]]
ans = [0, -1, 4]

for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().strStr(t[0], t[1])
    print(f"test case {i+1}:\n"
          f"\ttest = {t[0]}, {t[1]};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# "sadbutsad"\n"sad"\n
# @lcpr case=end

# @lcpr case=start
# "leetcode"\n"leeto"\n
# @lcpr case=end

#
