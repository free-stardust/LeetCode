#
# @lc app=leetcode.cn id=38 lang=python3
# @lcpr version=30204
#
# [38] 外观数列
#
# https://leetcode.cn/problems/count-and-say/description/
#
# algorithms
# Medium (60.98%)
# Likes:    1089
# Dislikes: 0
# Total Accepted:    373.4K
# Total Submissions: 612.2K
# Testcase Example:  '1'
#
# 「外观数列」是一个数位字符串序列，由递归公式定义：
# 
# 
# countAndSay(1) = "1"
# countAndSay(n) 是 countAndSay(n-1) 的行程长度编码。
# 
# 
# 
# 
# 
# 
# 
# 
# 行程长度编码（RLE）是一种字符串压缩方法，其工作原理是通过将连续相同字符（重复两次或更多次）替换为字符重复次数（运行长度）和字符的串联。例如，要压缩字符串
# "3322251" ，我们将 "33" 用 "23" 替换，将 "222" 用 "32" 替换，将 "5" 用 "15" 替换并将 "1" 用 "11"
# 替换。因此压缩后字符串变为 "23321511"。
# 
# 给定一个整数 n ，返回 外观数列 的第 n 个元素。
# 
# 示例 1：
# 
# 
# 输入：n = 4
# 
# 输出："1211"
# 
# 解释：
# 
# countAndSay(1) = "1"
# 
# countAndSay(2) = "1" 的行程长度编码 = "11"
# 
# countAndSay(3) = "11" 的行程长度编码 = "21"
# 
# countAndSay(4) = "21" 的行程长度编码 = "1211"
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 
# 输出："1"
# 
# 解释：
# 
# 这是基本情况。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 30
# 
# 
# 
# 进阶：你能迭代解决该问题吗？
#


# @lcpr-template-start
import copy
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush
# @lcpr-template-end
# @lc code=start
class Solution:
    def dp1(self, n: int) -> str:
        s = ["1"]
        
        for i in range(1, n):
            count = 0
            next_s = ""
            tmp_s = s[i-1][0]
            for _s in s[i-1]:
                if tmp_s == _s:
                    count += 1
                else:
                    next_s += str(count) + tmp_s
                    count = 1
                    tmp_s = _s
            next_s += str(count) + tmp_s
            s.append(next_s)
        
        return s[n-1]
    
    def recursion1(self, n: int) -> str:
        if n == 1:
            return "1"
        
        last_s = self.recursion1(n-1)
        s = ""
        count = 0
        tmp_s = last_s[0]
        for _s in last_s:
            if tmp_s == _s:
                count += 1
            else:
                s += str(count) + tmp_s
                tmp_s = _s
                count = 1
        
        s += str(count) + tmp_s

        return s

    def countAndSay(self, n: int) -> str:
        # return self.dp1(n)
        return self.recursion1(n)
# @lc code=end

tests =[4, 1]
ans = ["1211", "1"]
for i,(t,a) in enumerate(zip(tests, ans)):
    res = Solution().countAndSay(t)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = \"{a}\"\n"
          f"\tres = \"{res}\"\n"
          f"\t{a == res}.")
#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

