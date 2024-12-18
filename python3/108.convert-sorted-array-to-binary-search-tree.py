#
# @lc app=leetcode.cn id=108 lang=python3
# @lcpr version=30204
#
# [108] 将有序数组转换为二叉搜索树
#
# https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (78.92%)
# Likes:    1547
# Dislikes: 0
# Total Accepted:    517.5K
# Total Submissions: 654.7K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡 二叉搜索树。
#
#
#
# 示例 1：
#
# 输入：nums = [-10,-3,0,5,9]
# 输出：[0,-3,9,-10,null,5]
# 解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：
#
#
#
# 示例 2：
#
# 输入：nums = [1,3]
# 输出：[3,1]
# 解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums 按 严格递增 顺序排列
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

    def recursion1(self, nums: List[int]) -> Optional[TreeNode]:

        def build_tree(left, right):
            if left > right:
                return None
            mid = (left + right + 1) // 2

            root = TreeNode(nums[mid])
            root.left = build_tree(left, mid - 1)
            root.right = build_tree(mid + 1, right)

            return root

        return build_tree(0, len(nums) - 1)

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.recursion1(nums)


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


tests = [[-10, -3, 0, 5, 9], [1, 3]]
ans = [[0, -3, 9, -10, None, 5], [3, 1]]
for i, (t, a) in enumerate(zip(tests, ans)):
    root = Solution().sortedArrayToBST(t)
    res = build_list_from_tree(root)
    print(f"test case {i+1};\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# [-10,-3,0,5,9]\n
# @lcpr case=end

# @lcpr case=start
# [1,3]\n
# @lcpr case=end

#
