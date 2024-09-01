#
# @lc app=leetcode.cn id=130 lang=python3
# @lcpr version=30204
#
# [130] 被围绕的区域
#
# https://leetcode.cn/problems/surrounded-regions/description/
#
# algorithms
# Medium (46.62%)
# Likes:    1144
# Dislikes: 0
# Total Accepted:    297.7K
# Total Submissions: 637.6K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' 组成，捕获 所有 被围绕的区域：
#
#
# 连接：一个单元格与水平或垂直方向上相邻的单元格连接。
# 区域：连接所有 'O' 的单元格来形成一个区域。
# 围绕：如果您可以用 'X' 单元格 连接这个区域，并且区域中没有任何单元格位于 board 边缘，则该区域被 'X' 单元格围绕。
#
#
# 通过将输入矩阵 board 中的所有 'O' 替换为 'X' 来 捕获被围绕的区域。
#
#
#
#
#
# 示例 1：
#
#
# 输入：board =
# [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
#
# 输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
#
# 解释：
#
# 在上图中，底部的区域没有被捕获，因为它在 board 的边缘并且不能被围绕。
#
#
# 示例 2：
#
#
# 输入：board = [["X"]]
#
# 输出：[["X"]]
#
#
#
#
# 提示：
#
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] 为 'X' 或 'O'
#
#
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

    def dfs(self, board: List[List[str]]) -> None:
        if not board:
            return

        rows, cols = len(board), len(board[0])

        def dfs_find_link_o_edge(row, col):
            if not 0 <= row < rows or not 0 <= col < cols or board[row][
                    col] != "O":
                return

            board[row][col] = "A"
            dfs_find_link_o_edge(row + 1, col)
            dfs_find_link_o_edge(row - 1, col)
            dfs_find_link_o_edge(row, col + 1)
            dfs_find_link_o_edge(row, col - 1)

        for row in range(rows):
            dfs_find_link_o_edge(row, 0)
            dfs_find_link_o_edge(row, cols - 1)

        for col in range(1, cols - 1):
            dfs_find_link_o_edge(0, col)
            dfs_find_link_o_edge(rows - 1, col)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "A":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"

    def bfs(self, board: List[List[str]]) -> None:
        if not board:
            return

        rows, cols = len(board), len(board[0])
        queue = collections.deque()

        for row in range(rows):
            if board[row][0] == "O":
                queue.append((row, 0))
                board[row][0] = "A"
            if board[row][cols - 1] == "O":
                queue.append((row, cols - 1))
                board[row][cols - 1] = "A"

        for col in range(1, cols - 1):
            if board[0][col] == "O":
                queue.append((0, col))
                board[0][col] = "A"
            if board[rows - 1][col] == "O":
                queue.append((rows - 1, col))
                board[rows - 1][col] = "A"

        while queue:
            row, col = queue.popleft()
            for r, c in [(row + 1, col), (row - 1, col), (row, col + 1),
                         (row, col - 1)]:
                if 0 <= r < rows and 0 <= c < cols and board[r][c] == "O":
                    queue.append((r, c))
                    board[r][c] = "A"

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "A":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # self.dfs(board)
        self.bfs(board)


# @lc code=end


def print_list(ls):
    for l in ls:
        print("\t\t" + str(l))


tests = [[["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"],
          ["X", "O", "X", "X"]], [["X"]]]
ans = [[["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"],
        ["X", "O", "X", "X"]], [["X"]]]
all_pass = True
for i, (t, a) in enumerate(zip(tests, ans)):
    origin_t = copy.deepcopy(t)
    Solution().solve(t)
    print(f"test case {i+1}:\n"
          f"\ttest = ")
    print_list(origin_t)
    print(f"\tans =")
    print_list(a)
    print(f"\tres =")
    print_list(t)
    print(f"\t{a == t};")
    all_pass &= a == t
print(f"all pass: {all_pass}.")
#
# @lcpr case=start
# [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]\n
# @lcpr case=end

# @lcpr case=start
# [["X"]]\n
# @lcpr case=end

#
