#
# @lc app=leetcode.cn id=80 lang=python3
# @lcpr version=30204
#
# [80] 删除有序数组中的重复项 II
#
# https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/description/
#
# algorithms
# Medium (62.05%)
# Likes:    1092
# Dislikes: 0
# Total Accepted:    442.7K
# Total Submissions: 712.7K
# Testcase Example:  '[1,1,1,2,2,3]'
#
# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。
# 
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
# 
# 
# 
# 说明：
# 
# 为什么返回数值是整数，但输出的答案是数组呢？
# 
# 请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
# 
# 你可以想象内部操作如下:
# 
# // nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
# int len = removeDuplicates(nums);
# 
# // 在函数里修改输入数组对于调用者是可见的。
# // 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
# for (int i = 0; i < len; i++) {
# print(nums[i]);
# }
# 
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,1,1,2,2,3]
# 输出：5, nums = [1,1,2,2,3]
# 解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3。 不需要考虑数组中超出新长度后面的元素。
# 
# 
# 示例 2：
# 
# 输入：nums = [0,0,1,1,1,1,2,3,3]
# 输出：7, nums = [0,0,1,1,2,3,3]
# 解释：函数应返回新长度 length = 7, 并且原数组的前七个元素被修改为 0, 0, 1, 1, 2, 3,
# 3。不需要考虑数组中超出新长度后面的元素。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 3 * 10^4
# -10^4 <= nums[i] <= 10^4
# nums 已按升序排列
# 
# 
#


# @lcpr-template-start
import copy
import collections
import random
import math
from collections import namedtuple
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush
# @lcpr-template-end
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_len = len(nums)

        if nums_len <= 2:
            return nums_len
        
        slow, fast = 2, 2
        
        while fast < nums_len:
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow
# @lc code=end

tests = [[1,1,1,2,2,3], [0,0,1,1,1,1,2,3,3]]
ans = [[5, [1,1,2,2,3]], [7, [0,0,1,1,2,3,3]]]

for i, (t,a) in enumerate(zip(tests, ans)):
    tmp_t = t.copy()
    res = Solution().removeDuplicates(t)
    print(f"test case {i+1}:\n"
          f"\ttest = {tmp_t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a[0] == res}, {t == a[1]}.")

#
# @lcpr case=start
# [1,1,1,2,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,1,2,3,3]\n
# @lcpr case=end

#

