#
# @lc app=leetcode.cn id=234 lang=python3
# @lcpr version=30204
#
# [234] 回文链表
#
# https://leetcode.cn/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (54.91%)
# Likes:    1955
# Dislikes: 0
# Total Accepted:    808.7K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,2,1]'
#
# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
# 输入：head = [1,2,2,1]
# 输出：true
#
#
# 示例 2：
#
# 输入：head = [1,2]
# 输出：false
#
#
#
#
# 提示：
#
#
# 链表中节点数目在范围[1, 10^5] 内
# 0 <= Node.val <= 9
#
#
#
#
# 进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
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
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True

        stack = []
        slow = fast = head

        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        while stack:
            if stack.pop() != slow.val:
                return False
            slow = slow.next

        return True


# @lc code=end

#
# @lcpr case=start
# [1,2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#
