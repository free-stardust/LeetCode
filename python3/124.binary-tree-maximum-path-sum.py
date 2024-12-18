#
# @lc app=leetcode.cn id=124 lang=python3
# @lcpr version=30204
#
# [124] 二叉树中的最大路径和
#
# https://leetcode.cn/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (45.73%)
# Likes:    2268
# Dislikes: 0
# Total Accepted:    447K
# Total Submissions: 975.3K
# Testcase Example:  '[1,2,3]'
#
# 二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个
# 节点，且不一定经过根节点。
#
# 路径和 是路径中各节点值的总和。
#
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。
#
#
#
# 示例 1：
#
# 输入：root = [1,2,3]
# 输出：6
# 解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
#
# 示例 2：
#
# 输入：root = [-10,9,20,null,null,15,7]
# 输出：42
# 解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
#
#
#
#
# 提示：
#
#
# 树中节点数目范围是 [1, 3 * 10^4]
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

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")

        def max_gain(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            left_max_gain = max(max_gain(node.left), 0)
            right_max_gain = max(max_gain(node.right), 0)

            node_max_gain = node.val + left_max_gain + right_max_gain

            nonlocal max_sum
            max_sum = max(max_sum, node_max_gain)

            return node.val + max(left_max_gain, right_max_gain)

        max_gain(root)

        return max_sum


# @lc code=end


def build_tree_from_list(l: List[int], index=0) -> Optional[TreeNode]:
    if len(l) == 0 or index >= len(l):
        return None

    root = None

    if l[index]:
        root = TreeNode(l[index])
        root.left = build_tree_from_list(l, 2 * index + 1)
        root.right = build_tree_from_list(l, 2 * index + 2)

    return root


tests = [[1, 2, 3], [-10, 9, 20, None, None, 15, 7]]
ans = [6, 42]
all_pass = True
for i, (t, a) in enumerate(zip(tests, ans)):
    root = build_tree_from_list(t)
    res = Solution().maxPathSum(root)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")
    all_pass &= (a == res)
print(f"all pass: {all_pass}.")
#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [-10,9,20,null,null,15,7]\n
# @lcpr case=end

#
