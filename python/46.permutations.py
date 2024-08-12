#
# @lc app=leetcode.cn id=46 lang=python3
# @lcpr version=30204
#
# [46] 全排列
#
# https://leetcode.cn/problems/permutations/description/
#
# algorithms
# Medium (79.45%)
# Likes:    2942
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,3]'
#
# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 
# 
# 示例 2：
# 
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
# 
# 
# 示例 3：
# 
# 输入：nums = [1]
# 输出：[[1]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# nums 中的所有整数 互不相同
# 
# 
#


# @lcpr-template-start
import copy
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush
# @lcpr-template-end
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums_len = len(nums)

        def backtrack(first = 0):
            if first == nums_len:
                ans.append(nums[:])

            for i in range(first, nums_len):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        backtrack()

        return ans
# @lc code=end

tests = [[1,2,3], [0,1],[1]]
ans = [[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]], [[0,1],[1,0]], [[1]]]
for i,(t,a) in enumerate(zip(tests,ans)):
    res = Solution().permute(t)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

