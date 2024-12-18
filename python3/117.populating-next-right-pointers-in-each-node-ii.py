#
# @lc app=leetcode.cn id=117 lang=python3
# @lcpr version=30204
#
# [117] 填充每个节点的下一个右侧节点指针 II
#
# https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/description/
#
# algorithms
# Medium (69.86%)
# Likes:    857
# Dislikes: 0
# Total Accepted:    275.4K
# Total Submissions: 393.5K
# Testcase Example:  '[1,2,3,4,5,null,7]'
#
# 给定一个二叉树：
#
# struct Node {
# ⁠ int val;
# ⁠ Node *left;
# ⁠ Node *right;
# ⁠ Node *next;
# }
#
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL 。
#
# 初始状态下，所有 next 指针都被设置为 NULL 。
#
#
#
# 示例 1：
#
# 输入：root = [1,2,3,4,5,null,7]
# 输出：[1,#,2,3,#,4,5,7,#]
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化输出按层序遍历顺序（由 next
# 指针连接），'#' 表示每层的末尾。
#
# 示例 2：
#
# 输入：root = []
# 输出：[]
#
#
#
#
# 提示：
#
#
# 树中的节点数在范围 [0, 6000] 内
# -100 <= Node.val <= 100
#
#
# 进阶：
#
#
# 你只能使用常量级额外空间。
# 使用递归解题也符合要求，本题中递归程序的隐式栈空间不计入额外空间复杂度。
#
#
#
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
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:

    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        if not root.left and not root.right:
            root.next = None
            return root

        queue = collections.deque([root])

        while queue:
            cur_len = len(queue)
            pre = None
            for _ in range(cur_len):
                node = queue.popleft()
                if pre:
                    pre.next = node
                pre = node
                queue.append(node.left) if node.left else None
                queue.append(node.right) if node.right else None

        return root


# @lc code=end

#
# @lcpr case=start
# [1,2,3,4,5,null,7]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#
