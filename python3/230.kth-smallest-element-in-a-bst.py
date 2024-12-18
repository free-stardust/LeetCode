#
# @lc app=leetcode.cn id=230 lang=python3
# @lcpr version=30204
#
# [230] 二叉搜索树中第K小的元素
#
# https://leetcode.cn/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (77.77%)
# Likes:    902
# Dislikes: 0
# Total Accepted:    414.6K
# Total Submissions: 531.1K
# Testcase Example:  '[3,1,4,null,2]\n1'
#
# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 小的元素（从 1 开始计数）。
#
#
#
# 示例 1：
#
# 输入：root = [3,1,4,null,2], k = 1
# 输出：1
#
#
# 示例 2：
#
# 输入：root = [5,3,6,2,4,null,null,1], k = 3
# 输出：3
#
#
#
#
#
#
# 提示：
#
#
# 树中的节点数为 n 。
# 1 <= k <= n <= 10^4
# 0 <= Node.val <= 10^4
#
#
#
#
# 进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？
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

    def solution1(self, root: Optional[TreeNode], k: int) -> int:

        def get_node_count(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            left_count = get_node_count(node.left)
            right_count = get_node_count(node.right)
            return 1 + left_count + right_count

        left_count = get_node_count(root.left)
        right_count = get_node_count(root.right)

        if k > 1 + left_count + right_count:
            return -1
        else:
            if k <= left_count:
                return self.solution1(root.left, k)
            elif k == 1 + left_count:
                return root.val
            else:
                return self.solution1(root.right, k - 1 - left_count)

    def solution2(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # return self.solution1(root, k)
        return self.solution2(root, k)


# @lc code=end

#
# @lcpr case=start
# [3,1,4,null,2]\n1\n
# @lcpr case=end

# @lcpr case=start
# [5,3,6,2,4,null,null,1]\n3\n
# @lcpr case=end

#
