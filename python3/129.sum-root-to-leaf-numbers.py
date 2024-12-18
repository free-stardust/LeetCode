#
# @lc app=leetcode.cn id=129 lang=python3
# @lcpr version=30204
#
# [129] 求根节点到叶节点数字之和
#
# https://leetcode.cn/problems/sum-root-to-leaf-numbers/description/
#
# algorithms
# Medium (70.83%)
# Likes:    756
# Dislikes: 0
# Total Accepted:    287.4K
# Total Submissions: 405.3K
# Testcase Example:  '[1,2,3]'
#
# 给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
#
#
# 每条从根节点到叶节点的路径都代表一个数字：
#
#
# 例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
#
#
# 计算从根节点到叶节点生成的 所有数字之和 。
#
# 叶节点 是指没有子节点的节点。
#
#
#
# 示例 1：
#
# 输入：root = [1,2,3]
# 输出：25
# 解释：
# 从根到叶子节点路径 1->2 代表数字 12
# 从根到叶子节点路径 1->3 代表数字 13
# 因此，数字总和 = 12 + 13 = 25
#
# 示例 2：
#
# 输入：root = [4,9,0,5,1]
# 输出：1026
# 解释：
# 从根到叶子节点路径 4->9->5 代表数字 495
# 从根到叶子节点路径 4->9->1 代表数字 491
# 从根到叶子节点路径 4->0 代表数字 40
# 因此，数字总和 = 495 + 491 + 40 = 1026
#
#
#
#
# 提示：
#
#
# 树中节点的数目在范围 [1, 1000] 内
# 0 <= Node.val <= 9
# 树的深度不超过 10
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
# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def dfs(self, root: Optional[TreeNode]) -> int:

        def dfs_sum(node: Optional[TreeNode], pre_sum: int) -> int:
            if node is None:
                return 0

            node_sum = 10 * pre_sum + node.val
            if not node.left and not node.right:
                return node_sum
            else:
                return dfs_sum(node.left, node_sum) + dfs_sum(
                    node.right, node_sum)

        return dfs_sum(root, 0)

    def bfs_sum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        total_sum = 0
        node_queue = collections.deque([root])
        sum_queue = collections.deque([root.val])

        while node_queue:
            node = node_queue.popleft()
            tmp_sum = sum_queue.popleft()
            left, right = node.left, node.right
            if not left and not right:
                total_sum += tmp_sum
            else:
                if left:
                    node_queue.append(left)
                    sum_queue.append(10 * tmp_sum + left.val)
                if right:
                    node_queue.append(right)
                    sum_queue.append(10 * tmp_sum + right.val)

        return total_sum

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # return self.dfs(root)
        return self.bfs_sum(root)


# @lc code=end


def build_tree_from_list(l: List[int], index=0) -> Optional[TreeNode]:
    if len(l) == 0 or index >= len(l):
        return None

    root = None

    if l[index] is not None:
        root = TreeNode(l[index])
        root.left = build_tree_from_list(l, 2 * index + 1)
        root.right = build_tree_from_list(l, 2 * index + 2)

    return root


tests = [[1, 2, 3], [4, 9, 0, 5, 1]]
ans = [25, 1026]
all_pass = True
for i, (t, a) in enumerate(zip(tests, ans)):
    root = build_tree_from_list(t)
    res = Solution().sumNumbers(root)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res};")
    all_pass &= a == res
print(f"all pass: {all_pass}.")

#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [4,9,0,5,1]\n
# @lcpr case=end

#
