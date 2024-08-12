#
# @lc app=leetcode.cn id=49 lang=python3
# @lcpr version=30204
#
# [49] 字母异位词分组
#
# https://leetcode.cn/problems/group-anagrams/description/
#
# algorithms
# Medium (68.48%)
# Likes:    1961
# Dislikes: 0
# Total Accepted:    785.6K
# Total Submissions: 1.1M
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
# 
# 字母异位词 是由重新排列源单词的所有字母得到的一个新单词。
# 
# 
# 
# 示例 1:
# 
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
# 
# 示例 2:
# 
# 输入: strs = [""]
# 输出: [[""]]
# 
# 
# 示例 3:
# 
# 输入: strs = ["a"]
# 输出: [["a"]]
# 
# 
# 
# 提示：
# 
# 
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] 仅包含小写字母
# 
# 
#


# @lcpr-template-start
import copy
import collections
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush
# @lcpr-template-end
# @lc code=start
class Solution:
    def sort1(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            mp[key].append(s)
        
        return list(mp.values())
    
    def count1(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            mp[tuple(counts)].append(s)

        return list(mp.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # return self.sort1(strs)
        return self.count1(strs)
# @lc code=end

tests = [["eat", "tea", "tan", "ate", "nat", "bat"], [""], ["a"]]
ans = [[["bat"],["nat","tan"],["ate","eat","tea"]], [[""]], [["a"]]]
for i, (t,a) in enumerate(zip(tests,ans)):
    res = Solution().groupAnagrams(t)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# ["eat", "tea", "tan", "ate", "nat", "bat"]\n
# @lcpr case=end

# @lcpr case=start
# [""]\n
# @lcpr case=end

# @lcpr case=start
# ["a"]\n
# @lcpr case=end

#

