#
# @lc app=leetcode.cn id=32 lang=python3
# @lcpr version=30204
#
# [32] 最长有效括号
#
# https://leetcode.cn/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (38.25%)
# Likes:    2541
# Dislikes: 0
# Total Accepted:    470.1K
# Total Submissions: 1.2M
# Testcase Example:  '"(()"'
#
# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
#
#
#
#
#
# 示例 1：
#
# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"
#
#
# 示例 2：
#
# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"
#
#
# 示例 3：
#
# 输入：s = ""
# 输出：0
#
#
#
#
# 提示：
#
#
# 0 <= s.length <= 3 * 10^4
# s[i] 为 '(' 或 ')'
#
#
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

    def dp1(self, s: str) -> int:
        s_len = len(s)
        if s_len < 2:
            return 0

        dp = [0] * s_len
        max_len = 0
        for i in range(1, s_len):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = 2
                    if i - 2 >= 0:
                        dp[i] = dp[i] + dp[i - 2]
                else:
                    if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                        dp[i] = dp[i - 1] + 2
                        if i - dp[i - 1] - 2 >= 0:
                            dp[i] = dp[i] + dp[i - dp[i - 1] - 2]

            max_len = max(max_len, dp[i])

        return max_len

    def stack1(self, s: str) -> int:
        s_len = len(s)
        if s_len < 2:
            return 0

        stack = []
        match_list = [0] * s_len
        max_len = 0

        for i in range(s_len):
            if s[i] == "(":
                stack.append(i)
            else:
                if len(stack) > 0:
                    j = stack.pop()
                    if s[j] == "(":
                        match_list[i], match_list[j] = 1, 1

        tmp_len = 0
        for i in range(s_len):
            if match_list[i] == 1:
                tmp_len += 1
            else:
                max_len = tmp_len if tmp_len > max_len else max_len
                tmp_len = 0
        max_len = tmp_len if tmp_len > max_len else max_len

        return max_len

    def stack2(self, s: str) -> int:
        s_len = len(s)
        if len(s) < 2:
            return 0

        max_len = 0
        stack = []
        stack.append(-1)
        for i in range(s_len):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[len(stack) - 1])

        return max_len
    
    def noExtentSpace(self, s: str) -> int:
        s_len = len(s)
        if s_len < 2:
            return 0
        
        left, right, max_len = 0, 0, 0
        for i in range(s_len):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                max_len = max(max_len, left + right)
            elif left < right:
                left = right = 0
        
        left = right = 0
        for i in range(s_len-1, -1, -1):
            if s[i] == ")":
                right += 1
            else:
                left += 1
            if left == right:
                max_len = max(max_len, left + right)
            elif left > right:
                left = right = 0
        
        return max_len


    def longestValidParentheses(self, s: str) -> int:
        # return self.dp1(s)
        # return self.stack1(s)
        # return self.stack2(s)
        return self.noExtentSpace(s)


# @lc code=end

tests = ["(()", ")()())", "", "()(()", "((()))"]
ans = [2, 4, 0, 2, 6]
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().longestValidParentheses(t)
    print(f"test case {i+1}:\n"
          f"\ttest = \"{t}\";\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# "(()"\n
# @lcpr case=end

# @lcpr case=start
# ")()())"\n
# @lcpr case=end

# @lcpr case=start
# ""\n
# @lcpr case=end

#
