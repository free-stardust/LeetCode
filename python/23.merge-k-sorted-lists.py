#
# @lc app=leetcode.cn id=23 lang=python3
# @lcpr version=30204
#
# [23] 合并 K 个升序链表
#
# https://leetcode.cn/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (60.04%)
# Likes:    2859
# Dislikes: 0
# Total Accepted:    843.7K
# Total Submissions: 1.4M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 给你一个链表数组，每个链表都已经按升序排列。
# 
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
# 
# 
# 
# 示例 1：
# 
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
# ⁠ 1->4->5,
# ⁠ 1->3->4,
# ⁠ 2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
# 
# 
# 示例 2：
# 
# 输入：lists = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 输入：lists = [[]]
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] 按 升序 排列
# lists[i].length 的总和不超过 10^4
# 
# 
#


# @lcpr-template-start
from heapq import heapify, heappop, heappush
from typing import List, Tuple
from typing import Optional
# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def recursion1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists_len = len(lists)

        if lists_len == 0:
            return None
        
        if lists_len == 1:
            return lists[0]
        
        node = None
        if lists_len == 2:
            left = lists[0]
            right = lists[1]
            if not left and not right:
                return None
            elif left and not right:
                return left
            elif right and not left:
                return right
            
            if left.val <= right.val:
                node = left
                node.next = self.recursion1([left.next, right])
            else:
                node = right
                node.next = self.recursion1([left,right.next])

        if lists_len > 2:
            mid = lists_len // 2
            node1 = self.recursion1(lists[:mid])
            node2 = self.recursion1(lists[mid:])
            node = self.recursion1([node1, node2])
            
        return node
    
    def traverse1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        def merge(l1:Optional[ListNode], l2:Optional[ListNode]) -> Optional[ListNode]: 
            p = head = ListNode()

            while l1 and l2:
                if l1.val <= l2.val:
                    p.next = l1
                    l1 = l1.next
                else:
                    p.next = l2
                    l2 = l2.next
                p = p.next
            
            p.next = l1 or l2
            return head.next
        
        n = len(lists)
        while n > 1:
            mid = n >> 1
            for i in range(mid):
                lists[i] = merge(lists[i], lists[n-i-1])
            n = mid + n % 2    
        return lists[0]
    
    def heap1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur = head = ListNode()  # 哨兵节点，作为合并后链表头节点的前一个节点
        heads = [h for h in lists if h]  # 初始把所有链表的头节点入堆
        heapify(heads)  # 堆化
        while heads:  # 循环直到堆为空
            node = heappop(heads)  # 剩余节点中的最小节点
            if node.next:  # 下一个节点不为空
                heappush(heads, node.next)  # 下一个节点有可能是最小节点，入堆
            cur.next = node  # 合并到新链表中
            cur = cur.next  # 准备合并下一个节点
        return head.next  # 哨兵节点的下一个节点就是新链表的头节点
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # return self.recursion1(lists)
        return self.traverse1(lists)
        # return self.heap1(lists)
# @lc code=end

def list_to_link(l: List[int]) -> Optional[ListNode]:
    l_len = len(l)

    if l_len == 0:
        return None
    
    head = ListNode(l[0])
    point = head

    for i in range(1,l_len):
        point.next = ListNode(l[i])
        point = point.next

    return head

def link_to_list(lk:Optional[ListNode]) -> List[int]:
    if lk is None:
        return []
    
    l = []
    while lk:
        l.append(lk.val)
        lk = lk.next

    return l

def lists_to_links(lists: List[List[int]]) -> List[Optional[ListNode]]:
    ls_len = len(lists)

    if ls_len == 0:
        return []
    
    lks = []
    for l in lists:
        lks .append(list_to_link(l))
    
    return lks

tests = [[[1,4,5],[1,3,4],[2,6]], [], [[]]]
ans = [[1,1,2,3,4,4,5,6], [],[]]
for i,(t,a) in enumerate(zip(tests,ans)):
    t_lk = lists_to_links(t)
    res = Solution().mergeKLists(t_lk)
    res_list = link_to_list(res)
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res_list};\n"
          f"\t{a == res_list}.")

#
# @lcpr case=start
# [[1,4,5],[1,3,4],[2,6]]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [[]]\n
# @lcpr case=end

#

