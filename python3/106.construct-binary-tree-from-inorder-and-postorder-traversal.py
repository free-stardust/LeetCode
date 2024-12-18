#
# @lc app=leetcode.cn id=106 lang=python3
# @lcpr version=30204
#
# [106] 从中序与后序遍历序列构造二叉树
#
# https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (72.34%)
# Likes:    1256
# Dislikes: 0
# Total Accepted:    408.7K
# Total Submissions: 564.7K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# 给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder
# 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。
#
#
#
# 示例 1:
#
# 输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# 输出：[3,9,20,null,null,15,7]
#
#
# 示例 2:
#
# 输入：inorder = [-1], postorder = [-1]
# 输出：[-1]
#
#
#
#
# 提示:
#
#
# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder 和 postorder 都由 不同 的值组成
# postorder 中每一个值都在 inorder 中
# inorder 保证是树的中序遍历
# postorder 保证是树的后序遍历
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
# class TreeNode:

#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def recursion1(self, inorder: List[int],
                   postorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val: idx for idx, val in enumerate(inorder)}

        def helper(in_left, in_right):
            if in_left > in_right:
                return None

            val = postorder.pop()
            root = TreeNode(val)

            index = idx_map[val]

            # 注意：这里左右不能反，因为后序遍历时是“左右根”，如果先左，就会导致 pop 出错
            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)

            return root

        return helper(0, len(inorder) - 1)

    def recursion2(self, inorder: List[int],
                   postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        index_dict = {val: index for index, val in enumerate(inorder)}

        def build_tree(in_left, in_right, post_left, post_right):
            if in_left > in_right:
                return None

            in_root = index_dict[postorder[post_right]]
            size_left_tree = in_root - in_left

            root = TreeNode(postorder[post_right])
            root.left = build_tree(in_left, in_root - 1, post_left,
                                   post_left + size_left_tree - 1)
            root.right = build_tree(in_root + 1, in_right,
                                    post_left + size_left_tree, post_right - 1)
            return root

        return build_tree(0, n - 1, 0, n - 1)

    def buildTree(self, inorder: List[int],
                  postorder: List[int]) -> Optional[TreeNode]:
        # return self.recursion1(inorder, postorder)
        return self.recursion2(inorder, postorder)


# @lc code=end


def build_list_from_tree(root: Optional[TreeNode]) -> List[int]:
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

    for i in range(len(ans) - 1, 0, -1):
        if not ans[i]:
            ans.pop()
        else:
            break

    return ans


tests = [[[9, 3, 15, 20, 7], [9, 15, 7, 20, 3]], [[-1], [-1]]]
ans = [[3, 9, 20, None, None, 15, 7], [-1]]
for i, (t, a) in enumerate(zip(tests, ans)):
    root = Solution().buildTree(t[0], t[1])
    res = build_list_from_tree(root)
    print(f"test case {i+1};\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# [9,3,15,20,7]\n[9,15,7,20,3]\n
# @lcpr case=end

# @lcpr case=start
# [-1]\n[-1]\n
# @lcpr case=end

#
