#
# @lc app=leetcode.cn id=61 lang=python3
# @lcpr version=30204
#
# [61] 旋转链表
#
# https://leetcode.cn/problems/rotate-list/description/
#
# algorithms
# Medium (41.40%)
# Likes:    1073
# Dislikes: 0
# Total Accepted:    401K
# Total Submissions: 968.3K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
# 
# 
# 
# 示例 1：
# 
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[4,5,1,2,3]
# 
# 
# 示例 2：
# 
# 输入：head = [0,1,2], k = 4
# 输出：[2,0,1]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点的数目在范围 [0, 500] 内
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 10^9
# 
# 
#


# @lcpr-template-start
import copy
import collections
import random
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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head

        lk_len = 0
        pre = p = head

        while p:
            lk_len += 1
            pre = p
            p = p.next
        
        pre.next = head

        end_pos = lk_len - k % lk_len
        pre = p = head

        while end_pos > 0:
            pre = p
            p = p.next
            end_pos -= 1
        
        pre.next = None

        return p
# @lc code=end

def list_to_link(l: List[int]) -> ListNode:
    head = ListNode(0)
    p = head

    for num in l:
        p.next = ListNode(num)
        p = p.next
    
    return head.next

def link_to_list(lk: Optional[ListNode]) -> List[int]:
    l = []

    while lk:
        l.append(lk.val)
        lk = lk.next
    
    return l

tests = [[[1,2,3,4,5], 2], [[0,1,2], 4], [[], 0]]
ans = [[4,5,1,2,3], [2,0,1], []]
for i,(t,a) in enumerate(zip(tests, ans)):
    t_lk = list_to_link(t[0])
    res = Solution().rotateRight(t_lk, t[1])
    res_list = link_to_list(res)
    print(f"test case {i+1}:\n"
          f"\ttest = {t[0]}, {t[1]};\n"
          f"\tans = {a};\n"
          f"\tres = {res_list};\n"
          f"\t{a == res_list}.")



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2]\n4\n
# @lcpr case=end

#

