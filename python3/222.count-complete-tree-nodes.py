#
# @lc app=leetcode.cn id=222 lang=python3
# @lcpr version=30204
#
# [222] 完全二叉树的节点个数
#
# https://leetcode.cn/problems/count-complete-tree-nodes/description/
#
# algorithms
# Easy (82.02%)
# Likes:    1177
# Dislikes: 0
# Total Accepted:    434.8K
# Total Submissions: 530.1K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# 给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。
#
# 完全二叉树
# 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h
# 层，则该层包含 1~ 2^h 个节点。
#
#
#
# 示例 1：
#
# 输入：root = [1,2,3,4,5,6]
# 输出：6
#
#
# 示例 2：
#
# 输入：root = []
# 输出：0
#
#
# 示例 3：
#
# 输入：root = [1]
# 输出：1
#
#
#
#
# 提示：
#
#
# 树中节点的数目范围是[0, 5 * 10^4]
# 0 <= Node.val <= 5 * 10^4
# 题目数据保证输入的树是 完全二叉树
#
#
#
#
# 进阶：遍历树来统计节点是一种时间复杂度为 O(n) 的简单解决方案。你可以设计一个更快的算法吗？
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

    def recursion(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_count = self.countNodes(root.left)
        right_count = self.countNodes(root.right)

        return left_count + right_count + 1

    def official(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def exists(node: Optional[TreeNode], level: int, k: int) -> bool:
            bits = 1 << (level - 1)
            while node and bits > 0:
                if not (bits & k):
                    node = node.left
                else:
                    node = node.right
                bits >>= 1
                # print(bits)
            return node != None

        level = 0
        node = root
        while node.left:
            level += 1
            node = node.left

        low, high = 1 << level, (1 << (level + 1)) - 1
        while low < high:
            mid = low + (high - low + 1) // 2
            if exists(root, level, mid):
                low = mid
            else:
                high = mid - 1

        return low

    def countNodes(self, root: Optional[TreeNode]) -> int:
        # return self.recursion(root)
        return self.official(root)


# @lc code=end

#
# @lcpr case=start
# [1,2,3,4,5,6]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#
