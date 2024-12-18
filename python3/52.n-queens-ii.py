#
# @lc app=leetcode.cn id=52 lang=python3
# @lcpr version=30204
#
# [52] N 皇后 II
#
# https://leetcode.cn/problems/n-queens-ii/description/
#
# algorithms
# Hard (82.35%)
# Likes:    519
# Dislikes: 0
# Total Accepted:    157K
# Total Submissions: 190.5K
# Testcase Example:  '4'
#
# n 皇后问题 研究的是如何将 n 个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 
# 给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：n = 4
# 输出：2
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
# 
# 
# 示例 2：
# 
# 输入：n = 1
# 输出：1
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
from collections import namedtuple
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush
# @lcpr-template-end
# @lc code=start
class Solution:
    def recursion1(self, n: int) -> int:
        ans = 0

        cols = set()
        diags1 = set()
        diags2 = set()
        
        def backtrace(row: int):
            if row == n:
                nonlocal ans
                ans += 1
            else:
                for col in range(n):
                    if col in cols or row - col in diags1 or row + col in diags2:
                        continue

                    cols.add(col)
                    diags1.add(row - col)
                    diags2.add(row + col)

                    backtrace(row + 1)
                    
                    cols.remove(col)
                    diags1.remove(row - col)
                    diags2.remove(row + col)

        backtrace(0)

        return ans

    def totalNQueens(self, n: int) -> int:
        return self.recursion1(n)
# @lc code=end

tests = [4, 1]
ans = [2, 1]
for i, (t,a) in enumerate(zip(tests, ans)):
    res = Solution().totalNQueens(t)
    print(f"test case {i+1}:\n"
          f"\ttest: n = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

