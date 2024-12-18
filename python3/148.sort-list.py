#
# @lc app=leetcode.cn id=148 lang=python3
# @lcpr version=30204
#
# [148] 排序链表
#
# https://leetcode.cn/problems/sort-list/description/
#
# algorithms
# Medium (65.85%)
# Likes:    2360
# Dislikes: 0
# Total Accepted:    558.3K
# Total Submissions: 845.8K
# Testcase Example:  '[4,2,1,3]'
#
# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
#
#
#
#
#
#
# 示例 1：
#
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
#
#
# 示例 2：
#
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
#
#
# 示例 3：
#
# 输入：head = []
# 输出：[]
#
#
#
#
# 提示：
#
#
# 链表中节点的数目在范围 [0, 5 * 10^4] 内
# -10^5 <= Node.val <= 10^5
#
#
#
#
# 进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
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

    def solution1(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def merge_link(head1: Optional[ListNode],
                       head2: Optional[ListNode]) -> Optional[ListNode]:
            dummy_head = ListNode(0)
            temp = dummy_head
            while head1 and head2:
                if head1.val <= head2.val:
                    temp.next = head1
                    head1 = head1.next
                else:
                    temp.next = head2
                    head2 = head2.next
                temp = temp.next
            if head1:
                temp.next = head1
            elif head2:
                temp.next = head2

            return dummy_head.next

        def sort_link(head: Optional[ListNode],
                      tail: Optional[ListNode]) -> Optional[ListNode]:
            if not head:
                return head

            if head.next == tail:
                head.next = None
                return head

            slow = fast = head

            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next

            mid = slow

            return merge_link(sort_link(head, mid), sort_link(mid, tail))

        return sort_link(head, None)

    def solution2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        def quick_sort(pre: Optional[ListNode], end: Optional[ListNode]):
            if pre == end or pre.next == end or pre.next.next == end:
                return

            pivot, cur = pre.next, ListNode(0)
            left, right = cur, pivot

            while right.next != end:
                if right.next.val < pivot.val:
                    left.next = right.next
                    left = left.next
                    right.next = right.next.next
                else:
                    right = right.next

            left.next = pre.next
            pre.next = cur.next

            quick_sort(pre, pivot)
            quick_sort(pivot, end)

        pre = ListNode(0, head)
        quick_sort(pre, None)

        return pre.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.solution1(head)
        # return self.solution2(head)


# @lc code=end

#
# @lcpr case=start
# [4,2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [-1,5,3,4,0]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#
