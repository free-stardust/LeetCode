#
# @lc app=leetcode.cn id=14 lang=python3
# @lcpr version=30204
#
# [14] 最长公共前缀
#
# https://leetcode.cn/problems/longest-common-prefix/description/
#
# algorithms
# Easy (44.21%)
# Likes:    3159
# Dislikes: 0
# Total Accepted:    1.4M
# Total Submissions: 3.1M
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 
# 
# 示例 1：
# 
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
# 
# 
# 示例 2：
# 
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。
# 
# 
# 
# 提示：
# 
# 
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] 仅由小写英文字母组成
# 
# 
#


# @lcpr-template-start
from typing import List, Tuple
from typing import Optional

from numpy import s_
from sympy import false
# @lcpr-template-end
# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(s) for s in strs)

        for i in range(min_len):
            s_tmp = strs[0][i]
            for j in range(1, len(strs)):
                if s_tmp != strs[j][i]:
                    return strs[0][:i]
            
        return strs[0][:min_len]
# @lc code=end

strs = [["flower","flow","flight"], ["dog","racecar","car"], ["a"]]
ans = ["fl", "", "a"]
for s,a in zip(strs, ans):
    res = Solution().longestCommonPrefix(s)
    print(f"s = {s}, ans = \"{a}\", res = \"{res}\", {a == res}.")

#
# @lcpr case=start
# ["flower","flow","flight"]\n
# @lcpr case=end

# @lcpr case=start
# ["dog","racecar","car"]\n
# @lcpr case=end

#

