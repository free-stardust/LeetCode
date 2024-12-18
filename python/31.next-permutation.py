#
# @lc app=leetcode.cn id=31 lang=python3
# @lcpr version=30204
#
# [31] 下一个排列
#
# https://leetcode.cn/problems/next-permutation/description/
#
# algorithms
# Medium (39.61%)
# Likes:    2535
# Dislikes: 0
# Total Accepted:    540.5K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,3]'
#
# 整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。
#
#
# 例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
#
#
# 整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列
# 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。
#
#
# 例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
# 类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
# 而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
#
#
# 给你一个整数数组 nums ，找出 nums 的下一个排列。
#
# 必须 原地 修改，只允许使用额外常数空间。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：[1,3,2]
#
#
# 示例 2：
#
# 输入：nums = [3,2,1]
# 输出：[1,2,3]
#
#
# 示例 3：
#
# 输入：nums = [1,1,5]
# 输出：[1,5,1]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
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

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        if nums_len < 2:
            return

        j = -1
        for i in range(nums_len - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                j = i - 1
                break

        if j >= 0:
            k = -1
            for i in range(nums_len - 1, j, -1):
                if nums[j] < nums[i]:
                    k = i
                    break
            tmp = nums[j]
            nums[j] = nums[k]
            nums[k] = tmp

        for i in range(j + 1, j + 1 + (nums_len - 1 - j) // 2):
            tmp = nums[i]
            nums[i] = nums[nums_len - i + j]
            nums[nums_len - i + j] = tmp

        # nums[j + 1:] = sorted(nums[j + 1:])


# @lc code=end

tests = [[1, 2, 3], [3, 2, 1], [1, 1, 5], [1, 2], [2, 1, 3, 4, 1]]
ans = [[1, 3, 2], [1, 2, 3], [1, 5, 1], [2, 1], [2, 1, 4, 1, 3]]
for i, (t, a) in enumerate(zip(tests, ans)):
    tmp_t = t.copy()
    Solution().nextPermutation(t)
    print(f"test case {i+1}:\n"
          f"\ttest = {tmp_t};\n"
          f"\tans = {a};\n"
          f"\tres = {t};\n"
          f"\t{a == t}.")

#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,5]\n
# @lcpr case=end

#
