#
# @lc app=leetcode.cn id=22 lang=python3
# @lcpr version=30204
#
# [22] 括号生成
#
# https://leetcode.cn/problems/generate-parentheses/description/
#
# algorithms
# Medium (77.91%)
# Likes:    3649
# Dislikes: 0
# Total Accepted:    880.2K
# Total Submissions: 1.1M
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
#
# 示例 1：
#
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
#
#
# 示例 2：
#
# 输入：n = 1
# 输出：["()"]
#
#
#
#
# 提示：
#
#
# 1 <= n <= 8
#
#
#

# @lcpr-template-start
from typing import List, Tuple
from typing import Optional


# @lcpr-template-end
# @lc code=start
class Solution:

    def recursion1(self, n: int) -> List[str]:
        if n == 0:
            return []

        ans = []

        def dfs(ans, s, left, right) -> None:
            # 如果左右括号都用完，直接返回
            if left == 0 and right == 0:
                ans.append(s)
                return

            if left == right:  # s 中左括号等于右括号，后续只能用左括号
                dfs(ans, s + "(", left - 1, right)
            else:  # 由于一旦两者相等，先用左括号，所以，必定有 left < right，故使用左右括号都可
                if left > 0:
                    dfs(ans, s + "(", left - 1, right)
                dfs(ans, s + ")", left, right - 1)

        dfs(ans, "", n, n)

        return ans

    def recursion2(self, n: int) -> List[str]:
        if n == 0:
            return [""]

        ans = []

        for c in range(n):
            for left in self.recursion2(c):
                for right in self.recursion2(n - 1 - c):
                    ans.append(f"({left}){right}")
        return ans

    def recursion3(self, n: int) -> List[str]:
        m = n * 2  # 括号长度
        ans = []
        path = [''] * m  # 所有括号长度都是一样的 m

        # i = 目前填了多少个括号
        # open = 左括号个数，i-open = 右括号个数
        def dfs(i: int, open: int) -> None:
            if i == m:  # 括号构造完毕
                ans.append(''.join(path))  # 加入答案
                return
            if open < n:  # 可以填左括号
                path[i] = '('  # 直接覆盖
                dfs(i + 1, open + 1)  # 多了一个左括号
            if i - open < open:  # 可以填右括号
                path[i] = ')'  # 直接覆盖
                dfs(i + 1, open)

        dfs(0, 0)
        return ans

    def backtrace(self, n: int) -> List[str]:
        ans = []

        def backtrace(s, left, right) -> None:
            if len(s) == 2 * n:
                ans.append(''.join(s))
                return

            # 这个代码里面的 append 和 pop 的作用是为了不断地迭代，所以需要添加和置空
            # 这个代码之所以能穷举最多的可能，主要是因为本来就只有两种情况，一种左括号，一
            # 种右括号，通过二叉树就可以穷举，所以实际还是一个 dfs

            if left < n:
                s.append("(")
                backtrace(s, left + 1, right)
                s.pop()

            if left > right:
                s.append(")")
                backtrace(s, left, right + 1)
                s.pop()

        backtrace([], 0, 0)

        return ans

    def dynamic_programing(self, n: int) -> List[str]:
        if n == 0:
            return []
        total_l = []
        total_l.append([None])  # 0组括号时记为None
        total_l.append(["()"])  # 1组括号只有一种情况
        for i in range(2, n + 1):  # 开始计算i组括号时的括号组合
            l = []
            for j in range(i):  # 开始遍历 p q ，其中p+q=i-1 , j 作为索引
                now_list1 = total_l[j]  # p = j 时的括号组合情况
                now_list2 = total_l[i - 1 - j]  # q = (i-1) - j 时的括号组合情况
                for k1 in now_list1:
                    for k2 in now_list2:
                        if k1 == None:
                            k1 = ""
                        if k2 == None:
                            k2 = ""
                        el = "(" + k1 + ")" + k2
                        l.append(el)  # 把所有可能的情况添加到 l 中
            total_l.append(l)  # l这个list就是i组括号的所有情况，添加到total_l中，继续求解i=i+1的情况
        return total_l[n]

    def generateParenthesis(self, n: int) -> List[str]:
        # return self.recursion1(n)
        # return self.recursion2(n)
        # return self.backtrace(n)
        return self.dynamic_programing(n)


# @lc code=end

tests = [3, 1]
ans = [["((()))", "(()())", "(())()", "()(())", "()()()"], ["()"]]
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().generateParenthesis(t)
    print(f"test case {i+1}:\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")
#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#
