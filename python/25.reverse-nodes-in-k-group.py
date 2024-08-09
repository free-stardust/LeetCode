#
# @lc app=leetcode.cn id=25 lang=python3
# @lcpr version=30204
#
# [25] K 个一组翻转链表
#
# https://leetcode.cn/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (68.26%)
# Likes:    2374
# Dislikes: 0
# Total Accepted:    639.6K
# Total Submissions: 936.7K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
# 
# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# 
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
# 
# 
# 
# 示例 1：
# 
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]
# 
# 
# 示例 2：
# 
# 
# 
# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]
# 
# 
# 
# 提示：
# 
# 
# 链表中的节点数目为 n
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
# 
# 
# 
# 
# 进阶：你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？
# 
# 
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
    def recursion1(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        p = ListNode(next=head)
        for _ in range(k):
            if head:
                head = head.next
            else:
                return p.next
        
        pre = p.next
        for _ in range(k-1):
            p1 = p.next
            p2 = pre.next
            p3 = p2.next

            pre.next = p3
            p2.next = p1
            p.next = p2

        pre.next = self.recursion1(pre.next, k) 
        
        return p.next
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return self.recursion1(head, k)
# @lc code=end

def list_to_link(l: List[int]) -> Optional[ListNode]:
    l_len = len(l)

    if l_len == 0:
        return None
    
    lk = head = ListNode(l[0])
    for i in range(1, l_len):
        lk.next = ListNode(l[i])
        lk = lk.next

    return head

def link_to_list(lk: Optional[ListNode]) -> List[int]:
    if lk is None:
        return []
    
    l = []
    while lk:
        l.append(lk.val)
        lk = lk.next
    return l

tests = [[[1,2,3,4,5], 2],[[1,2,3,4,5], 3]]
ans = [[2,1,4,3,5], [3,2,1,4,5]]
for i,(t,a) in enumerate(zip(tests,ans)):
    lk = list_to_link(t[0])
    res = Solution().reverseKGroup(lk, t[1])
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
# [1,2,3,4,5]\n3\n
# @lcpr case=end

#

