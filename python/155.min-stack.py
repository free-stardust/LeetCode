#
# @lc app=leetcode.cn id=155 lang=python3
# @lcpr version=30204
#
# [155] 最小栈
#
# https://leetcode.cn/problems/min-stack/description/
#
# algorithms
# Medium (60.12%)
# Likes:    1815
# Dislikes: 0
# Total Accepted:    632.2K
# Total Submissions: 1M
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n' +
#   '[[],[-2],[0],[-3],[],[],[],[]]'
#
# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
#
# 实现 MinStack 类:
#
#
# MinStack() 初始化堆栈对象。
# void push(int val) 将元素val推入堆栈。
# void pop() 删除堆栈顶部的元素。
# int top() 获取堆栈顶部的元素。
# int getMin() 获取堆栈中的最小元素。
#
#
#
#
# 示例 1:
#
# 输入：
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# 输出：
# [null,null,null,null,-3,null,0,-2]
#
# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
#
#
#
#
# 提示：
#
#
# -2^31 <= val <= 2^31 - 1
# pop、top 和 getMin 操作总是在 非空栈 上调用
# push, pop, top, and getMin最多被调用 3 * 10^4 次
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
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_styack = [math.inf]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_styack.append(min(val, self.min_styack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_styack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_styack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

#
# @lcpr case=start
# ["MinStack","push","push","push","getMin","pop","top","getMin"][[],[-2],[0],[-3],[],[],[],[]]\n
# @lcpr case=end

#
