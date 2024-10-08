#
# @lc app=leetcode.cn id=98 lang=python3
# @lcpr version=30204
#
# [98] 验证二叉搜索树
#
# https://leetcode.cn/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (38.20%)
# Likes:    2393
# Dislikes: 0
# Total Accepted:    969.9K
# Total Submissions: 2.5M
# Testcase Example:  '[2,1,3]'
#
# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
#
# 有效 二叉搜索树定义如下：
#
#
# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
#
#
#
#
# 示例 1：
#
# 输入：root = [2,1,3]
# 输出：true
#
#
# 示例 2：
#
# 输入：root = [5,1,4,null,null,3,6]
# 输出：false
# 解释：根节点的值是 5 ，但是右子节点的值是 4 。
#
#
#
#
# 提示：
#
#
# 树中节点数目范围在[1, 10^4] 内
# -2^31 <= Node.val <= 2^31 - 1
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
# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def recursion(self, root: Optional[TreeNode]) -> bool:

        def check(node, lower=float('-inf'), upper=float('inf')) -> bool:
            if not node:
                return True

            if node.val <= lower or node.val >= upper:
                return False

            if not check(node.left, lower, node.val):
                return False

            if not check(node.right, node.val, upper):
                return False

            return True

        return check(root)

    def traverse(self, root: Optional[TreeNode]) -> bool:
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            if root.val <= inorder:
                return False

            inorder = root.val
            root = root.right

        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # return self.recursion(root)
        return self.traverse(root)


# @lc code=end


def build_tree_form_list(l: List[int], index=0) -> Optional[TreeNode]:
    if len(l) == 0 or index >= len(l):
        return None

    root = TreeNode(l[index])
    root.left = build_tree_form_list(l, 2 * index + 1)
    root.right = build_tree_form_list(l, 2 * index + 2)

    return root


tests = [[2, 1, 3], [5, 1, 4, float('-inf'),
                     float('-inf'), 3, 6], [2, 2, 2],
         [5, 4, 6, float('-inf'), float('-inf'), 3, 7]]
ans = [True, False, False, False]
for i, (t, a) in enumerate(zip(tests, ans)):
    root = build_tree_form_list(t)
    res = Solution().isValidBST(root)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,4,null,null,3,6]\n
# @lcpr case=end

#
