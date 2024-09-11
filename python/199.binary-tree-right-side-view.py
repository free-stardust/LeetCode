#
# @lc app=leetcode.cn id=199 lang=python3
# @lcpr version=30204
#
# [199] 二叉树的右视图
#
# https://leetcode.cn/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (67.54%)
# Likes:    1113
# Dislikes: 0
# Total Accepted:    476.8K
# Total Submissions: 702.7K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
#
#
#
# 示例 1:
#
#
#
# 输入: [1,2,3,null,5,null,4]
# 输出: [1,3,4]
#
#
# 示例 2:
#
# 输入: [1,null,3]
# 输出: [1,3]
#
#
# 示例 3:
#
# 输入: []
# 输出: []
#
#
#
#
# 提示:
#
#
# 二叉树的节点个数的范围是 [0,100]
# -100 <= Node.val <= 100
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

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def bfs(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        ans = []
        deque = collections.deque([root])

        while deque:
            ans.append(deque[-1].val)
            deque_len = len(deque)
            for _ in range(deque_len):
                node = deque.popleft()
                deque.append(node.left) if node.left else None
                deque.append(node.right) if node.right else None

        return ans

    def dfs(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        ans = []

        def dfs_inner(node: Optional[TreeNode], depth: int):
            if node is None:
                return

            if len(ans) <= depth:
                ans.append(node.val)
            else:
                ans[depth] = node.val

            dfs_inner(node.left, depth + 1)
            dfs_inner(node.right, depth + 1)

        dfs_inner(root, 0)

        return ans

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # return self.bfs(root)
        return self.dfs(root)


# @lc code=end

#
# @lcpr case=start
# [1,2,3,null,5,null,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#
