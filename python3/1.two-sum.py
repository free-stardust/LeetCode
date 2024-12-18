#
# @lc app=leetcode.cn id=1 lang=python3
# @lcpr version=30204
#
# [1] 两数之和
#
# https://leetcode.cn/problems/two-sum/description/
#
# algorithms
# Easy (53.68%)
# Likes:    18556
# Dislikes: 0
# Total Accepted:    5.4M
# Total Submissions: 10.1M
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
#
# 你可以按任意顺序返回答案。
#
#
#
# 示例 1：
#
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
#
#
# 示例 2：
#
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
#
#
# 示例 3：
#
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
#
#
#
#
# 提示：
#
#
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# 只会存在一个有效答案
#
#
#
#
# 进阶：你可以想出一个时间复杂度小于 O(n^2) 的算法吗？
#
#

# @lcpr-template-start
from typing import List


# @lcpr-template-end
# @lc code=start
class Solution:

    def __violence__(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            res = target - nums[i]
            if res in nums[i + 1:]:
                return [i, nums[i + 1:].index(res) + i + 1]
        return []
    
    def __hashtable__(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            res = target - num
            if res in dict:
                return [dict[res], i]
            dict[num] = i
        return []

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return self.__violence__(nums, target)
        return self.__hashtable__(nums, target)


# @lc code=end

#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n6\n
# @lcpr case=end

#
