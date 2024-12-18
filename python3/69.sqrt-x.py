#
# @lc app=leetcode.cn id=69 lang=python3
# @lcpr version=30204
#
# [69] x 的平方根 
#
# https://leetcode.cn/problems/sqrtx/description/
#
# algorithms
# Easy (38.58%)
# Likes:    1571
# Dislikes: 0
# Total Accepted:    941.3K
# Total Submissions: 2.4M
# Testcase Example:  '4'
#
# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
# 
# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
# 
# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
# 
# 
# 
# 示例 1：
# 
# 输入：x = 4
# 输出：2
# 
# 
# 示例 2：
# 
# 输入：x = 8
# 输出：2
# 解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= x <= 2^31 - 1
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
    def claculator(self, x: int) -> int:
        if x == 0:
            return 0
        ans = int(math.exp(0.5 * math.log(x)))
        return ans + 1 if (ans + 1) ** 2 <= x else ans
    
    def binary(self, x: int) -> int:
        l, r, ans = 0, x, -1
        
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return ans
    
    def newton_recursion(self, x: int) -> int:
        if x == 0:
            return 0
        
        c, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + c / x0)
            if abs(x0 -xi) < 1e-7:
                break
            x0 = xi
        
        return int(x0)

    def mySqrt(self, x: int) -> int:
        # return self.claculator(x)
        # return self.binary(x)
        return self.newton_recursion(x)
# @lc code=end

tests = [4, 8]
ans = [2, 2]
for i,(t,a) in enumerate(zip(tests, ans)):
    res = Solution().mySqrt(t)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 8\n
# @lcpr case=end

#

