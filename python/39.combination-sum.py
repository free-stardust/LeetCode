#
# @lc app=leetcode.cn id=39 lang=python3
# @lcpr version=30204
#
# [39] 组合总和
#
# https://leetcode.cn/problems/combination-sum/description/
#
# algorithms
# Medium (72.93%)
# Likes:    2855
# Dislikes: 0
# Total Accepted:    995.4K
# Total Submissions: 1.4M
# Testcase Example:  '[2,3,6,7]\n7'
#
# 给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target
# 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
#
# candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。
#
# 对于给定的输入，保证和为 target 的不同组合数少于 150 个。
#
#
#
# 示例 1：
#
# 输入：candidates = [2,3,6,7], target = 7
# 输出：[[2,2,3],[7]]
# 解释：
# 2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
# 7 也是一个候选， 7 = 7 。
# 仅有这两种组合。
#
# 示例 2：
#
# 输入: candidates = [2,3,5], target = 8
# 输出: [[2,2,2,2],[2,3,3],[3,5]]
#
# 示例 3：
#
# 输入: candidates = [2], target = 1
# 输出: []
#
#
#
#
# 提示：
#
#
# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# candidates 的所有元素 互不相同
# 1 <= target <= 40
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

    def recursion1(self, candidates: List[int],
                   target: int) -> List[List[int]]:
        def dfs(nexts, cur_res, ans, target) -> None:
            if target == 0:
                ans.append(cur_res)
                return

            for i in range(len(nexts)):
                if nexts[i] <= target:
                    dfs(nexts[i:], cur_res + [nexts[i]], ans, target - nexts[i])
                else:
                    break

        ans = []
        candidates.sort()
        dfs(candidates, [], ans, target)

        return ans

    def recursion2(self, candidates: List[int],
                   target: int) -> List[List[int]]:

        def dfs(candidates, begin, size, path, res, target):
            if target == 0:
                res.append(path)
                return

            for index in range(begin, size):
                residue = target - candidates[index]
                if residue < 0:
                    break

                dfs(candidates, index, size, path + [candidates[index]], res,
                    residue)

        size = len(candidates)
        if size == 0:
            return []
        candidates.sort()
        path = []
        res = []
        dfs(candidates, 0, size, path, res, target)
        return res

    def recursion3(self, candidates: List[int],
                   target: int) -> List[List[int]]:

        def dfs(i: int, s: int):
            if s == 0:
                ans.append(t[:])
                return
            if s < candidates[i]:
                return
            for j in range(i, len(candidates)):
                t.append(candidates[j])
                dfs(j, s - candidates[j])
                t.pop()

        candidates.sort()
        t = []
        ans = []
        dfs(0, target)
        return ans

    def recursion4(self, candidates: List[int],
                   target: int) -> List[List[int]]:

        def dfs(i: int, s: int):
            if s == 0:
                ans.append(t[:])
                return
            if i >= len(candidates) or s < candidates[i]:
                return
            dfs(i + 1, s)
            t.append(candidates[i])
            dfs(i, s - candidates[i])
            t.pop()

        candidates.sort()
        t = []
        ans = []
        dfs(0, target)
        return ans

    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:
        return self.recursion1(candidates, target)
        # return self.recursion2(candidates, target)
        # return self.recursion3(candidates, target)
        # return self.recursion4(candidates, target)

# @lc code=end

tests = [[[2, 3, 6, 7], 7], [[2, 3, 5], 8], [[2], 1], [[3, 5, 8], 11]]
ans = [[[2, 2, 3], [7]], [[2, 2, 2, 2], [2, 3, 3], [3, 5]], [],
       [[3, 3, 5], [3, 8]]]
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().combinationSum(t[0], t[1])
    print(f"test case  {i+1}:\n"
          f"\ttest = {t[0]}, {t[1]};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# [2,3,6,7]\n7\n
# @lcpr case=end

# @lcpr case=start
# [2,3,5]\n8\n
# @lcpr case=end

# @lcpr case=start
# [2]\n1\n
# @lcpr case=end

#
