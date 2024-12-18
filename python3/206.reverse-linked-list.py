#
# @lc app=leetcode.cn id=206 lang=python3
# @lcpr version=30204
#
# [206] 反转链表
#
# https://leetcode.cn/problems/reverse-linked-list/description/
#
# algorithms
# Easy (74.69%)
# Likes:    3667
# Dislikes: 0
# Total Accepted:    2M
# Total Submissions: 2.7M
# Testcase Example:  '[1,2,3,4,5]'
#
# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
#
#
#
#
# 示例 1：
#
# 输入：head = [1,2,3,4,5]
# 输出：[5,4,3,2,1]
#
#
# 示例 2：
#
# 输入：head = [1,2]
# 输出：[2,1]
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
# 链表中节点的数目范围是 [0, 5000]
# -5000 <= Node.val <= 5000
#
#
#
#
# 进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？
#
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
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def head_insert(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        p = ListNode()
        while head:
            head_next = head.next
            head.next = p.next
            p.next = head
            head = head_next

        return p.next

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        new_head = self.reverse(head.next)
        head.next.next = head
        head.next = None

        return new_head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.head_insert(head)
        # return self.reverse(head)


# @lc code=end


def build_link_from_list(l: List[int]) -> Optional[ListNode]:
    if len(l) == 0:
        return None

    p = head = ListNode()

    for num in l:
        p.next = ListNode(num)
        p = p.next

    return head.next


def build_list_from_link(lk: Optional[ListNode]) -> List[int]:
    l = []

    while lk:
        l.append(lk.val)
        lk = lk.next

    return l


test = [[1, 2, 3, 4, 5], [1, 2], []]
ans = [[5, 4, 3, 2, 1], [2, 1], []]
all_pass = True
for i, (t, a) in enumerate(zip(test, ans)):
    head = build_link_from_list(t)
    res_lk = Solution().reverseList(head)
    res = build_list_from_link(res_lk)
    all_pass &= (a == res)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res};")
print(f"all pass: {all_pass}.")

#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#
