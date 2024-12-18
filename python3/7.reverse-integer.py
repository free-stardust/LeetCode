#
# @lc app=leetcode.cn id=7 lang=python3
# @lcpr version=30204
#
# [7] 整数反转
#
# https://leetcode.cn/problems/reverse-integer/description/
#
# algorithms
# Medium (35.54%)
# Likes:    4008
# Dislikes: 0
# Total Accepted:    1.3M
# Total Submissions: 3.7M
# Testcase Example:  '123'
#
# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
# 
# 如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 − 1] ，就返回 0。
# 假设环境不允许存储 64 位整数（有符号或无符号）。
# 
# 
# 
# 示例 1：
# 
# 输入：x = 123
# 输出：321
# 
# 
# 示例 2：
# 
# 输入：x = -123
# 输出：-321
# 
# 
# 示例 3：
# 
# 输入：x = 120
# 输出：21
# 
# 
# 示例 4：
# 
# 输入：x = 0
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# -2^31 <= x <= 2^31 - 1
# 
# 
#


# @lcpr-template-start
from typing import List, Tuple
from typing import Optional
# @lcpr-template-end
# @lc code=start
class Solution:
    def reverseByStr(sefl, x:int) -> int:
        sign = -1 if x < 0 else 1
        x = x * sign
        s_str = str(x)
        ans = int("".join(reversed(s_str))) * sign

        if ans < -(2 ** 31) or ans > (2 ** 31 - 1):
            return 0
        else:
            return ans
        
    def realSolution(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        rev = 0
        while x != 0:     
            # 这个提前检查不完全，最后加上去那个数的大小也会影响 
            # if rev < INT_MIN // 10 + 1 or rev > INT_MAX // 10:
            #     return 0

            digit = x % 10
            # Python3 的取模运算在 x 为负数时也会返回 [0, 9) 以内的结果，因此这里需要进行特殊判断
            if x < 0 and digit > 0:
                digit -= 10

            if rev < INT_MIN // 10 + 1 or (rev == INT_MAX // 10 + 1 and digit > 8):
                return 0
            elif rev > INT_MAX // 10 or (rev == INT_MAX // 10 and digit > 7):
                return 0

            # 同理，Python3 的整数除法在 x 为负数时会向下（更小的负数）取整，因此不能写成 x //= 10
            x = (x - digit) // 10
            rev = rev * 10 + digit

            # if rev < INT_MIN or rev > INT_MAX:
            #     return 0
        
        return rev

    def reverse(self, x: int) -> int:
        # return self.reverseByStr(x)
        return self.realSolution(x)
# @lc code=end

nums = [123, -123, 120, 1534236469, -8463847412, 8463847412, -2147483648, 2147483647]
for num in nums:
    ans = Solution().reverse(num)
    print(f"num = {num}, ans = {ans}.")

#
# @lcpr case=start
# 123\n
# @lcpr case=end

# @lcpr case=start
# -123\n
# @lcpr case=end

# @lcpr case=start
# 120\n
# @lcpr case=end

# @lcpr case=start
# 0\n
# @lcpr case=end

#

