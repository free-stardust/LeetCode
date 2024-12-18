#
# @lc app=leetcode.cn id=55 lang=python3
# @lcpr version=30204
#
# [55] 跳跃游戏
#
# https://leetcode.cn/problems/jump-game/description/
#
# algorithms
# Medium (43.37%)
# Likes:    2829
# Dislikes: 0
# Total Accepted:    1M
# Total Submissions: 2.4M
# Testcase Example:  '[2,3,1,1,4]'
#
# 给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 
# 判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
# 
# 
# 示例 2：
# 
# 输入：nums = [3,2,1,0,4]
# 输出：false
# 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 10^5
# 
# 
#


# @lcpr-template-start
import copy
import collections
from collections import namedtuple
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush
# @lcpr-template-end
# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_pos = 0
        nums_len = len(nums)        
        for i in range(nums_len - 1):
            if max_pos >= i:
                max_pos = max(max_pos, i + nums[i])
        return True if max_pos >= nums_len - 1 else False
# @lc code=end

tests = [[2,3,1,1,4], [3,2,1,0,4]]
ans = [True, False]

for i,(t,a) in enumerate(zip(tests,ans)):
    res = Solution().canJump(t)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1,0,4]\n
# @lcpr case=end

#

