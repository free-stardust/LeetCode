#
# @lc app=leetcode.cn id=15 lang=python3
# @lcpr version=30204
#
# [15] 三数之和
#
# https://leetcode.cn/problems/3sum/description/
#
# algorithms
# Medium (38.22%)
# Likes:    6987
# Dislikes: 0
# Total Accepted:    1.9M
# Total Submissions: 5M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j !=
# k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#
#
#
#
# 示例 1：
#
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。
#
#
# 示例 2：
#
# 输入：nums = [0,1,1]
# 输出：[]
# 解释：唯一可能的三元组和不为 0 。
#
#
# 示例 3：
#
# 输入：nums = [0,0,0]
# 输出：[[0,0,0]]
# 解释：唯一可能的三元组和为 0 。
#
#
#
#
# 提示：
#
#
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
#
#
#

# @lcpr-template-start
from typing import List, Tuple
from typing import Optional


# @lcpr-template-end
# @lc code=start
class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums_len = len(nums)
        if not nums or nums_len < 3:
            return ans
        
        nums.sort()
        for i in range(nums_len):
            if nums[i] > 0: 
                return ans

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = nums_len - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1 
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1

        return ans


# @lc code=end

lists = [[-1, 0, 1, 2, -1, -4], [0, 1, 1], [0, 0, 0]]
ans = [[[-1, -1, 2], [-1, 0, 1]], [], [[0, 0, 0]]]

for l, a in zip(lists, ans):
    res = Solution().threeSum(l)
    print(f"l = {l}, ans = {a}, res = {res}.")

#
# @lcpr case=start
# [-1,0,1,2,-1,-4]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n
# @lcpr case=end

#
