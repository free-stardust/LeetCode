#
# @lc app=leetcode.cn id=16 lang=python3
# @lcpr version=30204
#
# [16] 最接近的三数之和
#
# https://leetcode.cn/problems/3sum-closest/description/
#
# algorithms
# Medium (44.79%)
# Likes:    1640
# Dislikes: 0
# Total Accepted:    575.8K
# Total Submissions: 1.3M
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。
#
# 返回这三个数的和。
#
# 假定每组输入只存在恰好一个解。
#
#
#
# 示例 1：
#
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#
#
# 示例 2：
#
# 输入：nums = [0,0,0], target = 1
# 输出：0
#
#
#
#
# 提示：
#
#
# 3 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# -10^4 <= target <= 10^4
#
#
#

# @lcpr-template-start
from asyncio.base_tasks import _task_get_stack
from math import inf
from typing import List, Tuple
from typing import Optional


# @lcpr-template-end
# @lc code=start
class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = 0
        min_dis = inf
        nums.sort()
        nums_len = len(nums)
        for i in range(nums_len - 2):
            # 这个判断是因为在后续双指针那里计算过了，所以不需要再重复计算，跳过相同值
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # 如果大于目标值，后续肯定更大，所有没必要再进行后续计算，再判断后可以直接跳过
            tmp_sum = nums[i] + nums[i+1] + nums[i+2]
            if tmp_sum > target:
                if tmp_sum - target < min_dis:
                    ans = tmp_sum
                break
            
            # 如果和最后两值相加还是小于目标值，说明只需要移动第一个元素位置，直接下一轮循环
            tmp_sum = nums[i] + nums[-2] + nums[-1]
            if tmp_sum < target:
                if  target - tmp_sum < min_dis:
                    ans = tmp_sum
                    min_dis = target - tmp_sum
                continue

            L, R = i + 1, nums_len - 1
            while L < R:
                tmp_sum = nums[i] + nums[L] + nums[R]
                if tmp_sum == target:   # 和目标值相等，直接返回
                    return tmp_sum
                if tmp_sum > target:    # 如果大于目标值，则移动右边指针
                    if tmp_sum - target < min_dis:
                        min_dis = tmp_sum - target
                        ans = tmp_sum
                    R -= 1
                else:   # 反之，如果小于目标值，则移动左指针
                    if target - tmp_sum < min_dis:
                        min_dis = target - tmp_sum
                        ans = tmp_sum
                    L += 1  
                
        return ans


# @lc code=end

nums = [([-1, 2, 1, -4], 1), ([0, 0, 0], 1)]
ans = [2, 0]
for p, a in zip(nums, ans):
    res = Solution().threeSumClosest(p[0], p[1])
    print(
        f"nums = {p[0]}, target = {p[1]}, ans = {a}, res = {res}, {a == res}.")

#
# @lcpr case=start
# [-1,2,1,-4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n1\n
# @lcpr case=end

#
