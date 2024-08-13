#
# @lc app=leetcode.cn id=50 lang=python3
# @lcpr version=30204
#
# [50] Pow(x, n)
#
# https://leetcode.cn/problems/powx-n/description/
#
# algorithms
# Medium (38.45%)
# Likes:    1373
# Dislikes: 0
# Total Accepted:    469.5K
# Total Submissions: 1.2M
# Testcase Example:  '2.00000\n10'
#
# 实现 pow(x, n) ，即计算 x 的整数 n 次幂函数（即，x^n^ ）。
# 
# 
# 
# 示例 1：
# 
# 输入：x = 2.00000, n = 10
# 输出：1024.00000
# 
# 
# 示例 2：
# 
# 输入：x = 2.10000, n = 3
# 输出：9.26100
# 
# 
# 示例 3：
# 
# 输入：x = 2.00000, n = -2
# 输出：0.25000
# 解释：2^-2 = 1/2^2 = 1/4 = 0.25
# 
# 
# 
# 
# 提示：
# 
# 
# -100.0 < x < 100.0
# -2^31 <= n <= 2^31-1
# n 是一个整数
# 要么 x 不为零，要么 n > 0 。
# -10^4 <= x^n <= 10^4
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
    def recursion1(self, x: float, n: int) -> float:
        if n == 0.0:
            return 1
        
        if x == 1.0:
            return 1.0 

        if x == -1.0:
             return -1.0 if n % 2 == 1 else 1.0
        
        if n < 0:
            return 1 / x * self.recursion1(1 / x, -n - 1)
        else:
            return x * self.recursion1(x, n - 1)

    def traverse1(self, x: float, n: int) -> float:
        ans = 1.0

        if x == 1.0:
            return ans
        
        if x == -1.0:
            return -ans if n % 2 == 1 else ans

        if n < 0:
            x = 1 / x
            n = -n
        
        for i in range(n):
            if ans == 0.0:
                return 0.0
            ans *= x
        
        return ans
    
    def quick_recursion(self, x: float, n: int) -> float:
        def quick_mul(N):
            if N == 0:
                return 1.0
            
            y = quick_mul(N // 2)
            return y * y if N % 2 == 0 else y * y * x
        
        return quick_mul(n) if n >= 0 else 1 / quick_mul(-n)
    
    
    def quick_traverse(self, x: float, n: int) -> float:
        ans = 1.0
        multiplier = x

        n_sign = -1 if n < 0 else 1
        n = n if n >= 0 else -n

        while n > 0:
            if n & 1:
                ans *= multiplier
            multiplier *= multiplier
            n >>= 1

        return ans if n_sign > 0 else 1/ ans

    def myPow(self, x: float, n: int) -> float:
        # return self.recursion1(x, n)
        # return self.traverse1(x, n)
        # return self.quick_recursion(x, n)
        return self.quick_traverse(x, n)
# @lc code=end

tests = [[2.0, 10], [2.1, 3], [2.0, -2], [0.00001, 2147483647]]
ans = [1024.0, 9.261, 0.25, 0.0]
for i,(t,a) in enumerate(zip(tests, ans)):
    res = Solution().myPow(t[0], t[1])
    print(f"test case {i+1}:\n"
          f"\ttests: x = {t[0]}, n = {t[1]};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# 2.00000\n10\n
# @lcpr case=end

# @lcpr case=start
# 2.10000\n3\n
# @lcpr case=end

# @lcpr case=start
# 2.00000\n-2\n
# @lcpr case=end

#

