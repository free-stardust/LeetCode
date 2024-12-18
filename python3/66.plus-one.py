#
# @lc app=leetcode.cn id=66 lang=python3
# @lcpr version=30204
#
# [66] 加一
#
# https://leetcode.cn/problems/plus-one/description/
#
# algorithms
# Easy (46.00%)
# Likes:    1421
# Dislikes: 0
# Total Accepted:    767.1K
# Total Submissions: 1.7M
# Testcase Example:  '[1,2,3]'
#
# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
# 
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
# 
# 
# 
# 示例 1：
# 
# 输入：digits = [1,2,3]
# 输出：[1,2,4]
# 解释：输入数组表示数字 123。
# 
# 
# 示例 2：
# 
# 输入：digits = [4,3,2,1]
# 输出：[4,3,2,2]
# 解释：输入数组表示数字 4321。
# 
# 
# 示例 3：
# 
# 输入：digits = [0]
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
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
    def solution1(self, digits: List[int]) -> List[int]:
        carry = 0
        ans = []

        for i in range(len(digits) - 1, -1, -1):
            tmp_sum = carry + digits[i]
            tmp_sum += 1 if i == len(digits) - 1 else 0
            if tmp_sum > 9:
                carry = 1
                ans.append(0)
            else:
                carry = 0
                ans.append(tmp_sum)

        if carry != 0:
            ans = ans + [carry]
        
        for i in range(len(ans) // 2):
            ans[i], ans[len(ans) - 1 - i] = ans[len(ans) - 1 - i], ans[i]

        return ans
    
    def solution2(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                for j in range(i + 1, n):
                    digits[j] = 0
                return digits

        return [1] + [0] * n

    def plusOne(self, digits: List[int]) -> List[int]:
        # return self.solution1(digits)
        return self.solution2(digits)
# @lc code=end

tests = [[1,2,3], [4,3,2,1], [0], [8,9,9,9]]
ans = [[1,2,4], [4,3,2,2], [1], [9,0,0,0]]

for i,(t,a) in enumerate(zip(tests,ans)):
    res = Solution().plusOne(t)
    print(f"test case {i + 1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [4,3,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

