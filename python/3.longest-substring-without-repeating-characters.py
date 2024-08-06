#
# @lc app=leetcode.cn id=3 lang=python3
# @lcpr version=30204
#
# [3] 无重复字符的最长子串
#
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (39.79%)
# Likes:    10154
# Dislikes: 0
# Total Accepted:    2.9M
# Total Submissions: 7.2M
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
# 
# 
# 
# 示例 1:
# 
# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 
# 
# 示例 2:
# 
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 
# 
# 示例 3:
# 
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= s.length <= 5 * 10^4
# s 由英文字母、数字、符号和空格组成
# 
# 
#


# @lcpr-template-start
from typing import List
from typing import Optional
# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_s = ""
        max_len = 0
        for char in s:
            if char in sub_s:
                max_len = len(sub_s) if (len(sub_s) > max_len) else max_len
                sub_s = sub_s[sub_s.index(char) + 1:]
            sub_s += char
        
        if len(sub_s) > max_len:
            max_len = len(sub_s)

        return max_len
# @lc code=end

tests = ["aab", "abcabcbb", "bbbbb", "pwwkew", "a","aabaab!bb"]

for test in tests:
    result = Solution().lengthOfLongestSubstring(test)
    print(f"string = \"{test}\", result = {result}")

#
# @lcpr case=start
# "abcabcbb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#

