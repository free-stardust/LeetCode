#
# @lc app=leetcode.cn id=142 lang=python3
# @lcpr version=30204
#
# [142] 环形链表 II
#
# https://leetcode.cn/problems/linked-list-cycle-ii/description/
#
# algorithms
# Medium (59.40%)
# Likes:    2605
# Dislikes: 0
# Total Accepted:    977.8K
# Total Submissions: 1.6M
# Testcase Example:  '[3,2,0,-4]\n1'
#
# 给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
#
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos
# 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos
# 不作为参数进行传递，仅仅是为了标识链表的实际情况。
#
# 不允许修改 链表。
#
#
#
#
#
#
# 示例 1：
#
#
#
# 输入：head = [3,2,0,-4], pos = 1
# 输出：返回索引为 1 的链表节点
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
#
# 示例 2：
#
#
#
# 输入：head = [1,2], pos = 0
# 输出：返回索引为 0 的链表节点
# 解释：链表中有一个环，其尾部连接到第一个节点。
#
#
# 示例 3：
#
#
#
# 输入：head = [1], pos = -1
# 输出：返回 null
# 解释：链表中没有环。
#
#
#
#
# 提示：
#
#
# 链表中节点的数目范围在范围 [0, 10^4] 内
# -10^5 <= Node.val <= 10^5
# pos 的值为 -1 或者链表中的一个有效索引
#
#
#
#
# 进阶：你是否可以使用 O(1) 空间解决此题？
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

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def solution1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()

        while head is not None:
            if head in visited:
                return head
            visited.add(head)
            head = head.next

        return None

    def solution2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast:
            slow = slow.next

            if fast.next is None:
                return None

            fast = fast.next.next

            if fast == slow:
                ptr = head
                while ptr != slow:
                    ptr = ptr.next
                    slow = slow.next
                return ptr

        return None

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return self.solution1(head)
        return self.solution2(head)


# @lc code=end

#
# @lcpr case=start
# [3,2,0,-4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [1]\n-1\n
# @lcpr case=end

#