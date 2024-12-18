#
# @lc app=leetcode.cn id=29 lang=python3
# @lcpr version=30204
#
# [29] 两数相除
#
# https://leetcode.cn/problems/divide-two-integers/description/
#
# algorithms
# Medium (22.34%)
# Likes:    1235
# Dislikes: 0
# Total Accepted:    242.8K
# Total Submissions: 1.1M
# Testcase Example:  '10\n3'
#
# 给你两个整数，被除数 dividend 和除数 divisor。将两数相除，要求 不使用 乘法、除法和取余运算。
# 
# 整数除法应该向零截断，也就是截去（truncate）其小数部分。例如，8.345 将被截断为 8 ，-2.7335 将被截断至 -2 。
# 
# 返回被除数 dividend 除以除数 divisor 得到的 商 。
# 
# 注意：假设我们的环境只能存储 32 位 有符号整数，其数值范围是 [−2^31,  2^31 − 1] 。本题中，如果商 严格大于 2^31 − 1
# ，则返回 2^31 − 1 ；如果商 严格小于 -2^31 ，则返回 -2^31^ 。
# 
# 
# 
# 示例 1:
# 
# 输入: dividend = 10, divisor = 3
# 输出: 3
# 解释: 10/3 = 3.33333.. ，向零截断后得到 3 。
# 
# 示例 2:
# 
# 输入: dividend = 7, divisor = -3
# 输出: -2
# 解释: 7/-3 = -2.33333.. ，向零截断后得到 -2 。
# 
# 
# 
# 提示：
# 
# 
# -2^31 <= dividend, divisor <= 2^31 - 1
# divisor != 0
# 
# 
#


# @lcpr-template-start
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush
# @lcpr-template-end
# @lc code=start
class Solution:
    def divide1(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        a, b, res = abs(dividend), abs(divisor), 0
        for i in range(31, -1, -1):
            # 令 a = dividend, b = divisor
            # 1.先以 10 进制为例进行理解：
            # sum = b * 10^k1 + b * 10^k2 + ... + b * 10^kn, sum <= a
            # remainder = a - sum, remainder < b, 故 remainder / b < 1
            # 故有 quotient = 10^k1 + 10^k2 + ... + 10^kn
            # 2.以 2 进制理解
            # sum = b * 2^k1 + b * 2^k2 + ... + 2 * 10^kn, sum <= a， k1,...,kn > 0
            # remainder = a - sum, remainder < b, 故 remainder / b < 1
            # 故有 quotient = 2^k1 + 2^k2 + ... + 2^kn
            # 3.之所以这里用 2 进制，是因为计算机存储是二进制的，如果用其他进制，则需要乘除法，
            # 但题目规定不能用乘除法，因此需要基于二进制本身进行处理，而二进制的移位操作对应
            # 的即为乘除法
            if (b << i) <= a:
                res += 1 << i
                a -= b << i
        return res if (dividend > 0) == (divisor > 0) else -res
    
    def divide2(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

        if dividend == 0:
            return 0
        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        if divisor == INT_MIN:
            return 1 if dividend == INT_MIN else 0

        return res

    def divide(self, dividend: int, divisor: int) -> int:
        return self.divide1(dividend, divisor)
# @lc code=end

tests = [[10, 3], [7, -3]]
ans = [3, -2]
for i,(t,a) in enumerate(zip(tests, ans)):
    res = Solution().divide(t[0],t[1])
    print(f"test case {i + 1}:\n"
          f"\ttest = {t[0]}, {t[1]};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# 10\n3\n
# @lcpr case=end

# @lcpr case=start
# 7\n-3\n
# @lcpr case=end

#

