#
# @lc app=leetcode.cn id=109 lang=python3
# @lcpr version=30204
#
# [109] 有序链表转换二叉搜索树
#
# https://leetcode.cn/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (76.81%)
# Likes:    922
# Dislikes: 0
# Total Accepted:    169K
# Total Submissions: 220K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# 给定一个单链表的头节点  head ，其中的元素 按升序排序 ，将其转换为 平衡 二叉搜索树。
# 
# 
# 
# 示例 1:
# 
# 
# 
# 输入: head = [-10,-3,0,5,9]
# 输出: [0,-3,9,-10,null,5]
# 解释: 一个可能的答案是[0，-3,9，-10,null,5]，它表示所示的高度平衡的二叉搜索树。
# 
# 
# 示例 2:
# 
# 输入: head = []
# 输出: []
# 
# 
# 
# 
# 提示:
# 
# 
# head 中的节点数在[0, 2 * 10^4] 范围内
# -10^5 <= Node.val <= 10^5
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
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
# @lc code=end



#
# @lcpr case=start
# [-10,-3,0,5,9]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

