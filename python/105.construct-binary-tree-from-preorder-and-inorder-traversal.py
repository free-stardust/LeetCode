#
# @lc app=leetcode.cn id=105 lang=python3
# @lcpr version=30204
#
# [105] 从前序与中序遍历序列构造二叉树
#
# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (71.85%)
# Likes:    2362
# Dislikes: 0
# Total Accepted:    694.6K
# Total Submissions: 965.7K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder
# 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
#
#
#
# 示例 1:
#
# 输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# 输出: [3,9,20,null,null,15,7]
#
#
# 示例 2:
#
# 输入: preorder = [-1], inorder = [-1]
# 输出: [-1]
#
#
#
#
# 提示:
#
#
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder 和 inorder 均 无重复 元素
# inorder 均出现在 preorder
# preorder 保证 为二叉树的前序遍历序列
# inorder 保证 为二叉树的中序遍历序列
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

    def recursion(self, preorder: List[int],
                  inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        index = {node: i for i, node in enumerate(inorder)}

        def build_tree(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None

            pre_root = pre_left
            in_root = index[preorder[pre_root]]

            root = TreeNode(preorder[pre_root])
            size_left_tree = in_root - in_left

            root.left = build_tree(pre_left + 1, pre_left + size_left_tree,
                                   in_left, in_root - 1)
            root.right = build_tree(pre_left + size_left_tree + 1, pre_right,
                                    in_root + 1, in_right)
            return root

        return build_tree(0, n - 1, 0, n - 1)

    def traverse(self, preorder: List[int],
                 inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        in_index = 0

        for i in range(1, len(preorder)):
            pre_val = preorder[i]
            node = stack[-1]
            if node.val != inorder[in_index]:
                node.left = TreeNode(pre_val)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[in_index]:
                    node = stack.pop()
                    in_index += 1
                node.right = TreeNode(pre_val)
                stack.append(node.right)

        return root

    def buildTree(self, preorder: List[int],
                  inorder: List[int]) -> Optional[TreeNode]:
        # return self.recursion(preorder, inorder)
        return self.traverse(preorder, inorder)


# @lc code=end


def build_tree_from_list(l, index=0) -> Optional[TreeNode]:
    if len(l) == 0 or index >= len(l):
        return None

    root = None

    if l[index]:
        root = TreeNode(l[index])
        root.left = build_tree_from_list(l, 2 * index + 1)
        root.right = build_tree_from_list(l, 2 * index + 2)

    return root


def build_list_from_tree(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []

    ans = []
    queue = collections.deque([root])

    while queue:
        cur_len = len(queue)
        for _ in range(cur_len):
            node = queue.popleft()
            ans.append(node.val if node else None)
            if node:
                queue.append(node.left) if node.left else None
                queue.append(node.right) if node.right else None

    return ans


tests = [[[3, 9, 20, 15, 7], [9, 3, 15, 20, 7]], [[-1], [-1]]]
ans = [[3, 9, 20, None, None, 15, 7], [-1]]
for i, (t, a) in enumerate(zip(tests, ans)):
    root = Solution().buildTree(t[0], t[1])
    res = build_list_from_tree(root)
    print(f"test case = {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# [3,9,20,15,7]\n[9,3,15,20,7]\n
# @lcpr case=end

# @lcpr case=start
# [-1]\n[-1]\n
# @lcpr case=end

#
