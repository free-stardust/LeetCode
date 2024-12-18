#
# @lc app=leetcode.cn id=394 lang=python3
# @lcpr version=30204
#
# [394] 字符串解码
#
# https://leetcode.cn/problems/decode-string/description/
#
# algorithms
# Medium (57.99%)
# Likes:    1833
# Dislikes: 0
# Total Accepted:    356.9K
# Total Submissions: 612.1K
# Testcase Example:  '"3[a]2[bc]"'
#
# 给定一个经过编码的字符串，返回它解码后的字符串。
#
# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
#
# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
#
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
#
#
#
# 示例 1：
#
# 输入：s = "3[a]2[bc]"
# 输出："aaabcbc"
#
#
# 示例 2：
#
# 输入：s = "3[a2[c]]"
# 输出："accaccacc"
#
#
# 示例 3：
#
# 输入：s = "2[abc]3[cd]ef"
# 输出："abcabccdcdcdef"
#
#
# 示例 4：
#
# 输入：s = "abc3[cd]xyz"
# 输出："abccdcdcdxyz"
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 30
# s 由小写英文字母、数字和方括号 '[]' 组成
# s 保证是一个 有效 的输入。
# s 中所有整数的取值范围为 [1, 300]
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

    def use_stack(self, s: str) -> str:
        stack, res, multi = [], "", 0

        for ch in s:
            if ch == "[":
                stack.append([res, multi])
                res, multi = "", 0
            elif ch == "]":
                pre_res, cur_multi = stack.pop()
                res = pre_res + cur_multi * res
            elif "0" <= ch <= "9":
                multi = 10 * multi + int(ch)
            else:
                res += ch

        return res

    def use_recursion(self, s: str) -> str:

        def dfs(s, i):
            res, multi = "", 0
            while i < len(s):
                if "0" <= s[i] <= "9":
                    multi = 10 * multi + int(s[i])
                elif s[i] == "[":
                    i, tmp_res = dfs(s, i + 1)
                    res += multi * tmp_res
                    multi = 0
                elif s[i] == "]":
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res

        return dfs(s, 0)

    def decodeString(self, s: str) -> str:
        # return self.use_stack(s)
        return self.use_recursion(s)


# @lc code=end

#
# @lcpr case=start
# "3[a]2[bc]"\n
# @lcpr case=end

# @lcpr case=start
# "3[a2[c]]"\n
# @lcpr case=end

# @lcpr case=start
# "2[abc]3[cd]ef"\n
# @lcpr case=end

# @lcpr case=start
# "abc3[cd]xyz"\n
# @lcpr case=end

#
