#
# @lc app=leetcode.cn id=20 lang=python3
# @lcpr version=30204
#
# [20] 有效的括号
#
# https://leetcode.cn/problems/valid-parentheses/description/
#
# algorithms
# Easy (44.08%)
# Likes:    4509
# Dislikes: 0
# Total Accepted:    1.9M
# Total Submissions: 4.3M
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。
# 
# 
# 
# 
# 示例 1：
# 
# 输入：s = "()"
# 输出：true
# 
# 
# 示例 2：
# 
# 输入：s = "()[]{}"
# 输出：true
# 
# 
# 示例 3：
# 
# 输入：s = "(]"
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^4
# s 仅由括号 '()[]{}' 组成
# 
# 
#


# @lcpr-template-start
from typing import List, Tuple
from typing import Optional
# @lcpr-template-end
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(',']':'[','}':'{'}
        stack = []
        for i in s:
            if stack and i in dic:
                if stack[-1] == dic[i]: 
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(i)
        return not stack
# @lc code=end

tests = ["()", "()[]{}", "(]"]
ans = [True, True, False]
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().isValid(t)
    print(f"test case {i + 1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")


#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

#

