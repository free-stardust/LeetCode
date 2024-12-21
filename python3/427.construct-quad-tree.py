#
# @lc app=leetcode.cn id=427 lang=python3
# @lcpr version=30204
#
# [427] 建立四叉树
#
# https://leetcode.cn/problems/construct-quad-tree/description/
#
# algorithms
# Medium (72.67%)
# Likes:    220
# Dislikes: 0
# Total Accepted:    41.3K
# Total Submissions: 56.9K
# Testcase Example:  '[[0,1],[1,0]]'
#
# 给你一个 n * n 矩阵 grid ，矩阵由若干 0 和 1 组成。请你用四叉树表示该矩阵 grid 。
#
# 你需要返回能表示矩阵 grid 的 四叉树 的根结点。
#
# 四叉树数据结构中，每个内部节点只有四个子节点。此外，每个节点都有两个属性：
#
#
# val：储存叶子结点所代表的区域的值。1 对应 True，0 对应 False。注意，当 isLeaf 为 False 时，你可以把 True 或者
# False 赋值给节点，两种值都会被判题机制 接受 。
# isLeaf: 当这个节点是一个叶子结点时为 True，如果它有 4 个子节点则为 False 。
#
#
# class Node {
# ⁠   public boolean val;
# public boolean isLeaf;
# public Node topLeft;
# public Node topRight;
# public Node bottomLeft;
# public Node bottomRight;
# }
#
# 我们可以按以下步骤为二维区域构建四叉树：
#
#
# 如果当前网格的值相同（即，全为 0 或者全为 1），将 isLeaf 设为 True ，将 val 设为网格相应的值，并将四个子节点都设为 Null
# 然后停止。
# 如果当前网格的值不同，将 isLeaf 设为 False， 将 val 设为任意值，然后如下图所示，将当前网格划分为四个子网格。
# 使用适当的子网格递归每个子节点。
#
#
#
#
# 如果你想了解更多关于四叉树的内容，可以参考 wiki 。
#
# 四叉树格式：
#
# 你不需要阅读本节来解决这个问题。只有当你想了解输出格式时才会这样做。输出为使用层序遍历后四叉树的序列化形式，其中 null
# 表示路径终止符，其下面不存在节点。
#
# 它与二叉树的序列化非常相似。唯一的区别是节点以列表形式表示 [isLeaf, val] 。
#
# 如果 isLeaf 或者 val 的值为 True ，则表示它在列表 [isLeaf, val] 中的值为 1 ；如果 isLeaf 或者 val 的值为
# False ，则表示值为 0 。
#
#
#
# 示例 1：
#
#
#
# 输入：grid = [[0,1],[1,0]]
# 输出：[[0,1],[1,0],[1,1],[1,1],[1,0]]
# 解释：此示例的解释如下：
# 请注意，在下面四叉树的图示中，0 表示 false，1 表示 True 。
#
#
#
# 示例 2：
#
#
#
# 输入：grid =
# [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
#
# 输出：[[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
# 解释：网格中的所有值都不相同。我们将网格划分为四个子网格。
# topLeft，bottomLeft 和 bottomRight 均具有相同的值。
# topRight 具有不同的值，因此我们将其再分为 4 个子网格，这样每个子网格都具有相同的值。
# 解释如下图所示：
#
#
#
#
#
# 提示：
#
#
# n == grid.length == grid[i].length
# n == 2^x 其中 0 <= x <= 6
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
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Node:

    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:

    def binary(self, grid: List[List[int]]) -> 'Node':
        sum_gird = sum(sum(row) for row in grid)
        if sum_gird == 0 or sum_gird == len(grid)**2:
            return Node(grid[0][0], True, None, None, None, None)
        half = len(grid) // 2
        tL = self.construct([row[:half] for row in grid[:half]])
        tR = self.construct([row[half:] for row in grid[:half]])
        bL = self.construct([row[:half] for row in grid[half:]])
        bR = self.construct([row[half:] for row in grid[half:]])
        return Node(grid[0][0], False, tL, tR, bL, bR)

    def binary2(self, grid: List[List[int]]) -> 'Node':
        # 判断网格所有元素是否相同
        def f(grid):
            for i in grid:
                if i != grid[0]: return False
            return len(set(grid[0])) == 1

        if f(grid):
            return Node(grid[0][0], 1, None, None, None, None)
        l = len(grid) // 2
        # 不相同切分为 左上，右上， 左下，右下四个网格作为子树
        grid1 = [i[:l] for i in grid[:l]]
        grid2 = [i[l:len(grid)] for i in grid[:l]]
        grid3 = [i[:l] for i in grid[l:len(grid)]]
        grid4 = [i[l:len(grid)] for i in grid[l:len(grid)]]
        return Node(1, 0, self.construct(grid1), self.construct(grid2),
                    self.construct(grid3), self.construct(grid4))

    def construct(self, grid: List[List[int]]) -> 'Node':
        # return self.binary(grid)
        return self.binary2(grid)


# @lc code=end

#
# @lcpr case=start
# [[0,1],[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]\n
# @lcpr case=end

#