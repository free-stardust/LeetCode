#
# @lc app=leetcode.cn id=6 lang=python3
# @lcpr version=30204
#
# [6] Z 字形变换
#
# https://leetcode.cn/problems/zigzag-conversion/description/
#
# algorithms
# Medium (52.83%)
# Likes:    2322
# Dislikes: 0
# Total Accepted:    684.1K
# Total Submissions: 1.3M
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
#
# 比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
#
# 请你实现这个将字符串进行指定行数变换的函数：
#
# string convert(string s, int numRows);
#
#
#
# 示例 1：
#
# 输入：s = "PAYPALISHIRING", numRows = 3
# 输出："PAHNAPLSIIGYIR"
#
# 示例 2：
#
# 输入：s = "PAYPALISHIRING", numRows = 4
# 输出："PINALSIGYAHRPI"
# 解释：
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
#
#
# 示例 3：
#
# 输入：s = "A", numRows = 1
# 输出："A"
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 1000
# s 由英文字母（小写和大写）、',' 和 '.' 组成
# 1 <= numRows <= 1000
#
#
#

# @lcpr-template-start
from typing import List, Tuple
from typing import Optional
from unittest import result


# @lcpr-template-end
# @lc code=start
class Solution:

    def splice(self, s: str, numRows: int) -> str:
        s_len = len(s)
        if numRows < 2 or numRows >= s_len:
            return s
        ans = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            ans[i] += c
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        return "".join(ans)

    def mapping(self, s: str, numRows: int) -> str:
        s_len = len(s)
        if numRows < 2 or numRows >= s_len:
            return s
        ans = ""
        step = 2 * (numRows - 1)
        for i in range(numRows):
            for j in range(0, s_len - i, step):
                ans += s[i + j]
                if 0 < i < numRows - 1 and j + step - i < s_len:
                    # 这里之所以是 j + step - i，可以基于第一行内容的偏移来理解，
                    # j 由于是初始行的索引，然后如果不基于 i 进行偏移，那就从第一行开始，
                    # 然后第二个元素，就是需要 j 前进一个周期，然后减去当前周期的位置，即
                    # 为第二个元素
                    ans += s[j + step - i]
        return ans

    def convert(self, s: str, numRows: int) -> str:
        # return self.splice(s, numRows)
        return self.mapping(s, numRows)


# @lc code=end

strs = [["PAYPALISHIRING", 3], ["PAYPALISHIRING", 4], ["A", 1]]
ans = ["PAHNAPLSIIGYIR", "PINALSIGYAHRPI", "A"]
for s, a in zip(strs, ans):
    result = Solution().convert(s[0], s[1])
    judge_result = result == a
    print(
        f"s = \"{s[0]}\", rows = {s[1]}, result = \"{result}\", {judge_result}."
    )
#
# @lcpr case=start
# "PAYPALISHIRING"\n3\n
# @lcpr case=end

# @lcpr case=start
# "PAYPALISHIRING"\n4\n
# @lcpr case=end

# @lcpr case=start
# "A"\n1\n
# @lcpr case=end

#
