#
# @lc app=leetcode.cn id=24 lang=python3
# @lcpr version=30204
#
# [24] 两两交换链表中的节点
#
# https://leetcode.cn/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (72.65%)
# Likes:    2255
# Dislikes: 0
# Total Accepted:    905.1K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,4]'
#
# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
# 
# 
# 
# 示例 1：
# 
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
# 
# 
# 示例 2：
# 
# 输入：head = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 输入：head = [1]
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点的数目在范围 [0, 100] 内
# 0 <= Node.val <= 100
# 
# 
#


# @lcpr-template-start
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

    def recursion1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        p = p1  = ListNode()
        p1 = head.next.next
        p.next = head.next
        head.next.next = head
        head.next = self.swapPairs(p1)

        return p.next
    
    def traverse1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        p = pre = ListNode(next=head)
        while head and head.next:
            p1 = head.next
            p2 = p1.next

            pre.next = p1
            p1.next = head
            head.next = p2

            pre = head
            head = head.next           

        return p.next

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return self.recursion1(head)
        return self.traverse1(head)
# @lc code=end

def list_to_link(l: List[int]) -> Optional[ListNode]:
    l_len = len(l)

    if l_len == 0:
        return None
    
    p = head = ListNode(l[0])
    for i in range(1, l_len):
        p.next = ListNode(l[i])
        p = p.next
    
    return head

def link_to_list(lk: Optional[ListNode]) -> List[int]:
    if lk is None:
        return []
    
    l = []
    while lk:
        l.append(lk.val)
        lk = lk.next

    return l


test = [[1,2,3,4], [], [1]]
ans = [[2,1,4,3],[],[1]]
for i,(t,a) in enumerate(zip(test,ans)):
    t_link = list_to_link(t)
    res = Solution().swapPairs(t_link)
    res_list = link_to_list(res)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res_list};\n"
          f"\t{a == res_list}.")


#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

