#
# @lc app=leetcode.cn id=236 lang=python3
# @lcpr version=30204
#
# [236] 二叉树的最近公共祖先
#
# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (71.68%)
# Likes:    2782
# Dislikes: 0
# Total Accepted:    787.1K
# Total Submissions: 1.1M
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x
# 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#
#
#
# 示例 1：
#
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出：3
# 解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
#
#
# 示例 2：
#
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出：5
# 解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
#
#
# 示例 3：
#
# 输入：root = [1,2], p = 1, q = 2
# 输出：1
#
#
#
#
# 提示：
#
#
# 树中节点数目在范围 [2, 10^5] 内。
# -10^9 <= Node.val <= 10^9
# 所有 Node.val 互不相同 。
# p != q
# p 和 q 均存在于给定的二叉树中。
#
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

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':

        # 思想：如果左边和右边返回不为空，说明分别找到了p和q，此时的root必然是最近的父节点；
        #      反之，如果其中一个未空，那么不为空那个必然是最近的父节点；
        if root is None or root == p or root == q:
            return root

        left_root = self.lowestCommonAncestor(root.left, p, q)
        right_root = self.lowestCommonAncestor(root.right, p, q)

        if left_root is not None and right_root is not None:
            return root

        if left_root is not None:
            return left_root

        return right_root


# @lc code=end

#
# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n5\n1\n
# @lcpr case=end

# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n5\n4\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n2\n
# @lcpr case=end

#
