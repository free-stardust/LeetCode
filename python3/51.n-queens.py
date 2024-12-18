#
# @lc app=leetcode.cn id=51 lang=python3
# @lcpr version=30204
#
# [51] N 皇后
#
# https://leetcode.cn/problems/n-queens/description/
#
# algorithms
# Hard (74.20%)
# Likes:    2110
# Dislikes: 0
# Total Accepted:    425.5K
# Total Submissions: 573.1K
# Testcase Example:  '4'
#
# 按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
#
# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
#
#
#
# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
#
#
#
# 示例 1：
#
# 输入：n = 4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
#
#
# 示例 2：
#
# 输入：n = 1
# 输出：[["Q"]]
#
#
#
#
# 提示：
#
#
# 1 <= n <= 9
#
#
#
#
#

# @lcpr-template-start
import copy
import collections
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush


# @lcpr-template-end
# @lc code=start
class Solution:

    def backtrack1(self, n: int) -> List[List[str]]:
        solutions = list()
        queens = [-1] * n
        row = ['.'] * n
        columns = set()
        diagnoal1 = set()
        diagnoal2 = set()

        def generate_board() -> List[str]:
            board = list()
            for i in range(n):
                row[queens[i]] = 'Q'
                board.append("".join(row))
                row[queens[i]] = '.'
            return board

        def backtrack(row: int):
            if row == n:
                board = generate_board()
                solutions.append(board)
            else:
                for i in range(n):
                    if i in columns or row - i in diagnoal1 or row + i in diagnoal2:
                        continue
                    queens[row] = i
                    columns.add(i)
                    diagnoal1.add(row - i)
                    diagnoal2.add(row + i)
                    backtrack(row + 1)
                    columns.remove(i)
                    diagnoal1.remove(row - i)
                    diagnoal2.remove(row + i)

        backtrack(0)

        return solutions
    
    def backtrace2(self, n: int) -> List[List[str]]:
        solutions = []
        board = [["."] * n for _ in range(n)]
        cols, diags1, diags2= set(), set(), set()
        
        def backtrack(row: int):
            if row == n:
                solutions.append(["".join(r) for r in board])
            else:
                for col in range(n):
                    if col in cols or row-col in diags1 or row + col in diags2:
                        continue
                    
                    board[row][col] = "Q"
                    cols.add(col)
                    diags1.add(row - col)
                    diags2.add(row + col)

                    backtrack(row + 1)

                    board[row][col] = "."
                    cols.remove(col)
                    diags1.remove(row - col)
                    diags2.remove(row + col)
        
        backtrack(0)
        
        return solutions        


    def solveNQueens(self, n: int) -> List[List[str]]:
        return self.backtrack1(n)
        # return self.backtrace2(n)


# @lc code=end


def print_ans(ans):
    if len(ans) == 0:
        print("\t\t[[]]")
        return

    for a in ans:
        print("\t\t" + str(a))


tests = [4, 1]
ans = [[[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]],
       [["Q"]]]
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().solveNQueens(t)
    print(f"test case {i+1};\n"
          f"\ttest: n = {t};\n"
          f"\tasn = ")
    print_ans(a)
    print(f"\tres = ")
    print_ans(res)
    print(f"\t{a == res}.")

#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#
