#
# @lc app=leetcode.cn id=97 lang=python3
# @lcpr version=30204
#
# [97] 交错字符串
#
# https://leetcode.cn/problems/interleaving-string/description/
#
# algorithms
# Medium (45.08%)
# Likes:    1026
# Dislikes: 0
# Total Accepted:    157.3K
# Total Submissions: 348.5K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# 给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。
#
# 两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：
#
#
# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# 交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
#
#
# 注意：a + b 意味着字符串 a 和 b 连接。
#
#
#
# 示例 1：
#
# 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 输出：true
#
#
# 示例 2：
#
# 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 输出：false
#
#
# 示例 3：
#
# 输入：s1 = "", s2 = "", s3 = ""
# 输出：true
#
#
#
#
# 提示：
#
#
# 0 <= s1.length, s2.length <= 100
# 0 <= s3.length <= 200
# s1、s2、和 s3 都由小写英文字母组成
#
#
#
#
# 进阶：您能否仅使用 O(s2.length) 额外的内存空间来解决它?
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

    def dp1(self, s1: str, s2: str, s3: str) -> bool:
        len1, len2, len3 = len(s1), len(s2), len(s3)

        if len1 + len2 != len3:
            return False

        f = [[False] * (len2 + 1) for _ in range(len1 + 1)]
        f[0][0] = True

        for i in range(len1 + 1):
            for j in range(len2 + 1):
                p = i + j - 1
                if i > 0:
                    f[i][j] |= (f[i - 1][j] and s1[i - 1] == s3[p])
                if j > 0:
                    f[i][j] |= (f[i][j - 1] and s2[j - 1] == s3[p])

        return f[len1][len2]

    def dp2(self, s1: str, s2: str, s3: str) -> bool:
        len1, len2, len3 = len(s1), len(s2), len(s3)

        if len1 + len2 != len3:
            return False

        # 这里之所以可以压缩成和一行，是因为把上一行的结果继承了下来，所以叫滚动数组
        f = [False] * (len2 + 1)
        f[0] = True

        for i in range(len1 + 1):
            for j in range(len2 + 1):
                p = i + j - 1
                if i > 0:
                    f[j] &= s1[i - 1] == s3[p]
                if j > 0:
                    f[j] |= (f[j - 1] and s2[j - 1] == s3[p])

        return f[len2]

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # return self.dp1(s1, s2, s3)
        return self.dp2(s1, s2, s3)


# @lc code=end

tests = [["aabcc", "dbbca", "aadbbcbcac"], ["aabcc", "dbbca", "aadbbbaccc"],
         ["", "", ""]]
ans = [True, False, True]
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().isInterleave(t[0], t[1], t[2])
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# "aabcc"\n"dbbca"\n"aadbbcbcac"\n
# @lcpr case=end

# @lcpr case=start
# "aabcc"\n"dbbca"\n"aadbbbaccc"\n
# @lcpr case=end

# @lcpr case=start
# ""\n""\n""\n
# @lcpr case=end

#
