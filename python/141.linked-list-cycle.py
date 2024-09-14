#
# @lc app=leetcode.cn id=141 lang=python3
# @lcpr version=30204
#
# [141] 环形链表
#
# https://leetcode.cn/problems/linked-list-cycle/description/
#
# algorithms
# Easy (52.61%)
# Likes:    2191
# Dislikes: 0
# Total Accepted:    1.3M
# Total Submissions: 2.5M
# Testcase Example:  '[3,2,0,-4]\n1'
#
# 给你一个链表的头节点 head ，判断链表中是否有环。
#
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos
# 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。
#
# 如果链表中存在环 ，则返回 true 。 否则，返回 false 。
#
#
#
# 示例 1：
#
#
#
# 输入：head = [3,2,0,-4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
#
# 示例 2：
#
#
#
# 输入：head = [1,2], pos = 0
# 输出：true
# 解释：链表中有一个环，其尾部连接到第一个节点。
#
#
# 示例 3：
#
#
#
# 输入：head = [1], pos = -1
# 输出：false
# 解释：链表中没有环。
#
#
#
#
# 提示：
#
#
# 链表中节点的数目范围是 [0, 10^4]
# -10^5 <= Node.val <= 10^5
# pos 为 -1 或者链表中的一个 有效索引 。
#
#
#
#
# 进阶：你能用 O(1)（即，常量）内存解决此问题吗？
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

    def use_hash(self, head: Optional[ListNode]) -> bool:
        visited = []

        while head:
            if head in visited:
                return True
            visited.append(head)
            head = head.next

        return False

    def double_point(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow, fast = head, head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # return self.use_hash(head)
        return self.double_point(head)


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