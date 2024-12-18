#
# @lc app=leetcode.cn id=200 lang=python3
# @lcpr version=30204
#
# [200] 岛屿数量
#
# https://leetcode.cn/problems/number-of-islands/description/
#
# algorithms
# Medium (60.95%)
# Likes:    2572
# Dislikes: 0
# Total Accepted:    908.7K
# Total Submissions: 1.5M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。
#
#
#
# 示例 1：
#
# 输入：grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# 输出：1
#
#
# 示例 2：
#
# 输入：grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# 输出：3
#
#
#
#
# 提示：
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] 的值为 '0' 或 '1'
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

    def use_dfs(self, grid: List[List[str]]) -> int:
        rows = len(grid)

        if rows == 0:
            return 0

        cols = len(grid[0])

        def dfs(row: int, col: int):
            grid[row][col] = "0"

            for r, c in [(row - 1, col), (row + 1, col), (row, col - 1),
                         (row, col + 1)]:
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1":
                    dfs(r, c)

        ans = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    ans += 1
                    dfs(row, col)

        return ans

    def use_bfs(self, grid: List[List[str]]) -> int:
        rows = len(grid)

        if rows == 0:
            return 0

        cols = len(grid[0])

        def bfs(row: int, col: int):
            grid[row][col] = "0"
            deque = collections.deque([(row, col)])

            while deque:
                r, c = deque.popleft()
                for _r, _c in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= _r < rows and 0 <= _c < cols and grid[_r][_c] == "1":
                        deque.append((_r, _c))
                        grid[_r][_c] = "0"

        ans = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    ans += 1
                    bfs(row, col)

        return ans

    def use_union_find(self, grid: List[List[str]]) -> int:
        rows = len(grid)

        if rows == 0:
            return 0

        cols = len(grid[0])

        union_parent = [0] * (rows * cols)
        ans = 0

        for row in range(rows):
            for col in range(cols):
                idx = row * cols + col
                union_parent[idx] = idx
                if grid[row][col] == "1":
                    ans += 1

        def find(i: int):
            if union_parent[i] == i:
                return union_parent[i]
            union_parent[i] = find(union_parent[i])
            return union_parent[i]

        def union(i: int, j: int):
            if find(i) == find(j):
                return
            union_parent[find(i)] = union_parent[find(j)]
            nonlocal ans
            ans -= 1

        for row in range(rows):
            for col in range(cols):
                idx = row * cols + col
                if grid[row][col] == "1":
                    if row + 1 < rows and grid[row + 1][col] == "1":
                        union(idx, (row + 1) * cols + col)
                    if col + 1 < cols and grid[row][col + 1] == "1":
                        union(idx, row * cols + col + 1)

        return ans

    def numIslands(self, grid: List[List[str]]) -> int:
        # return self.use_dfs(grid)
        # return self.use_bfs(grid)
        return self.use_union_find(grid)


# @lc code=end

tests = [[["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
          ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]],
         [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
          ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]],
         [[
             "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1",
             "1", "1", "0", "1", "0", "1", "1"
         ],
          [
              "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
              "0", "1", "1", "1", "1", "1", "0"
          ],
          [
              "1", "0", "1", "1", "1", "0", "0", "1", "1", "0", "1", "1", "1",
              "1", "1", "1", "1", "1", "1", "1"
          ],
          [
              "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1",
              "1", "1", "1", "1", "1", "1", "1"
          ],
          [
              "1", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
              "1", "1", "1", "1", "1", "1", "1"
          ],
          [
              "1", "0", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0",
              "1", "1", "1", "0", "1", "1", "1"
          ],
          [
              "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0",
              "1", "1", "0", "1", "1", "1", "1"
          ],
          [
              "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0",
              "1", "1", "1", "1", "0", "1", "1"
          ],
          [
              "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1",
              "1", "1", "1", "1", "1", "1", "1"
          ],
          [
              "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
              "1", "1", "1", "1", "1", "1", "1"
          ],
          [
              "0", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1",
              "1", "1", "1", "1", "1", "1", "1"
          ],
          [
              "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
              "1", "1", "1", "1", "1", "1", "1"
          ],
          [
              "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
              "1", "1", "1", "1", "1", "1", "1"
          ],
          [
              "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1",
              "0", "1", "1", "1", "1", "1", "1"
          ],
          [
              "1", "0", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "1",
              "1", "1", "1", "0", "1", "1", "1"
          ],
          [
              "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0",
              "1", "1", "1", "1", "1", "1", "0"
          ],
          [
              "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
              "0", "1", "1", "1", "1", "0", "0"
          ],
          [
              "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
              "1", "1", "1", "1", "1", "1", "1"
          ],
          [
              "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
              "1", "1", "1", "1", "1", "1", "1"
          ],
          [
              "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
              "1", "1", "1", "1", "1", "1", "1"
          ]]]
ans = [1, 3, 1]
all_pass = True
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().numIslands(t)
    all_pass &= (a == res)
    print(f"test case {i+1}:\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res};")
print(f"all pass: {all_pass}.")

#
# @lcpr case=start
# [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]\n
# @lcpr case=end

#
