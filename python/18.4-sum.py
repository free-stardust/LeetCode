#
# @lc app=leetcode.cn id=18 lang=python3
# @lcpr version=30204
#
# [18] 四数之和
#
# https://leetcode.cn/problems/4sum/description/
#
# algorithms
# Medium (36.63%)
# Likes:    1939
# Dislikes: 0
# Total Accepted:    611.9K
# Total Submissions: 1.7M
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a],
# nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：
#
#
# 0 <= a, b, c, d < n
# a、b、c 和 d 互不相同
# nums[a] + nums[b] + nums[c] + nums[d] == target
#
#
# 你可以按 任意顺序 返回答案 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#
#
# 示例 2：
#
# 输入：nums = [2,2,2,2,2], target = 8
# 输出：[[2,2,2,2]]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 200
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
#
#
#

# @lcpr-template-start
from typing import List, Tuple
from typing import Optional


# @lcpr-template-end
# @lc code=start
class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums_len = len(nums)

        if not nums or nums_len < 4:
            return []

        nums.sort()
        for i in range(nums_len - 3):
            if target >= 0 and nums[i] > target:
                return ans

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, nums_len - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                L, R = j + 1, nums_len - 1
                while L < R:
                    tmp_sum = nums[i] + nums[j] + nums[L] + nums[R]
                    if tmp_sum == target:
                        ans.append([nums[i], nums[j], nums[L], nums[R]])
                        while L < R and nums[L] == nums[L + 1]:
                            L += 1
                        while L < R and nums[R] == nums[R - 1]:
                            R -= 1
                        L += 1
                        R -= 1
                    elif tmp_sum < target:
                        L += 1
                    else:
                        R -= 1
        return ans


# @lc code=end

tests = [[[1, 0, -1, 0, -2, 2], 0], [[2, 2, 2, 2, 2], 8], [[0, 0, 0, 0], 0],
         [[2, 2, 2, 2, 2], 8], [[-2, -1, -1, 1, 1, 2, 2], 0],
         [[1, -2, -5, -4, -3, 3, 3, 5], -11]]
ans = [[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]], [[2, 2, 2, 2]],
       [[0, 0, 0, 0]], [[2, 2, 2, 2]], [[-2, -1, 1, 2], [-1, -1, 1, 1]],
       [[-5, -4, -3, 1]]]
for i, t, a in zip(range(len(tests)), tests, ans):
    res = Solution().fourSum(t[0], t[1])
    print(f"test case {i+1}:\n"
          f"\ttest = {t[0]}, {t[1]};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# [1,0,-1,0,-2,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,2,2]\n8\n
# @lcpr case=end

#
