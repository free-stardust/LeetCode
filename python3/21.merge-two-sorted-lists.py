#
# @lc app=leetcode.cn id=21 lang=python3
# @lcpr version=30204
#
# [21] 合并两个有序链表
#
# https://leetcode.cn/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (66.80%)
# Likes:    3568
# Dislikes: 0
# Total Accepted:    1.8M
# Total Submissions: 2.7M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
#
#
# 示例 1：
#
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
#
#
# 示例 2：
#
# 输入：l1 = [], l2 = []
# 输出：[]
#
#
# 示例 3：
#
# 输入：l1 = [], l2 = [0]
# 输出：[0]
#
#
#
#
# 提示：
#
#
# 两个链表的节点数目范围是 [0, 50]
# -100 <= Node.val <= 100
# l1 和 l2 均按 非递减顺序 排列
#
#
#

# @lcpr-template-start
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

    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2
        
        node = None
        if list1.val <= list2.val:
            node = list1
            node.next = self.mergeTwoLists(list1.next, list2)
        else:
            node = list2
            node.next = self.mergeTwoLists(list1, list2.next)

        return node


# @lc code=end


def list_to_link(l: List[int]) -> Optional[ListNode]:
    if len(l) == 0:
        return None

    head = ListNode(l[0])
    piont = head
    for i in range(1, len(l)):
        piont.next = ListNode(l[i])
        piont = piont.next

    return head


def link_to_list(lk: Optional[ListNode]) -> List[int]:
    if lk is None:
        return []

    l = []
    while lk:
        l.append(lk.val)
        lk = lk.next

    return l


tests = [[[1, 2, 4], [1, 3, 4]], [[], []], [[], [0]]]
ans = [[1, 1, 2, 3, 4, 4], [], [0]]
for i, (t, a) in enumerate(zip(tests, ans)):
    lk1 = list_to_link(t[0])
    lk2 = list_to_link(t[1])
    res = Solution().mergeTwoLists(lk1, lk2)
    res_list = link_to_list(res)
    print(f"test case {i+1}:\n"
          f"\ttest = {t[0]}, {t[1]};\n"
          f"\tans = {a};\n"
          f"\tres = {res_list};\n"
          f"\t{a == res_list}.")

#
# @lcpr case=start
# [1,2,4]\n[1,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n[]\n
# @lcpr case=end

# @lcpr case=start
# []\n[0]\n
# @lcpr case=end

#
