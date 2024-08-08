#
# @lc app=leetcode.cn id=19 lang=python3
# @lcpr version=30204
#
# [19] 删除链表的倒数第 N 个结点
#
# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (48.80%)
# Likes:    2911
# Dislikes: 0
# Total Accepted:    1.5M
# Total Submissions: 3.1M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
# 
# 
# 
# 示例 1：
# 
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
# 
# 
# 示例 2：
# 
# 输入：head = [1], n = 1
# 输出：[]
# 
# 
# 示例 3：
# 
# 输入：head = [1,2], n = 1
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中结点的数目为 sz
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
# 
# 
# 
# 
# 进阶：你能尝试使用一趟扫描实现吗？
# 
#


# @lcpr-template-start
from curses.ascii import SI
from email.header import Header
from os import link
from re import S
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        p = ListNode(next=head)
        p1, p2 = p, p

        for _ in range(n):
            p1 = p1.next

        while p1 and p1.next:
            p1, p2 = p1.next, p2.next
        
        p2.next = p2.next.next
        return p.next
# @lc code=end

def create_link_from_list(l: List[int]) -> Optional[ListNode]:
    l_len = len(l)
    if l == 0:
        return None
    head = ListNode(l[0])
    point = head
    for i in range(1,l_len):
        point.next = ListNode(l[i])
        point = point.next
    return head

def link_to_list(lk: Optional[ListNode]) -> List[int]:
    ans = []
    while lk:
        ans.append(lk.val)
        lk = lk.next
    return ans

tests = [[[1,2,3,4,5],2], [[1], 1], [[1,2], 1]]
ans = [[1,2,3,5], [], [1]]

for i,t,a in zip(range(len(tests)), tests, ans):
    lk = create_link_from_list(t[0])
    res = Solution().removeNthFromEnd(lk, t[1])
    res_list = link_to_list(res)
    print(f"test case {i}:\n"
          f"\ttest = {t[0]}, {t[1]};\n"
          f"\tans = {a};\n"
          f"\tres = {res_list};\n"
          f"\t{a == res_list}.")
    


#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n
# @lcpr case=end

#

