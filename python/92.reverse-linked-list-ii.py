#
# @lc app=leetcode.cn id=92 lang=python3
# @lcpr version=30204
#
# [92] 反转链表 II
#
# https://leetcode.cn/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (56.49%)
# Likes:    1831
# Dislikes: 0
# Total Accepted:    542.2K
# Total Submissions: 958.7K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right
# 的链表节点，返回 反转后的链表 。
#
#
# 示例 1：
#
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
#
#
# 示例 2：
#
# 输入：head = [5], left = 1, right = 1
# 输出：[5]
#
#
#
#
# 提示：
#
#
# 链表中节点数目为 n
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
#
#
#
#
# 进阶： 你可以使用一趟扫描完成反转吗？
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
# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def double_point1(self, head: Optional[ListNode], left: int,
                      right: int) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        pre = dummy_node

        for _ in range(left - 1):
            pre = pre.next

        cur = pre.next
        for _ in range(right - left):
            cur_next = cur.next
            cur.next = cur_next.next
            cur_next.next = pre.next
            pre.next = cur_next

        return dummy_node.next

    def divide_and_reverse(self, head: Optional[ListNode], left: int,
                           right: int) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)

        def reversed_link_list(head: Optional[ListNode]) -> None:
            pre = None
            cur = head

            while cur:
                cur_next = cur.next
                cur.next = pre
                pre = cur
                cur = cur_next

        pre = dummy_node

        for _ in range(left - 1):
            pre = pre.next

        right_node = pre.next

        for _ in range(right - left):
            right_node = right_node.next

        left_node = pre.next
        curr = right_node.next

        pre.next = None
        right_node.next = None

        reversed_link_list(left_node)

        pre.next = right_node
        left_node.next = curr

        return dummy_node.next

    def reverseBetween(self, head: Optional[ListNode], left: int,
                       right: int) -> Optional[ListNode]:
        # return self.double_point(head, left, right)
        return self.divide_and_reverse(head, left, right)


# @lc code=end


def list_to_link(l: List[int]) -> Optional[ListNode]:
    p = lk = ListNode(0)

    for data in l:
        p.next = ListNode(data)
        p = p.next

    return lk.next


def link_to_list(lk: Optional[ListNode]) -> List[int]:
    l = []

    while lk:
        l.append(lk.val)
        lk = lk.next

    return l


tests = [[[1, 2, 3, 4, 5], 2, 4], [[5], 1, 1]]
ans = [[1, 4, 3, 2, 5], [5]]
for i, (t, a) in enumerate(zip(tests, ans)):
    t_lk = list_to_link(t[0])
    res_lk = Solution().reverseBetween(t_lk, t[1], t[2])
    res = link_to_list(res_lk)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")
#
# @lcpr case=start
# [1,2,3,4,5]\n2\n4\n
# @lcpr case=end

# @lcpr case=start
# [5]\n1\n1\n
# @lcpr case=end

#
