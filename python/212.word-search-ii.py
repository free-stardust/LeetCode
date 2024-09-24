#
# @lc app=leetcode.cn id=212 lang=python3
# @lcpr version=30204
#
# [212] 单词搜索 II
#
# https://leetcode.cn/problems/word-search-ii/description/
#
# algorithms
# Hard (43.12%)
# Likes:    894
# Dislikes: 0
# Total Accepted:    113.6K
# Total Submissions: 263.5K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
#   '["oath","pea","eat","rain"]'
#
# 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words， 返回所有二维网格上的单词 。
#
# 单词必须按照字母顺序，通过 相邻的单元格
# 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
#
#
#
# 示例 1：
#
# 输入：board =
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# words = ["oath","pea","eat","rain"]
# 输出：["eat","oath"]
#
#
# 示例 2：
#
# 输入：board = [["a","b"],["c","d"]], words = ["abcb"]
# 输出：[]
#
#
#
#
# 提示：
#
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] 是一个小写英文字母
# 1 <= words.length <= 3 * 10^4
# 1 <= words[i].length <= 10
# words[i] 由小写英文字母组成
# words 中的所有字符串互不相同
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
class TrieNode:

    def __init__(self) -> None:
        self.children = collections.defaultdict(TrieNode)
        self.word = ""
        self.is_word = False

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.is_word = True
        cur.word = word


class Solution:

    def use_wordtree_dfs(self, board: List[List[str]],
                         words: List[str]) -> List[str]:
        ans = set()
        rows, cols = len(board), len(board[0])
        trie = TrieNode()
        for word in words:
            trie.insert(word)

        def dfs(node, row, col):
            if board[row][col] not in node.children:
                return

            ch = board[row][col]

            node = node.children[ch]
            if node.word != "":
                ans.add(node.word)

            board[row][col] = "#"
            for r, c in [(row + 1, col), (row - 1, col), (row, col + 1),
                         (row, col - 1)]:
                if 0 <= r < rows and 0 <= c < cols:
                    dfs(node, r, c)
            board[row][col] = ch

        return list(ans)

    def use_trietree_dfs2(self, board: List[List[str]],
                          words: List[str]) -> List[str]:
        ans = []
        rows, cols = len(board), len(board[0])
        trie = TrieNode()
        for word in words:
            trie.insert(word)

        def dfs(node: Optional[TrieNode], row, col):
            if board[row][col] not in node.children:
                return

            ch = board[row][col]

            next_node = node.children[ch]
            if next_node.word != "":
                ans.append(next_node.word)
                next_node.word = ""

            if next_node.children:
                board[row][col] = "#"
                for r, c in [(row + 1, col), (row - 1, col), (row, col + 1),
                             (row, col - 1)]:
                    if 0 <= r < rows and 0 <= c < cols:
                        dfs(next_node, r, c)
                board[row][col] = ch

            if not next_node.children:
                node.children.pop(ch)

        for row in range(rows):
            for col in range(cols):
                dfs(trie, row, col)

        return ans

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # return self.use_wordtree_dfs(board, words)
        return self.use_trietree_dfs2(board, words)


# @lc code=end

#
# @lcpr case=start
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n["oath","pea","eat","rain"]\n
# @lcpr case=end

# @lcpr case=start
# [["a","b"],["c","d"]]\n["abcb"]\n
# @lcpr case=end

#
