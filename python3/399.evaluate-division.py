#
# @lc app=leetcode.cn id=399 lang=python3
# @lcpr version=30204
#
# [399] 除法求值
#
# https://leetcode.cn/problems/evaluate-division/description/
#
# algorithms
# Medium (58.72%)
# Likes:    1125
# Dislikes: 0
# Total Accepted:    107.3K
# Total Submissions: 182.8K
# Testcase Example:  '[["a","b"],["b","c"]]\n' +
#   '[2.0,3.0]\n' +
#   '[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]'
#
# 给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和
# values[i] 共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。
#
# 另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj =
# ? 的结果作为答案。
#
# 返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 -1.0
# 替代这个答案。
#
# 注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。
#
# 注意：未在等式列表中出现的变量是未定义的，因此无法确定它们的答案。
#
#
#
# 示例 1：
#
# 输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries =
# [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# 输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
# 解释：
# 条件：a / b = 2.0, b / c = 3.0
# 问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# 结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]
# 注意：x 是未定义的 => -1.0
#
# 示例 2：
#
# 输入：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0],
# queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# 输出：[3.75000,0.40000,5.00000,0.20000]
#
#
# 示例 3：
#
# 输入：equations = [["a","b"]], values = [0.5], queries =
# [["a","b"],["b","a"],["a","c"],["x","y"]]
# 输出：[0.50000,2.00000,-1.00000,-1.00000]
#
#
#
#
# 提示：
#
#
# 1 <= equations.length <= 20
# equations[i].length == 2
# 1 <= Ai.length, Bi.length <= 5
# values.length == equations.length
# 0.0 < values[i] <= 20.0
# 1 <= queries.length <= 20
# queries[i].length == 2
# 1 <= Cj.length, Dj.length <= 5
# Ai, Bi, Cj, Dj 由小写英文字母与数字组成
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

    def calcEquation1(self, equations: List[List[str]], values: List[float],
                      queries: List[List[str]]) -> List[float]:

        graph = collections.defaultdict(dict)
        for (a, b), v in zip(equations, values):
            graph[a][b] = v
            graph[b][a] = 1 / v

        def dfs(a: str, b: str, path: List[str]) -> float:
            if a not in graph or b not in graph:
                return -1.0
            if a == b:
                return 1.0
            for p in graph[a]:
                if p not in path:
                    path.append(p)
                    res = graph[a][p] * dfs(p, b, path)
                    if res > 0:
                        return res
                    else:
                        continue
                else:
                    continue
            return -1.0

        res = []
        for a, b in queries:
            res.append(dfs(a, b, [a]))

        return res if res else [-1.0]

    def calcEquation2(self, equations: List[List[str]], values: List[float],
                      queries: List[List[str]]) -> List[float]:

        graph = collections.defaultdict(dict)
        for (a, b), v in zip(equations, values):
            graph[a][b] = v
            graph[b][a] = 1 / v

        def dfs(a: str, b: str) -> float:
            if a not in graph or b not in graph:
                return -1.0
            if a == b:
                return 1.0
            for p in graph[a]:
                if p == b:
                    return graph[a][b]
                elif p not in visited:
                    visited.add(p)
                    v = dfs(p, b)
                    if v != -1:
                        return graph[a][p] * v
            return -1.0

        res = []
        for a, b in queries:
            visited = set()
            res.append(dfs(a, b))

        return res if res else [-1.0]

    def calcEquation3(self, equations: List[List[str]], values: List[float],
                      queries: List[List[str]]) -> List[float]:

        graph = {}
        for (x, y), v in zip(equations, values):
            if x in graph:
                graph[x][y] = v
            else:
                graph[x] = {y: v}
            if y in graph:
                graph[y][x] = 1 / v
            else:
                graph[y] = {x: 1 / v}

        def dfs(s, t) -> int:
            if s not in graph:
                return -1
            if t == s:
                return 1
            for node in graph[s].keys():
                if node == t:
                    return graph[s][node]
                elif node not in visited:
                    visited.add(node)
                    v = dfs(node, t)
                    if v != -1:
                        return graph[s][node] * v
            return -1

        res = []
        for qs, qt in queries:
            visited = set()
            res.append(dfs(qs, qt))
        return res

    def calcEquation(self, equations: List[List[str]], values: List[float],
                     queries: List[List[str]]) -> List[float]:
        return self.calcEquation2(equations, values, queries)


# @lc code=end

tests = tests = [
    [
        [["a", "b"], ["b", "c"]],
        [2.0, 3.0],
        [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
    ],
    [
        [["a", "b"], ["b", "c"], ["bc", "cd"]],
        [1.5, 2.5, 5.0],
        [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
    ],
    [
        [["a", "b"]],
        [0.5],
        [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]],
    ],
    [[["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]],
     [3.0, 4.0, 5.0, 6.0],
     [["x1", "x5"], ["x5", "x2"], ["x2", "x4"], ["x2", "x2"], ["x2", "x9"],
      ["x9", "x9"]]],
]
ans = [[6.0, 0.5, -1.0, 1.0, -1.0], [3.75, 0.4, 5.0, 0.2],
       [0.5, 2.0, -1.0, -1.0], [360.0, 0.00833, 20.0, 1.0, -1.0, -1.0]]
all_pass = True
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().calcEquation(t[0], t[1], t[2])
    res = [round(x, 5) for x in res]
    print(f"test case {i+1}:\n"
          f"\ttest:\n"
          f"\t\tequations = {t[0]},\n"
          f"\t\tvalues = {t[1]},\n"
          f"\t\tqueries = {t[2]};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")
    all_pass = all_pass and a == res
print(f"all pass: {all_pass}.")

#
# @lcpr case=start
# [["a","b"],["b","c"]]\n[2.0,3.0]\n[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]\n
# @lcpr case=end

# @lcpr case=start
# [["a","b"],["b","c"],["bc","cd"]]\n[1.5,2.5,5.0]\n[["a","c"],["c","b"],["bc","cd"],["cd","bc"]]\n
# @lcpr case=end

# @lcpr case=start
# [["a","b"]]\n[0.5]\n[["a","b"],["b","a"],["a","c"],["x","y"]]\n
# @lcpr case=end

#
