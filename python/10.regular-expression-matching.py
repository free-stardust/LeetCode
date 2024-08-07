#
# @lc app=leetcode.cn id=10 lang=python3
# @lcpr version=30204
#
# [10] 正则表达式匹配
#
# https://leetcode.cn/problems/regular-expression-matching/description/
#
# algorithms
# Hard (30.71%)
# Likes:    3933
# Dislikes: 0
# Total Accepted:    428.3K
# Total Submissions: 1.4M
# Testcase Example:  '"aa"\n"a"'
#
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
#
#
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
#
#
# 所谓匹配，是要涵盖 整个 字符串 s 的，而不是部分字符串。
#
#
# 示例 1：
#
# 输入：s = "aa", p = "a"
# 输出：false
# 解释："a" 无法匹配 "aa" 整个字符串。
#
#
# 示例 2:
#
# 输入：s = "aa", p = "a*"
# 输出：true
# 解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
#
#
# 示例 3：
#
# 输入：s = "ab", p = ".*"
# 输出：true
# 解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 20
# 1 <= p.length <= 20
# s 只包含从 a-z 的小写字母。
# p 只包含从 a-z 的小写字母，以及字符 . 和 *。
# 保证每次出现字符 * 时，前面都匹配到有效的字符
#
#
#

# @lcpr-template-start
from typing import List, Tuple
from typing import Optional


# @lcpr-template-end
# @lc code=start
class Solution:

    def dynamicProgramming(self, s: str, p: str) -> bool:
        len1, len2 = len(s) + 1, len(p) + 1
        dp = [[False] * len2 for _ in range(len1)]
        dp[0][0] = True

        for j in range(2, len2, 2):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == "*"

        for i in range(1, len1):
            for j in range(1, len2):
                if p[j - 1] == "*":
                    if dp[i][j - 2]: dp[i][j] = True
                    elif dp[i - 1][j] and s[i - 1] == p[j - 2]: dp[i][j] = True
                    elif dp[i - 1][j] and p[j - 2] == ".": dp[i][j] = True
                else:
                    if dp[i - 1][j - 1] and s[i - 1] == p[j - 1]:
                        dp[i][j] = True
                    elif dp[i - 1][j - 1] and p[j - 1] == ".":
                        dp[i][j] = True
        return dp[-1][-1]

    def isMatch(self, s: str, p: str) -> bool:
        return self.dynamicProgramming(s, p)


# @lc code=end

tests = [["aa", "a"], ["aa", "a*"], ["ab", ".*"]]
for s, p in tests:
    ans = Solution().isMatch(s, p)
    print(f"s = \"{s}\", p = \"{p}\" ans = {ans}.")

#
# @lcpr case=start
# "aa"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"a*"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n".*"\n
# @lcpr case=end

#
