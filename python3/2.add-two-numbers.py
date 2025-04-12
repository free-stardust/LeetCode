#
# @lc app=leetcode.cn id=2 lang=python3
# @lcpr version=30204
#
# [2] 两数相加
#
# https://leetcode.cn/problems/add-two-numbers/description/
#
# algorithms
# Medium (43.66%)
# Likes:    10598
# Dislikes: 0
# Total Accepted:    2.1M
# Total Submissions: 4.8M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
#
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
#
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
#
#
# 示例 1：
#
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
#
#
# 示例 2：
#
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#
#
# 示例 3：
#
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]
#
#
#
#
# 提示：
#
#
# 每个链表中的节点数在范围 [1, 100] 内
# 0 <= Node.val <= 9
# 题目数据保证列表表示的数字不含前导零
#
#
#

# @lcpr-template-start
from typing import List
from typing import Optional


# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __traverse__(self, l1: Optional[ListNode],
                     l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        node = result
        carry = 0
        while l1 or l2 or carry:
            sum_nums = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            node.next = ListNode(sum_nums % 10)
            node = node.next
            carry = sum_nums // 10
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return result.next

    def __recursion__(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1: return l2  # 如果 l1 为 None，则返回 l2
        if not l2: return l1  # 如果 l2 为 None，则返回 l1

        l1.val += l2.val  # 计算 l1 第一个元素和 l2 第一个元素的和并存于 l1 中
        if l1.val >= 10:  # 如果大于等于 10 则将当前 l1 的第一个节点和后续节点看作两个列表进行递归计算
            l1.next = self.__recursion__(ListNode(l1.val // 10), l1.next)
            l1.val %= 10

        l1.next = self.__recursion__(l1.next, l2.next)  # 继续 l1 和 l2 的剩余计算
        return l1

    def solution(self, l1: Optional[ListNode],
                 l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1: return l2
        if not l2: return l1

        l1.val += l2.val
        if l1.val >= 10:
            l1.next = self.solution(ListNode(l1.val // 10), l1.next)
            l1.val %= 10

        l1.next = self.solution(l1.next, l2.next)
        return l1

    def addTwoNumbers(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        # return self.__traverse__(l1, l2)
        return self.__recursion__(l1, l2)


# @lc code=end


def list2Link(l: List) -> ListNode:
    for i in range(len(l)):
        if i == 0:
            head = ListNode(l[i])
            node = head
        else:
            node.next = ListNode(l[i])
            node = node.next
    return head


def link2List(link: ListNode) -> List:
    l = []
    while link:
        l.append(link.val)
        link = link.next
    return l


l1 = [2, 4, 3]
l2 = [5, 6, 4]

l1 = list2Link(l1)
l2 = list2Link(l2)

result = link2List(Solution().addTwoNumbers(l1, l2))
print(result)

#
# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

# @lcpr case=start
# [9,9,9,9,9,9,9]\n[9,9,9,9]\n
# @lcpr case=end

#
