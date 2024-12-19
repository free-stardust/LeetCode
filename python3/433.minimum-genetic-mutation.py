#
# @lc app=leetcode.cn id=433 lang=python3
# @lcpr version=30204
#
# [433] 最小基因变化
#
# https://leetcode.cn/problems/minimum-genetic-mutation/description/
#
# algorithms
# Medium (54.54%)
# Likes:    310
# Dislikes: 0
# Total Accepted:    78.6K
# Total Submissions: 144K
# Testcase Example:  '"AACCGGTT"\n"AACCGGTA"\n["AACCGGTA"]'
#
# 基因序列可以表示为一条由 8 个字符组成的字符串，其中每个字符都是 'A'、'C'、'G' 和 'T' 之一。
#
# 假设我们需要调查从基因序列 start 变为 end 所发生的基因变化。一次基因变化就意味着这个基因序列中的一个字符发生了变化。
#
#
# 例如，"AACCGGTT" --> "AACCGGTA" 就是一次基因变化。
#
#
# 另有一个基因库 bank 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。（变化后的基因必须位于基因库 bank 中）
#
# 给你两个基因序列 start 和 end ，以及一个基因库 bank ，请你找出并返回能够使 start 变化为 end
# 所需的最少变化次数。如果无法完成此基因变化，返回 -1 。
#
# 注意：起始基因序列 start 默认是有效的，但是它并不一定会出现在基因库中。
#
#
#
# 示例 1：
#
# 输入：start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
# 输出：1
#
#
# 示例 2：
#
# 输入：start = "AACCGGTT", end = "AAACGGTA", bank =
# ["AACCGGTA","AACCGCTA","AAACGGTA"]
# 输出：2
#
#
# 示例 3：
#
# 输入：start = "AAAAACCC", end = "AACCCCCC", bank =
# ["AAAACCCC","AAACCCCC","AACCCCCC"]
# 输出：3
#
#
#
#
# 提示：
#
#
# start.length == 8
# end.length == 8
# 0 <= bank.length <= 10
# bank[i].length == 8
# start、end 和 bank[i] 仅由字符 ['A', 'C', 'G', 'T'] 组成
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
class Solution:

    def copilot_solution(self, startGene: str, endGene: str,
                         bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        queue = collections.deque([(startGene, 0)])
        visited = set([startGene])
        while queue:
            gene, step = queue.popleft()
            if gene == endGene:
                return step
            for i in range(8):
                for c in 'ACGT':
                    new_gene = gene[:i] + c + gene[i + 1:]
                    if new_gene in bank and new_gene not in visited:
                        queue.append((new_gene, step + 1))
                        visited.add(new_gene)
        return -1

    def ex_solution(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        queue = collections.deque([(startGene, 0)])
        visited = set([startGene])
        while queue:
            gene, step = queue.popleft()
            if gene == endGene:
                return step
            for i in range(8):
                for c in 'ACGT':
                    new_gene = gene[:i] + c + gene[i + 1:]
                    if new_gene in bank and new_gene not in visited:
                        queue.append((new_gene, step + 1))
                        visited.add(new_gene)
        return -1

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # return self.copilot_solution(startGene, endGene, bank)
        return self.ex_solution(startGene, endGene, bank)


# @lc code=end

#
# @lcpr case=start
# "AACCGGTT"\n"AACCGGTA"\n["AACCGGTA"]\n
# @lcpr case=end

# @lcpr case=start
# "AACCGGTT"\n"AAACGGTA"\n["AACCGGTA","AACCGCTA","AAACGGTA"]\n
# @lcpr case=end

# @lcpr case=start
# "AAAAACCC"\n"AACCCCCC"\n["AAAACCCC","AAACCCCC","AACCCCCC"]\n
# @lcpr case=end

#
