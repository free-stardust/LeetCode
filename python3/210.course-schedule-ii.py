#
# @lc app=leetcode.cn id=210 lang=python3
# @lcpr version=30204
#
# [210] 课程表 II
#
# https://leetcode.cn/problems/course-schedule-ii/description/
#
# algorithms
# Medium (58.26%)
# Likes:    972
# Dislikes: 0
# Total Accepted:    248.1K
# Total Submissions: 424.8K
# Testcase Example:  '2\n[[1,0]]'
#
# 现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。给你一个数组 prerequisites ，其中
# prerequisites[i] = [ai, bi] ，表示在选修课程 ai 前 必须 先选修 bi 。
#
#
# 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1] 。
#
#
# 返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 任意一种 就可以了。如果不可能完成所有课程，返回 一个空数组 。
#
#
#
# 示例 1：
#
# 输入：numCourses = 2, prerequisites = [[1,0]]
# 输出：[0,1]
# 解释：总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
#
#
# 示例 2：
#
# 输入：numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# 输出：[0,2,1,3]
# 解释：总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
# 因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。
#
# 示例 3：
#
# 输入：numCourses = 1, prerequisites = []
# 输出：[0]
#
#
#
# 提示：
#
#
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# 所有[ai, bi] 互不相同
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

    def use_dfs(self, numCourses: int,
                prerequisites: List[List[int]]) -> List[int]:
        ans = []
        edges = collections.defaultdict(list)
        visited = [0] * numCourses
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

            visited[u] = 2
            ans.append(u)

        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)

        if not valid:
            return []

        return ans[::-1]

    def use_bfs(self, numCourses: int,
                prerequisites: List[List[int]]) -> List[int]:
        ans = []
        edges = collections.defaultdict(list)
        indeg = [0] * numCourses

        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1

        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])

        while q:
            u = q.popleft()
            ans.append(u)
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        if len(ans) != numCourses:
            return []

        return ans

    def findOrder(self, numCourses: int,
                  prerequisites: List[List[int]]) -> List[int]:
        # return self.use_dfs(numCourses, prerequisites)
        return self.use_bfs(numCourses, prerequisites)


# @lc code=end

#
# @lcpr case=start
# 2\n[[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[[1,0],[2,0],[3,1],[3,2]]\n
# @lcpr case=end

# @lcpr case=start
# 1\n[]\n
# @lcpr case=end

#
