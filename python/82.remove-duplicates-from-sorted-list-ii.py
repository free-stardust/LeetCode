#
# @lc app=leetcode.cn id=82 lang=python3
# @lcpr version=30204
#
# [82] 删除排序链表中的重复元素 II
#
# https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (54.50%)
# Likes:    1313
# Dislikes: 0
# Total Accepted:    463.3K
# Total Submissions: 849.5K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。
#
#
#
# 示例 1：
#
# 输入：head = [1,2,3,3,4,4,5]
# 输出：[1,2,5]
#
#
# 示例 2：
#
# 输入：head = [1,1,1,2,3]
# 输出：[2,3]
#
#
#
#
# 提示：
#
#
# 链表中节点数目在范围 [0, 300] 内
# -100 <= Node.val <= 100
# 题目数据保证链表已经按升序 排列
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

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        cur = p = ListNode(0, head)

        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                tmp = cur.next.val
                while cur.next and cur.next.val == tmp:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return p.next


# @lc code=end


def list_to_link(l: List[int]) -> Optional[ListNode]:
    lk = ListNode()
    p = lk

    for num in l:
        p.next = ListNode(num)
        p = p.next

    return lk.next


def link_to_list(lk: Optional[ListNode]) -> List[int]:
    l = []

    while lk:
        l.append(lk.val)
        lk = lk.next

    return l


tests = [[1, 2, 3, 3, 4, 4, 5], [1, 1, 1, 2, 3], [1, 1]]
ans = [[1, 2, 5], [2, 3], []]
for i, (t, a) in enumerate(zip(tests, ans)):
    t_lk = list_to_link(t)
    res_lk = Solution().deleteDuplicates(t_lk)
    res = link_to_list(res_lk)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")

#
# @lcpr case=start
# [1,2,3,3,4,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,2,3]\n
# @lcpr case=end

#
