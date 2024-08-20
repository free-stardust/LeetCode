#
# @lc app=leetcode.cn id=79 lang=python3
# @lcpr version=30204
#
# [79] 单词搜索
#
# https://leetcode.cn/problems/word-search/description/
#
# algorithms
# Medium (47.28%)
# Likes:    1863
# Dislikes: 0
# Total Accepted:    558.3K
# Total Submissions: 1.2M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
#
#
# 示例 1：
#
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
# "ABCCED"
# 输出：true
#
#
# 示例 2：
#
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
# "SEE"
# 输出：true
#
#
# 示例 3：
#
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
# "ABCB"
# 输出：false
#
#
#
#
# 提示：
#
#
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board 和 word 仅由大小写英文字母组成
#
#
#
#
# 进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？
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

    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        def check(row, col, word_index) -> bool:
            if board[row][col] != word[word_index]:
                return False
            if word_index == len(word) - 1:
                return True

            res = False
            visited.add((row, col))

            for step_row, step_col in directions:
                next_row, next_col = row + step_row, col + step_col
                if 0 <= next_row < len(board) and \
                    0 <= next_col < len(board[0]):
                    if (next_row, next_col) not in visited:
                        if check(next_row, next_col, word_index + 1):
                            res = True
                            break

            visited.remove((row, col))
            return res

        row_len, col_len = len(board), len(board[0])

        for row in range(row_len):
            for col in range(col_len):
                if check(row, col, 0):
                    return True

        return False


# @lc code=end


def print_matrix(matrix):
    for row in matrix:
        print("\t\t" + str(row))


tests = [[[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
          "ABCCED"],
         [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
          "SEE"],
         [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
          "ABCB"]]
ans = [True, True, False]
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().exist(t[0], t[1])
    print(f"test case {i+1}:\n"
          f"\ttest: board = ")
    print_matrix(t[0])
    print(f"\t      word = {t[1]};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"\n
# @lcpr case=end

# @lcpr case=start
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"SEE"\n
# @lcpr case=end

# @lcpr case=start
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCB"\n
# @lcpr case=end

#
