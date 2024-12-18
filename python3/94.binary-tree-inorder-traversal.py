#
# @lc app=leetcode.cn id=94 lang=python3
# @lcpr version=30204
#
# [94] 二叉树的中序遍历
#
# https://leetcode.cn/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Easy (77.06%)
# Likes:    2134
# Dislikes: 0
# Total Accepted:    1.6M
# Total Submissions: 2M
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
#
#
#
# 示例 1：
#
# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
#
#
# 示例 2：
#
# 输入：root = []
# 输出：[]
#
#
# 示例 3：
#
# 输入：root = [1]
# 输出：[1]
#
#
#
#
# 提示：
#
#
# 树中节点数目在范围 [0, 100] 内
# -100 <= Node.val <= 100
#
#
#
#
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
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

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return

            dfs(node.left)
            ans.append(node.val) if node else None
            dfs(node.right)

        dfs(root)

        return ans


# @lc code=end


def build_tree_from_list(l: List[int]) -> Optional[TreeNode]:
    if not l:
        return None

    root = TreeNode(l[0])
    queue = [root]
    index = 1

    while queue and index < len(l):
        cur_node = queue.pop()

        if index < len(l) and l[index] is not None:
            cur_node.left = TreeNode(l[index])
            queue.append(cur_node.left)
        index += 1

        if index < len(l) and l[index] is not None:
            cur_node.right = TreeNode(l[index])
            queue.append(cur_node.right)
        index += 1

    return root


tests = [[1, None, 2, 3], [], [1]]
ans = [[1, 3, 2], [], [1]]
all_pass = True
for i, (t, a) in enumerate(zip(tests, ans)):
    root = build_tree_from_list(t)
    res = Solution().inorderTraversal(root)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res};")
    all_pass &= (a == res)
print(f"all pass: {all_pass}.")

#
# @lcpr case=start
# [1,null,2,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#
