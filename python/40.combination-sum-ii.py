#
# @lc app=leetcode.cn id=40 lang=python3
# @lcpr version=30204
#
# [40] 组合总和 II
#
# https://leetcode.cn/problems/combination-sum-ii/description/
#
# algorithms
# Medium (59.49%)
# Likes:    1573
# Dislikes: 0
# Total Accepted:    550.4K
# Total Submissions: 924.9K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用 一次 。
#
# 注意：解集不能包含重复的组合。
#
#
#
# 示例 1:
#
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#
# 示例 2:
#
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ]
#
#
#
# 提示:
#
#
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
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

    def solution1(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(cur_res, target, nexts) -> None:
            if target == 0:
                res.append(cur_res)
                return

            for i in range(len(nexts)):
                if nexts[i] > target or (i > 0 and nexts[i] == nexts[i - 1]):
                    continue
                dfs(cur_res + [nexts[i]], target - nexts[i], nexts[i + 1:])

        dfs([], target, nums)
        return res

    def solution2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        l = len(nums)

        def dfs(cur_res, target, index) -> None:
            if target == 0:
                res.append(cur_res)
                return

            for i in range(index, l):
                if nums[i] > target or (i > index and nums[i] == nums[i - 1]):
                    continue
                dfs(cur_res + [nums[i]], target - nums[i], i + 1)

        dfs([], target, 0)
        return res

    def combinationSum2(self, candidates: List[int],
                        target: int) -> List[List[int]]:
        # return self.solution1(candidates, target)
        return self.solution2(candidates, target)


# @lc code=end

tests = [[[10, 1, 2, 7, 6, 1, 5], 8], [[2, 5, 2, 1, 2], 5]]
ans = [[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]], [[1, 2, 2], [5]]]
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().combinationSum2(t[0], t[1])
    print(f"test case {i+1}:\n"
          f"\ttest = {t[0]}, {t[1]};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# [10,1,2,7,6,1,5]\n8\n
# @lcpr case=end

# @lcpr case=start
# [2,5,2,1,2]\n5\n
# @lcpr case=end

#
