#
# @lc app=leetcode.cn id=138 lang=python3
# @lcpr version=30204
#
# [138] 随机链表的复制
#
# https://leetcode.cn/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (67.60%)
# Likes:    1445
# Dislikes: 0
# Total Accepted:    326.1K
# Total Submissions: 480.4K
# Testcase Example:  '[[7,null],[13,0],[11,4],[10,2],[1,0]]'
#
# 给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。
#
# 构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random
# 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。
#
# 例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random
# --> y 。
#
# 返回复制链表的头节点。
#
# 用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：
#
#
# val：一个表示 Node.val 的整数。
# random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
#
#
# 你的代码 只 接受原链表的头节点 head 作为传入参数。
#
#
#
# 示例 1：
#
#
#
# 输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
#
#
# 示例 2：
#
#
#
# 输入：head = [[1,1],[2,1]]
# 输出：[[1,1],[2,1]]
#
#
# 示例 3：
#
#
#
# 输入：head = [[3,null],[3,0],[3,null]]
# 输出：[[3,null],[3,0],[3,null]]
#
#
#
#
# 提示：
#
#
# 0 <= n <= 1000
# -10^4 <= Node.val <= 10^4
# Node.random 为 null 或指向链表中的节点。
#
#
#
#
#

# @lcpr-template-start
import copy
import collections
import random
import math
from functools import reduce
from collections import namedtuple
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush
# @lcpr-template-end
# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Node:

    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:

    def recursion(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cache_ndoe = {}

        def copy_random_list(node: 'Optional[Node]') -> 'Optional[Node]':
            if not node:
                return None

            if (node not in cache_ndoe):
                new_node = Node(node.val)
                cache_ndoe[node] = new_node
                new_node.next = copy_random_list(node.next)
                new_node.random = copy_random_list(node.random)

            return cache_ndoe[node]

        return copy_random_list(head)

    def traverse(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_dict = {None: None}

        cur = head
        while cur:
            node_dict[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            node_dict[cur].next = node_dict[cur.next]
            node_dict[cur].random = node_dict[cur.random]
            cur = cur.next

        return node_dict[head]

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # return self.recursion(head)
        return self.traverse(head)


# @lc code=end

#
# @lcpr case=start
# [[7,null],[13,0],[11,4],[10,2],[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,null],[3,0],[3,null]]\n
# @lcpr case=end

#
