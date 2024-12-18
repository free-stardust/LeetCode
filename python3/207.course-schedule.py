#
# @lc app=leetcode.cn id=207 lang=python3
# @lcpr version=30204
#
# [207] 课程表
#
# https://leetcode.cn/problems/course-schedule/description/
#
# algorithms
# Medium (54.21%)
# Likes:    2008
# Dislikes: 0
# Total Accepted:    451.4K
# Total Submissions: 830K
# Testcase Example:  '2\n[[1,0]]'
#
# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
#
# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi]
# ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
#
#
# 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
#
#
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
# 输入：numCourses = 2, prerequisites = [[1,0]]
# 输出：true
# 解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
#
# 示例 2：
#
# 输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
# 输出：false
# 解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
#
#
#
# 提示：
#
#
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# prerequisites[i] 中的所有课程对 互不相同
#
#
#

# @lcpr-template-start
import copy
import collections
import random
import math
from functools import reduce
from collections import namedtuple
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush


# @lcpr-template-end
# @lc code=start
class Solution:

    def use_dfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        visited = [0] * numCourses
        # result = list()
        valid = True

        for info in prerequisites:
            edges[info[1]].append(info[0])

        def dfs(u: int):
            nonlocal valid
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    valid = False
                    return
            visited[u] = 2  # 此处用来标识这个节点已经被搜索完成
            # result.append(u)

        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)

        return valid

    def use_bfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        indeg = [0] * numCourses
        visited = 0

        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1

        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])

        while q:
            visited += 1
            u = q.popleft()
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return visited == numCourses

    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        # return self.use_dfs(numCourses, prerequisites)
        return self.use_bfs(numCourses, prerequisites)


# @lc code=end

tests = [[2, [[1, 0]]], [2, [[1, 0], [0, 1]]], [2, [[0, 1]]]]
ans = [True, False, True]
all_pass = True
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().canFinish(t[0], t[1])
    all_pass &= (a == res)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res};")
print(f"all pass: {all_pass}.")

#
# @lcpr case=start
# 2\n[[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[[1,0],[0,1]]\n
# @lcpr case=end

#
