#
# @lc app=leetcode.cn id=101 lang=python3
# @lcpr version=30204
#
# [101] 对称二叉树
#
# https://leetcode.cn/problems/symmetric-tree/description/
#
# algorithms
# Easy (60.72%)
# Likes:    2778
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 1.9M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给你一个二叉树的根节点 root ， 检查它是否轴对称。
#
#
#
# 示例 1：
#
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
#
#
# 示例 2：
#
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
#
#
#
#
# 提示：
#
#
# 树中节点数目在范围 [1, 1000] 内
# -100 <= Node.val <= 100
#
#
#
#
# 进阶：你可以运用递归和迭代两种方法解决这个问题吗？
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

        def check(p, q) -> bool:
            if not p and not q:
                return True
            elif not p or not q:
                return False
            else:
                return p.val == q.val and\
                       check(p.left, q.right) and\
                       check(p.right, q.left)

        return check(root, root)

    def traverse(self, root: Optional[TreeNode]) -> bool:

        def check(p, q) -> bool:
            queue = []
            queue.append(p)
            queue.append(q)

            while len(queue) > 0:
                p, q = queue[0], queue[1]
                queue = queue[2:]

                if not p and not q:
                    continue

                if (not p or not q) or (p.val != q.val):
                    return False

                queue.append(p.left)
                queue.append(q.right)

                queue.append(p.right)
                queue.append(q.left)

            return True

        return check(root, root)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # return self.recursion(root)
        return self.traverse(root)


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


tests = [[1, 2, 2, 3, 4, 4, 3], [1, 2, 2, None, 3, None, 3]]
ans = [True, False]
for i, (t, a) in enumerate(zip(tests, ans)):
    root = build_tree_from_list(t)
    res = Solution().isSymmetric(root)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# [1,2,2,3,4,4,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,null,3,null,3]\n
# @lcpr case=end

#
