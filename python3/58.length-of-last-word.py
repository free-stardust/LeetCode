#
# @lc app=leetcode.cn id=58 lang=python3
# @lcpr version=30204
#
# [58] 最后一个单词的长度
#
# https://leetcode.cn/problems/length-of-last-word/description/
#
# algorithms
# Easy (46.21%)
# Likes:    717
# Dislikes: 0
# Total Accepted:    604.9K
# Total Submissions: 1.3M
# Testcase Example:  '"Hello World"'
#
# 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。
#
# 单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
#
#
#
# 示例 1：
#
# 输入：s = "Hello World"
# 输出：5
# 解释：最后一个单词是“World”，长度为 5。
#
#
# 示例 2：
#
# 输入：s = "   fly me   to   the moon  "
# 输出：4
# 解释：最后一个单词是“moon”，长度为 4。
#
#
# 示例 3：
#
# 输入：s = "luffy is still joyboy"
# 输出：6
# 解释：最后一个单词是长度为 6 的“joyboy”。
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 10^4
# s 仅有英文字母和空格 ' ' 组成
# s 中至少存在一个单词
#
#
#

# @lcpr-template-start
import copy
import collections
import random
from collections import namedtuple
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush


# @lcpr-template-end
# @lc code=start
class Solution:
    def use_strip(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])
    
    def traverse_from_left(self, s: str) -> int:
        ans = 0
        
        for i in range(len(s)):
            if s[i] == " ":
                continue
            else:
                if i > 0 and s[i-1] == " ":
                    ans = 1
                else:
                    ans += 1

        return ans
    
    def traverse_from_right(self, s: str) -> int:
        ans = 0

        index = len(s) - 1
        while s[index] == " ":
            index -= 1
        
        while index >= 0 and s[index] != " ":
            ans += 1
            index -= 1

        return ans


    def lengthOfLastWord(self, s: str) -> int:
        # return self.use_strip(s)
        # return self.traverse_from_left(s)
        return self.traverse_from_right(s)


# @lc code=end

tests = ["Hello World", "   fly me   to   the moon  ", "luffy is still joyboy"]
ans = [5, 4, 6]
for i,(t,a) in enumerate(zip(tests, ans)):
    res = Solution().lengthOfLastWord(t)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# "Hello World"\n
# @lcpr case=end

# @lcpr case=start
# "   fly me   to   the moon  "\n
# @lcpr case=end

# @lcpr case=start
# "luffy is still joyboy"\n
# @lcpr case=end

#
