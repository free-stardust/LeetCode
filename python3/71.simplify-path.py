#
# @lc app=leetcode.cn id=71 lang=python3
# @lcpr version=30204
#
# [71] 简化路径
#
# https://leetcode.cn/problems/simplify-path/description/
#
# algorithms
# Medium (45.64%)
# Likes:    740
# Dislikes: 0
# Total Accepted:    248K
# Total Submissions: 542.5K
# Testcase Example:  '"/home/"'
#
# 给你一个字符串 path ，表示指向某一文件或目录的 Unix 风格 绝对路径 （以 '/' 开头），请你将其转化为更加简洁的规范路径。
# 
# 在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..）
# 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。任意多个连续的斜杠（即，'//'）都被视为单个斜杠 '/' 。
# 对于此问题，任何其他格式的点（例如，'...'）均被视为文件/目录名称。
# 
# 请注意，返回的 规范路径 必须遵循下述格式：
# 
# 
# 始终以斜杠 '/' 开头。
# 两个目录名之间必须只有一个斜杠 '/' 。
# 最后一个目录名（如果存在）不能 以 '/' 结尾。
# 此外，路径仅包含从根目录到目标文件或目录的路径上的目录（即，不含 '.' 或 '..'）。
# 
# 
# 返回简化后得到的 规范路径 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：path = "/home/"
# 
# 输出："/home"
# 
# 解释：
# 
# 应删除尾部斜杠。
# 
# 
# 示例 2：
# 
# 
# 输入：path = "/home//foo/"
# 
# 输出："/home/foo"
# 
# 解释：
# 
# 多个连续的斜杠被单个斜杠替换。
# 
# 
# 示例 3：
# 
# 
# 输入：path = "/home/user/Documents/../Pictures"
# 
# 输出："/home/user/Pictures"
# 
# 解释：
# 
# 两个点 ".." 表示上一级目录。
# 
# 
# 示例 4：
# 
# 
# 输入：path = "/../"
# 
# 输出："/"
# 
# 解释：
# 
# 不可能从根目录上升级一级。
# 
# 
# 示例 5：
# 
# 
# 输入：path = "/.../a/../b/c/../d/./"
# 
# 输出："/.../b/d"
# 
# 解释：
# 
# "..." 是此问题中目录的有效名称。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= path.length <= 3000
# path 由英文字母，数字，'.'，'/' 或 '_' 组成。
# path 是一个有效的 Unix 风格绝对路径。
# 
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
    def simplifyPath(self, path: str) -> str:
        stack = []

        names = path.split("/")

        for name in names:
            if name == "..":
                if stack:
                    stack.pop()
            elif name and name != ".":
                stack.append(name)

        return "/" + "/".join(stack)
# @lc code=end

tests = ["/home/", "/home//foo/", "/home/user/Documents/../Pictures", "/../",
         "/.../a/../b/c/../d/./"]
ans = ["/home", "/home/foo", "/home/user/Pictures", "/", "/.../b/d"]
for i,(t,a) in enumerate(zip(tests, ans)):
    res = Solution().simplifyPath(t)
    print(f"test case {i+1}:\n"
          f"\ttest = \"{t}\";\n"
          f"\tans = \"{a}\";\n"
          f"\tres = \"{res}\";\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# "/home/"\n
# @lcpr case=end

# @lcpr case=start
# "/home//foo/"\n
# @lcpr case=end

# @lcpr case=start
# "/home/user/Documents/../Pictures"\n
# @lcpr case=end

# @lcpr case=start
# "/../"\n
# @lcpr case=end

# @lcpr case=start
# "/.../a/../b/c/../d/./"\n
# @lcpr case=end

#

