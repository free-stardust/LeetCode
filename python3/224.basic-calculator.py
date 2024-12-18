#
# @lc app=leetcode.cn id=224 lang=python3
# @lcpr version=30204
#
# [224] 基本计算器
#
# https://leetcode.cn/problems/basic-calculator/description/
#
# algorithms
# Hard (42.98%)
# Likes:    1070
# Dislikes: 0
# Total Accepted:    157.1K
# Total Submissions: 365.5K
# Testcase Example:  '"1 + 1"'
#
# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
#
# 注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。
#
#
#
# 示例 1：
#
# 输入：s = "1 + 1"
# 输出：2
#
#
# 示例 2：
#
# 输入：s = " 2-1 + 2 "
# 输出：3
#
#
# 示例 3：
#
# 输入：s = "(1+(4+5+2)-3)+(6+8)"
# 输出：23
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 3 * 10^5
# s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
# s 表示一个有效的表达式
# '+' 不能用作一元运算(例如， "+1" 和 "+(2 + 3)" 无效)
# '-' 可以用作一元运算(即 "-1" 和 "-(2 + 3)" 是有效的)
# 输入中不存在两个连续的操作符
# 每个数字和运行的计算将适合于一个有符号的 32位 整数
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

    def use_double_stack(self, s: str) -> int:
        sign_stack, num_stack = [], [0]
        i, s_len, flag = 0, len(s), False

        while i < s_len:
            c = s[i]
            if c == "(":
                flag = True
                sign_stack.append(c)
            elif c in ["+", "-"]:
                if flag and c == "-":
                    num_stack.append(0)
                flag = False
                if sign_stack and sign_stack[-1] in ["+", "-"]:
                    sign = sign_stack.pop()
                    num2, num1 = num_stack.pop(), num_stack.pop()
                    res = num1 + num2 if sign == "+" else num1 - num2
                    num_stack.append(res)
                sign_stack.append(c)
            elif c == ")":
                flag = False
                while sign_stack[-1] != "(":
                    sign = sign_stack.pop()
                    num2, num1 = num_stack.pop(), num_stack.pop()
                    res = num1 + num2 if sign == "+" else num1 - num2
                    num_stack.append(res)
                sign_stack.pop()
            elif c.isdigit():
                flag = False
                num = 0
                while i < s_len and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                i -= 1
                num_stack.append(num)
            i += 1

        if sign_stack:
            sign = sign_stack.pop()
            num2, num1 = num_stack.pop(), num_stack.pop()
            num_stack.append(num1 + num2 if sign == "+" else num1 - num2)

        return num_stack.pop()

    def use_official(self, s: str) -> bool:
        # 该方案主要是利用了题中只有加减法， 所以进行了括号消除
        ops = [1]
        sign = 1

        ret = 0
        n = len(s)
        i = 0
        while i < n:
            if s[i] == ' ':
                pass
            elif s[i] == '+':
                sign = ops[-1]
            elif s[i] == '-':
                sign = -ops[-1]
            elif s[i] == '(':
                ops.append(sign)
            elif s[i] == ')':
                ops.pop()
            else:
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + ord(s[i]) - ord('0')
                    i += 1
                i -= 1
                ret += num * sign
            i += 1
            print(ops)
        return ret

    def calculate(self, s: str) -> int:
        # return self.use_double_stack(s)
        return self.use_official(s)


# @lc code=end

tests = ["1 + 1", " 2-1 + 2 ", "(1+(4+5+2)-3)+(6+8)", "1-(-2)", "-(3+4)+5"]
ans = [2, 3, 23, 3, -2]
all_pass = True
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().calculate(t)
    all_pass &= (a == res)
    print(f"test case {i+1}:\n"
          f"\ttest = \"{t}\";\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res};")
print(f"all pass: {all_pass}.")

#
# @lcpr case=start
# "1 + 1"\n
# @lcpr case=end

# @lcpr case=start
# " 2-1 + 2 "\n
# @lcpr case=end

# @lcpr case=start
# "(1+(4+5+2)-3)+(6+8)"\n
# @lcpr case=end

#
