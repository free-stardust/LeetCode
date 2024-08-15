#
# @lc app=leetcode.cn id=68 lang=python3
# @lcpr version=30204
#
# [68] 文本左右对齐
#
# https://leetcode.cn/problems/text-justification/description/
#
# algorithms
# Hard (54.45%)
# Likes:    432
# Dislikes: 0
# Total Accepted:    85.5K
# Total Submissions: 156.8K
# Testcase Example:  '["This", "is", "an", "example", "of", "text", "justification."]\n16'
#
# 给定一个单词数组 words 和一个长度 maxWidth ，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。
#
# 你应该使用 “贪心算法” 来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth
# 个字符。
#
# 要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
#
# 文本的最后一行应为左对齐，且单词之间不插入额外的空格。
#
# 注意:
#
#
# 单词是指由非空格字符组成的字符序列。
# 每个单词的长度大于 0，小于等于 maxWidth。
# 输入单词数组 words 至少包含一个单词。
#
#
#
#
# 示例 1:
#
# 输入: words = ["This", "is", "an", "example", "of", "text", "justification."],
# maxWidth = 16
# 输出:
# [
# "This    is    an",
# "example  of text",
# "justification.  "
# ]
#
#
# 示例 2:
#
# 输入:words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
# 输出:
# [
# "What   must   be",
# "acknowledgment  ",
# "shall be        "
# ]
# 解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
# 因为最后一行应为左对齐，而不是左右两端对齐。
# ⁠    第二行同样为左对齐，这是因为这行只包含一个单词。
#
#
# 示例 3:
#
# 输入:words =
# ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]，maxWidth
# = 20
# 输出:
# [
# "Science  is  what we",
# ⁠ "understand      well",
# "enough to explain to",
# "a  computer.  Art is",
# "everything  else  we",
# "do                  "
# ]
#
#
#
#
# 提示:
#
#
# 1 <= words.length <= 300
# 1 <= words[i].length <= 20
# words[i] 由小写英文字母和符号组成
# 1 <= maxWidth <= 100
# words[i].length <= maxWidth
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

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []

        def blank(count: int) -> str:
            return ' ' * count

        right, n = 0, len(words)

        while True:
            left = right
            sum_len = 0

            while right < n and sum_len + len(words[right]) + right - left <= maxWidth:
                sum_len += len(words[right])
                right += 1
            
            if right == n:
                s = " ".join(words[left:])
                ans.append(s + blank(maxWidth - len(s)))
                break

            num_words = right - left
            num_spaces = maxWidth - sum_len

            if num_words == 1:
                ans.append(words[left] + blank(num_spaces))
                continue

            avg_spaces = num_spaces // (num_words - 1)
            extra_spaces = num_spaces % (num_words - 1)
            s1 = blank(avg_spaces + 1).join(words[left: left + extra_spaces + 1])
            s2 = blank(avg_spaces).join(words[left + extra_spaces + 1:right])
            ans.append(s1 + blank(avg_spaces) + s2)

        return ans


# @lc code=end

test = [[["This", "is", "an", "example", "of", "text", "justification."], 16],
        [["What", "must", "be", "acknowledgment", "shall", "be"], 16],
        [[
            "Science", "is", "what", "we", "understand", "well", "enough",
            "to", "explain", "to", "a", "computer.", "Art", "is", "everything",
            "else", "we", "do"
        ], 20]]
ans = [["This    is    an", "example  of text", "justification.  "],
       ["What   must   be", "acknowledgment  ", "shall be        "],
       [
           "Science  is  what we", "understand      well",
           "enough to explain to", "a  computer.  Art is",
           "everything  else  we", "do                  "
       ]]

def print_str(strs: List[str]):
    for i in range(len(strs)):
        print("\t\t" + "\"" + strs[i] + "\"")

for i,(t,a) in enumerate(zip(test,ans)):
    res = Solution().fullJustify(t[0], t[1])
    print(f"test case {i+1}:\n"
        #   f"\ttest = {t[0]}, {t[1]};\n"
          f"\tans =")
    print_str(a)
    print(f"\tres =")
    print_str(res)
    print(f"\t{a == res}.")

#
# @lcpr case=start
# ["This", "is", "an", "example", "of", "text", "justification."]\n16\n
# @lcpr case=end

# @lcpr case=start
# ["What","must","be","acknowledgment","shall","be"]\n16\n
# @lcpr case=end

# @lcpr case=start
# ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we"\n20\n
# @lcpr case=end

#
