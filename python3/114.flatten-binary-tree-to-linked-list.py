#
# @lc app=leetcode.cn id=114 lang=python3
# @lcpr version=30204
#
# [114] 二叉树展开为链表
#
# https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (74.06%)
# Likes:    1719
# Dislikes: 0
# Total Accepted:    509.1K
# Total Submissions: 686.2K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# 给你二叉树的根结点 root ，请你将它展开为一个单链表：
#
#
# 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
# 展开后的单链表应该与二叉树 先序遍历 顺序相同。
#
#
#
#
# 示例 1：
#
# 输入：root = [1,2,5,3,4,null,6]
# 输出：[1,null,2,null,3,null,4,null,5,null,6]
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
# 输入：root = [0]
# 输出：[0]
#
#
#
#
# 提示：
#
#
# 树中结点数在范围 [0, 2000] 内
# -100 <= Node.val <= 100
#
#
#
#
# 进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？
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

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root or (not root.left and not root.right):
            return root

        if not root.left:
            self.flatten(root.right)
            return

        right_node = root.right
        root.right = root.left
        root.left = None
        next_step_root = root.right

        while root.right:
            root = root.right

        root.right = right_node
        self.flatten(next_step_root)


# @lc code=end


def build_tree_from_list(l, index=0):
    if len(l) == 0 or index >= len(l):
        return None

    root = None
    if l[index]:
        root = TreeNode(l[index])
        root.left = build_tree_from_list(l, 2 * index + 1)
        root.right = build_tree_from_list(l, 2 * index + 2)

    return root


def build_list_from_tree(root):
    if root is None:
        return []

    queue = collections.deque([root])
    ans = []

    while queue:
        cur_len = len(queue)
        for _ in range(cur_len):
            node = queue.popleft()
            ans.append(node.val if node else None)
            if node:
                queue.append(node.left if node.left else None)
                queue.append(node.right if node.right else None)

    for idx in range(len(ans) - 1, -1, -1):
        if ans[idx] is None:
            ans.pop()
        else:
            break

    return ans


tests = [[1, 2, 5, 3, 4, None, 6], [], [0]]
ans = [[1, None, 2, None, 3, None, 4, None, 5, None, 6], [], [0]]
for i, (t, a) in enumerate(zip(tests, ans)):
    root = build_tree_from_list(t)
    Solution().flatten(root)
    res = build_list_from_tree(root)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres= {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# [1,2,5,3,4,null,6]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#
