#
# @lc app=leetcode.cn id=437 lang=python3
# @lcpr version=30204
#
# [437] 路径总和 III
#
# https://leetcode.cn/problems/path-sum-iii/description/
#
# algorithms
# Medium (47.56%)
# Likes:    1914
# Dislikes: 0
# Total Accepted:    339.7K
# Total Submissions: 714.9K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
#
# 路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
#
#
#
# 示例 1：
#
#
#
# 输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# 输出：3
# 解释：和等于 8 的路径有 3 条，如图所示。
#
#
# 示例 2：
#
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：3
#
#
#
#
# 提示:
#
#
# 二叉树的节点个数的范围是 [0,1000]
# -10^9 <= Node.val <= 10^9
# -1000 <= targetSum <= 1000
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

    def use_dfs1(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0

        def dfs(node: Optional[TreeNode], sub_sum: int):
            if node is None:
                return 0

            cnt = 0
            if node.val == sub_sum:
                cnt += 1

            cnt += dfs(node.left, sub_sum - node.val)
            cnt += dfs(node.right, sub_sum - node.val)
            return cnt

        ans = dfs(root, targetSum)
        ans += self.use_dfs(root.left, targetSum)
        ans += self.use_dfs(root.right, targetSum)

        return ans

    def use_dfs2(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = collections.defaultdict(int)
        prefix[0] = 1

        def dfs(node: Optional[TreeNode], curr: int):
            if node is None:
                return 0

            ans = 0
            curr += node.val
            ans += prefix[curr - targetSum]
            prefix[curr] += 1
            ans += dfs(node.left, curr)
            ans += dfs(node.right, curr)
            prefix[curr] -= 1

            return ans

        return dfs(root, 0)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # return self.use_dfs1(root, targetSum)
        return self.use_dfs2(root, targetSum)


# @lc code=end

#
# @lcpr case=start
# [10,5,-3,3,2,null,11,3,-2,null,1]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,4,8,11,null,13,4,7,2,null,null,5,1]\n22\n
# @lcpr case=end

#
