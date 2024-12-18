#
# @lc app=leetcode.cn id=103 lang=python3
# @lcpr version=30204
#
# [103] 二叉树的锯齿形层序遍历
#
# https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (59.21%)
# Likes:    911
# Dislikes: 0
# Total Accepted:    395.9K
# Total Submissions: 667.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
#
#
# 示例 1：
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[20,9],[15,7]]
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

    def bfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        ans = []
        flag = True
        queue = collections.deque([root])

        while queue:
            tmp_ans = []
            cur_level_size = len(queue)

            for _ in range(cur_level_size):
                if flag:
                    node = queue.popleft()
                    queue.append(node.left) if node.left else None
                    queue.append(node.right) if node.right else None
                else:
                    node = queue.pop()
                    queue.appendleft(node.right) if node.right else None
                    queue.appendleft(node.left) if node.left else None

                tmp_ans.append(node.val)

            flag = False if flag else True

            ans.append(tmp_ans)

        return ans

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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


tests = [[3, 9, 20, None, None, 15, 7], [1], [], [1, 2, 3, 4, 5]]
ans = [[[3], [20, 9], [15, 7]], [[1]], [], [[1], [3, 2], [4, 5]]]
for i, (t, a) in enumerate(zip(tests, ans)):
    root = build_tree_from_list(t)
    res = Solution().zigzagLevelOrder(root)
    print(f"test case {i+1}:\n"
          f"\ttest = {i+1};\n"
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
