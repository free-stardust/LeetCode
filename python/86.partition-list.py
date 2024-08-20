#
# @lc app=leetcode.cn id=86 lang=python3
# @lcpr version=30204
#
# [86] 分隔链表
#
# https://leetcode.cn/problems/partition-list/description/
#
# algorithms
# Medium (64.92%)
# Likes:    850
# Dislikes: 0
# Total Accepted:    299.2K
# Total Submissions: 460.5K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
#
# 你应当 保留 两个分区中每个节点的初始相对位置。
#
#
#
# 示例 1：
#
# 输入：head = [1,4,3,2,5,2], x = 3
# 输出：[1,2,2,4,3,5]
#
#
# 示例 2：
#
# 输入：head = [2,1], x = 2
# 输出：[1,2]
#
#
#
#
# 提示：
#
#
# 链表中节点的数目在范围 [0, 200] 内
# -100 <= Node.val <= 100
# -200 <= x <= 200
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
# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def partition(self, head: Optional[ListNode],
                  x: int) -> Optional[ListNode]:
        small = small_head = ListNode(0)
        large = large_head = ListNode(0)

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next

        large.next = None
        small.next = large_head.next

        return small_head.next


# @lc code=end


def list_to_link(l: List[int]) -> Optional[ListNode]:
    p = lk = ListNode(l[0])

    for i in range(1, len(l)):
        p.next = ListNode(l[i])
        p = p.next

    return lk


def link_to_list(lk: Optional[ListNode]) -> List[int]:
    l = []

    while lk:
        l.append(lk.val)
        lk = lk.next

    return l


tests = [[[1, 4, 3, 2, 5, 2], 3], [[2, 1], 2]]
ans = [[1, 2, 2, 4, 3, 5], [1, 2]]
for i, (t, a) in enumerate(zip(tests, ans)):
    t_lk = list_to_link(t[0])
    res_lk = Solution().partition(t_lk, t[1])
    res = link_to_list(res_lk)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# [1,4,3,2,5,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n2\n
# @lcpr case=end

#
