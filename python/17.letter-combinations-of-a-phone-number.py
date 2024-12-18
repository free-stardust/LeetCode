#
# @lc app=leetcode.cn id=17 lang=python3
# @lcpr version=30204
#
# [17] 电话号码的字母组合
#
# https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (60.17%)
# Likes:    2867
# Dislikes: 0
# Total Accepted:    922.6K
# Total Submissions: 1.5M
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
#
#
#
#
# 示例 1：
#
# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
#
# 示例 2：
#
# 输入：digits = ""
# 输出：[]
#
#
# 示例 3：
#
# 输入：digits = "2"
# 输出：["a","b","c"]
#
#
#
#
# 提示：
#
#
# 0 <= digits.length <= 4
# digits[i] 是范围 ['2', '9'] 的一个数字。
#
#
#

# @lcpr-template-start
from typing import List, Tuple
from typing import Optional

from torch import le


# @lcpr-template-end
# @lc code=start
class Solution:

    def letterCombinations1(self, digits: str) -> List[str]:
        MAPPING = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        n = len(digits)
        if n == 0:
            return []
        ans = []
        path = [''] * n  # 本题 path 长度固定为 n

        def dfs(i: int) -> None:
            if i == n:
                ans.append(''.join(path))
                return
            for c in MAPPING[int(digits[i])]:
                path[i] = c  # 直接覆盖
                dfs(i + 1)

        dfs(0)
        return ans

    def letterCombinations2(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        letter_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans = []
        digits_len = len(digits)
        index = [0 for _ in range(digits_len)]

        def backtrack(index):
            for i in reversed(range(1, digits_len)):
                if index[i] == len(letter_dict[digits[i]]):
                    index[i - 1] += 1
                    index[i] = 0

        while index[0] < len(letter_dict[digits[0]]):
            tmp_ans = ""
            for j in range(digits_len):
                letters = letter_dict[digits[j]]
                if index[j] < len(letters):
                    tmp_ans += letters[index[j]]
                    index[j] = index[j] + 1 if j == digits_len - 1 else index[j]
                if j == digits_len - 1 and index[j] == len(letters):
                    backtrack(index)
            ans.append(tmp_ans)
        return ans

    def letterCombinations(self, digits: str) -> List[str]:
        return self.letterCombinations1(digits)
        # return self.letterCombinations2(digits)


# @lc code=end

strs = ["23", "", "2", "9", "234"]
ans = [["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], [],
       ["a", "b", "c"], ["w", "x", "y", "z"], []]
for s, a in zip(strs, ans):
    res = Solution().letterCombinations1(s)
    print(f"s = \"{s}\": \n\tans = {a};\n\tres = {res};\n\t{a == res}.")

#
# @lcpr case=start
# "23"\n
# @lcpr case=end

# @lcpr case=start
# ""\n
# @lcpr case=end

# @lcpr case=start
# "2"\n
# @lcpr case=end

#
