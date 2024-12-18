#
# @lc app=leetcode.cn id=102 lang=python3
# @lcpr version=30204
#
# [102] 二叉树的层序遍历
#
# https://leetcode.cn/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (67.78%)
# Likes:    2005
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 1.6M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
#
#
#
# 示例 1：
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]
#
#
# 示例 2：
#
# 输入：root = [1]
# 输出：[[1]]
#
#
# 示例 3：
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
# 树中节点数目在范围 [0, 2000] 内
# -1000 <= Node.val <= 1000
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

    def bfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        ans = []
        queue = collections.deque([root])

        while queue:
            tmp_ans = []
            cur_level_size = len(queue)

            for i in range(cur_level_size):
                node = queue.popleft()
                tmp_ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(tmp_ans)

        return ans

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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


tests = [[3, 9, 20, None, None, 15, 7], [1], []]
ans = [[[3], [9, 20], [15, 7]], [[1]], []]
for i, (t, a) in enumerate(zip(tests, ans)):
    root = build_tree_from_list(t)
    res = Solution().levelOrder(root)
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
# [1]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#
