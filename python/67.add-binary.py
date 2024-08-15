#
# @lc app=leetcode.cn id=67 lang=python3
# @lcpr version=30204
#
# [67] 二进制求和
#
# https://leetcode.cn/problems/add-binary/description/
#
# algorithms
# Easy (53.26%)
# Likes:    1222
# Dislikes: 0
# Total Accepted:    413.3K
# Total Submissions: 775.5K
# Testcase Example:  '"11"\n"1"'
#
# 给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。
#
#
#
# 示例 1：
#
# 输入:a = "11", b = "1"
# 输出："100"
#
# 示例 2：
#
# 输入：a = "1010", b = "1011"
# 输出："10101"
#
#
#
# 提示：
#
#
# 1 <= a.length, b.length <= 10^4
# a 和 b 仅由字符 '0' 或 '1' 组成
# 字符串如果不是 "0" ，就不含前导零
#
#
#

# @lcpr-template-start
import copy
import collections
import random
from collections import namedtuple
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush


# @lcpr-template-end
# @lc code=start
class Solution:

    def solution1(self, a: str, b: str) -> str:
        return "{0:b}".format(int(a, 2) + int(b, 2))

    def simulation(self, a: str, b: str) -> str:
        ans = ""

        a, b = a[::-1], b[::-1]

        n = max(len(a), len(b))
        carry = 0

        for i in range(n):
            carry += a[i] == '1' if i < len(a) else 0
            carry += b[i] == '1' if i < len(b) else 0
            ans += '1' if carry % 2 == 1 else '0'
            carry //= 2

        if carry != 0:
            ans += '1'

        ans = ans[::-1]

        return ans
    
    def bit_solution(self, a: str, b: str) -> str:
        x, y = int(a,2), int(b,2)
        
        while y:
            ans = x ^ y
            carry = (x & y) << 1
            x, y = ans, carry
        
        return bin(x)[2:]

    def addBinary(self, a: str, b: str) -> str:
        # return self.solution1(a, b)
        # return self.simulation(a, b)
        return self.bit_solution(a, b)


# @lc code=end

tests = [["11", "1"], ["1010", "1011"]]
ans = ["100", "10101"]
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().addBinary(t[0], t[1])
    print(f"test case {i+1}:\n"
          f"\ttest = \"{t[0]}\", \"{t[1]}\":\n"
          f"\tans = \"{a}\";\n"
          f"\tres = \"{res}\";\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# "11"\n"1"\n
# @lcpr case=end

# @lcpr case=start
# "1010"\n"1011"\n
# @lcpr case=end

#
