#
# @lc app=leetcode.cn id=5 lang=python3
# @lcpr version=30204
#
# [5] 最长回文子串
#
# https://leetcode.cn/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (38.34%)
# Likes:    7223
# Dislikes: 0
# Total Accepted:    1.7M
# Total Submissions: 4.5M
# Testcase Example:  '"babad"'
#
# 给你一个字符串 s，找到 s 中最长的 回文 子串。
#
#
#
# 示例 1：
#
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#
#
# 示例 2：
#
# 输入：s = "cbbd"
# 输出："bb"
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 1000
# s 仅由数字和英文字母组成
#
#
#

# @lcpr-template-start
from typing import List, Tuple
from typing import Optional


# @lcpr-template-end
# @lc code=start
class Solution:

    def dynamicPrograming(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        max_len = 1
        begin = 0
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for L in range(2, n + 1):
            for i in range(n):
                j = L + i - 1
                if j >= n:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i

        return s[begin:begin + max_len]

    def expandAroundCenter(self, s: str) -> str:

        def expandAroundCenter(self, s: str, left: int,
                               right: int) -> Tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = expandAroundCenter(s, i, i)
            left2, right2 = expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start:end + 1]

    def solution(self, s: str) -> str:
        s_len = len(s)
        if s_len < 2:
            return s

        begin, max_len = 0, 1
        dp = [[False] * s_len for _ in range(s_len)]
        for i in range(s_len):
            dp[i][i] = True

        for l in range(2, s_len + 1):
            for i in range(s_len):
                j = i + l - 1

                if j >= s_len:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i

        return s[begin:begin + max_len]

    def longestPalindrome(self, s: str) -> str:
        # return self.dynamicPrograming(s)
        # return self.expandAroundCenter(s)
        return self.solution(s)


# @lc code=end

strs = ["babad", "cbbd"]
for s in strs:
    result = Solution().longestPalindrome(s)
    print(f"s = \"{s}\", result = \"{result}\"")

#
# @lcpr case=start
# "babad"\n
# @lcpr case=end

# @lcpr case=start
# "cbbd"\n
# @lcpr case=end

#
