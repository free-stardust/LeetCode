#
# @lc app=leetcode.cn id=151 lang=python3
# @lcpr version=30204
#
# [151] 反转字符串中的单词
#
# https://leetcode.cn/problems/reverse-words-in-a-string/description/
#
# algorithms
# Medium (56.07%)
# Likes:    1198
# Dislikes: 0
# Total Accepted:    626.1K
# Total Submissions: 1.1M
# Testcase Example:  '"the sky is blue"'
#
# 给你一个字符串 s ，请你反转字符串中 单词 的顺序。
#
# 单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。
#
# 返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。
#
# 注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。
#
#
#
# 示例 1：
#
# 输入：s = "the sky is blue"
# 输出："blue is sky the"
#
#
# 示例 2：
#
# 输入：s = "  hello world  "
# 输出："world hello"
# 解释：反转后的字符串中不能存在前导空格和尾随空格。
#
#
# 示例 3：
#
# 输入：s = "a good   example"
# 输出："example good a"
# 解释：如果两个单词间有多余的空格，反转后的字符串需要将单词间的空格减少到仅有一个。
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 10^4
# s 包含英文大小写字母、数字和空格 ' '
# s 中 至少存在一个 单词
#
#
#
#
#
#
#
# 进阶：如果字符串在你使用的编程语言中是一种可变数据类型，请尝试使用 O(1) 额外空间复杂度的 原地 解法。
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

    def use_api(self, s: str) -> str:
        return ' '.join(s.strip().split()[::-1])

    def double_piont(self, s: str) -> str:
        s = s.strip()
        i = j = len(s) - 1
        words = []

        while i >= 0:
            while i >= 0 and s[i] != " ":
                i -= 1

            words.append(s[i + 1:j + 1])

            while i >= 0 and s[i] == " ":
                i -= 1

            j = i

        return " ".join(words)

    def reverseWords(self, s: str) -> str:
        # return self.use_api(s)
        return self.double_piont(s)


# @lc code=end

#
# @lcpr case=start
# "the sky is blue"\n
# @lcpr case=end

# @lcpr case=start
# "  hello world  "\n
# @lcpr case=end

# @lcpr case=start
# "a good   example"\n
# @lcpr case=end

#
