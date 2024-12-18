#
# @lc app=leetcode.cn id=41 lang=python3
# @lcpr version=30204
#
# [41] 缺失的第一个正数
#
# https://leetcode.cn/problems/first-missing-positive/description/
#
# algorithms
# Hard (45.14%)
# Likes:    2173
# Dislikes: 0
# Total Accepted:    420K
# Total Submissions: 929.6K
# Testcase Example:  '[1,2,0]'
#
# 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
# 请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,2,0]
# 输出：3
# 解释：范围 [1,2] 中的数字都在数组中。
# 
# 示例 2：
# 
# 输入：nums = [3,4,-1,1]
# 输出：2
# 解释：1 在数组中，但 2 没有。
# 
# 示例 3：
# 
# 输入：nums = [7,8,9,11,12]
# 输出：1
# 解释：最小的正数 1 没有出现。
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
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
    def solution1(self, nums: List[int]) -> int:
        nums_len = len(nums)
        count = [0] * nums_len
        for num in nums:
            if num > 0 and num <= nums_len:
                count[num - 1] += 1

        for i in range(nums_len):
            if count[i] == 0:
                return i + 1
        return nums_len + 1
    
    def hashtable(self, nums:List[int]) -> int:
        nums_len = len(nums)

        for i in range(nums_len):
            if nums[i] <= 0:
                nums[i] = nums_len + 1
        
        for i in range(nums_len):
            num = abs(nums[i])
            if num <= nums_len:
                nums[num - 1] = -abs(nums[num - 1])

        for i in range(nums_len):
            if nums[i] > 0:
                return i + 1

        return nums_len + 1
    
    def swap(self, nums:List[int]) -> int:
        nums_len = len(nums)
        
        for i in range(nums_len):
            while 1 <= nums[i] <= nums_len and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

                # 下面这种方式不会正常工作，因为下面这个方式会导致 nums[i] 的值先被修改，
                # 而随后的 nums[nums[i] - 1] 会利用改变后的 num[i] 去获取位置，然后
                # 接受赋值，从而导致，赋值位置出现错误
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
        
        for i in range(nums_len):
            if nums[i] != i + 1:
                return i + 1

        return nums_len + 1

    def firstMissingPositive(self, nums: List[int]) -> int:
        # return self.solution1(nums)
        # return self.hashtable(nums)
        return self.swap(nums)
# @lc code=end

tests = [[1,2,0],[3,4,-1,1],[7,8,9,11,12]]
ans = [3,2,1]
for i,(t,a) in enumerate(zip(tests, ans)):
    res = Solution().firstMissingPositive(t)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")
#
# @lcpr case=start
# [1,2,0]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,-1,1]\n
# @lcpr case=end

# @lcpr case=start
# [7,8,9,11,12]\n
# @lcpr case=end

#

