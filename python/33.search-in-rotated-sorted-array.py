#
# @lc app=leetcode.cn id=33 lang=python3
# @lcpr version=30204
#
# [33] 搜索旋转排序数组
#
# https://leetcode.cn/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (44.46%)
# Likes:    2984
# Dislikes: 0
# Total Accepted:    926.6K
# Total Submissions: 2.1M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# 整数数组 nums 按升序排列，数组中的值 互不相同 。
# 
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k],
# nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始
# 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
# 
# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
# 
# 你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
# 
# 
# 示例 2：
# 
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1
# 
# 示例 3：
# 
# 输入：nums = [1], target = 0
# 输出：-1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# nums 中的每个值都 独一无二
# 题目数据保证 nums 在预先未知的某个下标上进行了旋转
# -10^4 <= target <= 10^4
# 
# 
#


# @lcpr-template-start
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush
# @lcpr-template-end
# @lc code=start
class Solution:
    def binSearch1(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        return self.binSearch1(nums, target)
# @lc code=end

tests = [[[4,5,6,7,0,1,2], 0], [[4,5,6,7,0,1,2], 3], [[1],0]]
ans = [4, -1, -1]
for i,(t,a) in enumerate(zip(tests, ans)):
    res = Solution().search(t[0], t[1])
    print(f"test case {i+1}:\n"
          f"\ttest = {t[0]}, {t[1]};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")
#
# @lcpr case=start
# [4,5,6,7,0,1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [4,5,6,7,0,1,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#

