#
# @lc app=leetcode.cn id=104 lang=python3
# @lcpr version=30204
#
# [104] 二叉树的最大深度
#
# https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (77.79%)
# Likes:    1862
# Dislikes: 0
# Total Accepted:    1.4M
# Total Submissions: 1.8M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树 root ，返回其最大深度。
#
# 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
#
#
#
# 示例 1：
#
#
#
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：3
#
#
# 示例 2：
#
# 输入：root = [1,null,2]
# 输出：2
#
#
#
#
# 提示：
#
#
# 树中节点的数量在 [0, 10^4] 区间内。
# -100 <= Node.val <= 100
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

    def dfs(self, root: Optional[TreeNode]) -> int:

        def depth(root) -> int:
            if root is None:
                return 0
            else:
                return max(depth(root.left), depth(root.right)) + 1

        return depth(root)

    def bfs(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            cur_len = len(queue)
            for _ in range(cur_len):
                node = queue.popleft()
                queue.append(node.left) if node.left else None
                queue.append(node.right) if node.right else None

        return depth

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # return self.dfs(root)
        return self.bfs(root)


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


tests = [[3, 9, 20, None, None, 15, 7], [1, None, 2], []]
ans = [3, 2, 0]
for i, (t, a) in enumerate(zip(tests, ans)):
    root = build_tree_from_list(t)
    res = Solution().maxDepth(root)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,2]\n
# @lcpr case=end

#
