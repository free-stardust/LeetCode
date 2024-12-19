#
# @lc app=leetcode.cn id=530 lang=python3
# @lcpr version=30204
#
# [530] 二叉搜索树的最小绝对差
#
# https://leetcode.cn/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (62.90%)
# Likes:    596
# Dislikes: 0
# Total Accepted:    291.6K
# Total Submissions: 463.6K
# Testcase Example:  '[4,2,6,1,3]'
#
# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
#
# 差值是一个正数，其数值等于两值之差的绝对值。
#
#
#
# 示例 1：
#
# 输入：root = [4,2,6,1,3]
# 输出：1
#
#
# 示例 2：
#
# 输入：root = [1,0,48,null,null,12,49]
# 输出：1
#
#
#
#
# 提示：
#
#
# 树中节点的数目范围是 [2, 10^4]
# 0 <= Node.val <= 10^5
#
#
#
#
# 注意：本题与 783
# https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同
#
#

# @lcpr-template-start
import copy
import collections
import random
import math
from functools import reduce
from collections import namedtuple
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush


# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def bfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ls_val = []
        q = [root]
        while q:
            node = q.pop()
            ls_val.append(node.val)
            if node and node.left:
                q.append(node.left)
            if node and node.right:
                q.append(node.right)
        ls_val.sort()
        for i in range(len(ls_val) - 1):
            ls_val[i] = abs(ls_val[i] - ls_val[i + 1])
        return min(ls_val)

    def copilot_solution(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if not root:
                return []
            return dfs(root.left) + [root.val] + dfs(root.right)

        ls = dfs(root)
        return min(abs(ls[i] - ls[i + 1]) for i in range(len(ls) - 1))

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        return self.copilot_solution(root)


# @lc code=end


def build_tree_from_list(l, index=0) -> Optional[TreeNode]:
    if index >= len(l) or l[index] is None:
        return None
    root = TreeNode(l[index])
    root.left = build_tree_from_list(l, index * 2 + 1)
    root.right = build_tree_from_list(l, index * 2 + 2)
    return root


def build_list_from_tree(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    ls = []
    q = [root]
    while q:
        node = q.pop()
        ls.append(node.val)
        q.append(node.left if node else None)
        q.append(node.right if node else None)
    return ls


tests = [[4, 2, 6, 1, 3], [1, 0, 48, None, None, 12, 49]]
ans = [1, 1]
all_pass = True
for i, (t, a) in enumerate(zip(tests, ans)):
    root = build_tree_from_list(t)
    res = Solution().getMinimumDifference(root)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")
    all_pass &= (a == res)
print(f"all pass: {all_pass}.")

#
# @lcpr case=start
# [4,2,6,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,48,null,null,12,49]\n
# @lcpr case=end

#
