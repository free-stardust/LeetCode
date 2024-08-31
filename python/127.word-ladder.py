#
# @lc app=leetcode.cn id=127 lang=python3
# @lcpr version=30204
#
# [127] 单词接龙
#
# https://leetcode.cn/problems/word-ladder/description/
#
# algorithms
# Hard (48.98%)
# Likes:    1397
# Dislikes: 0
# Total Accepted:    226.3K
# Total Submissions: 461.2K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 字典 wordList 中从单词 beginWord 到 endWord 的 转换序列 是一个按下述规格形成的序列 beginWord -> s1 ->
# s2 -> ... -> sk：
#
#
# 每一对相邻的单词只差一个字母。
# 对于 1 <= i <= k 时，每个 si 都在 wordList 中。注意， beginWord 不需要在 wordList 中。
# sk == endWord
#
#
# 给你两个单词 beginWord 和 endWord 和一个字典 wordList ，返回 从 beginWord 到 endWord 的 最短转换序列
# 中的 单词数目 。如果不存在这样的转换序列，返回 0 。
#
#
# 示例 1：
#
# 输入：beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log","cog"]
# 输出：5
# 解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。
#
#
# 示例 2：
#
# 输入：beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log"]
# 输出：0
# 解释：endWord "cog" 不在字典中，所以无法进行转换。
#
#
#
# 提示：
#
#
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord、endWord 和 wordList[i] 由小写英文字母组成
# beginWord != endWord
# wordList 中的所有字符串 互不相同
#
#
#

# @lcpr-template-start
import copy
import collections
import random
import math
from collections import namedtuple
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush


# @lcpr-template-end
# @lc code=start
class Solution:

    def solution1(self, beginWord: str, endWord: str,
                  wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        word_id = dict()
        edge = collections.defaultdict(list)
        node_num = 0

        def add_word(word: str):
            if word not in word_id:
                nonlocal node_num
                word_id[word] = node_num
                node_num += 1

        def add_edge(word: str):
            add_word(word)
            id1 = word_id[word]
            chars = list(word)
            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = "*"
                new_word = "".join(chars)
                add_word(new_word)
                id2 = word_id[new_word]
                edge[id1].append(id2)
                edge[id2].append(id1)
                chars[i] = tmp

        for word in wordList:
            add_edge(word)

        add_edge(beginWord)

        dis = [float("inf")] * node_num
        begin_id, end_id = word_id[beginWord], word_id[endWord]
        dis[begin_id] = 0

        queue = collections.deque([begin_id])
        while queue:
            x = queue.popleft()
            if x == end_id:
                return dis[end_id] // 2 + 1
            for it in edge[x]:
                if dis[it] == float("inf"):
                    dis[it] = dis[x] + 1
                    queue.append(it)

        return 0

    def solution2(self, beginWord: str, endWord: str,
                  wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        word_id = dict()
        edge = collections.defaultdict(list)
        node_num = 0

        def add_word(word: str):
            if word not in word_id:
                nonlocal node_num
                word_id[word] = node_num
                node_num += 1

        def add_edge(word: str):
            add_word(word)
            id1 = word_id[word]
            chars = list(word)
            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = "*"
                new_word = "".join(chars)
                add_word(new_word)
                id2 = word_id[new_word]
                edge[id1].append(id2)
                edge[id2].append(id1)
                chars[i] = tmp

        for word in wordList:
            add_edge(word)

        add_edge(beginWord)

        dis_begin = [float("inf")] * node_num
        begin_id = word_id[beginWord]
        dis_begin[begin_id] = 0
        que_begin = collections.deque([begin_id])

        dis_end = [float("inf")] * node_num
        end_id = word_id[endWord]
        dis_end[end_id] = 0
        que_end = collections.deque([end_id])

        while que_begin or que_end:
            que_begin_size = len(que_begin)
            for _ in range(que_begin_size):
                node_begin = que_begin.popleft()
                if dis_end[node_begin] != float("inf"):
                    return (dis_begin[node_begin] +
                            dis_end[node_begin]) // 2 + 1
                for it in edge[node_begin]:
                    if dis_begin[it] == float("inf"):
                        dis_begin[it] = dis_begin[node_begin] + 1
                        que_begin.append(it)

            que_end_size = len(que_end)
            for _ in range(que_end_size):
                node_end = que_end.popleft()
                if dis_begin[node_end] != float("inf"):
                    return (dis_begin[node_end] + dis_end[node_end]) // 2 + 1
                for it in edge[node_end]:
                    if dis_end[it] == float("inf"):
                        dis_end[it] = dis_end[node_end] + 1
                        que_end.append(it)
        return 0

    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:
        # return self.solution1(beginWord, endWord, wordList)
        return self.solution2(beginWord, endWord, wordList)


# @lc code=end

tests = [["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]],
         ["hit", "cog", ["hot", "dot", "dog", "lot", "log"]]]
ans = [5, 0]
all_pass = True
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().ladderLength(t[0], t[1], t[2])
    print(f"testcase {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res};")
    all_pass &= (a == res)
print(f"all pass: {all_pass}.")
#
# @lcpr case=start
# "hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]\n
# @lcpr case=end

# @lcpr case=start
# "hit"\n"cog"\n["hot","dot","dog","lot","log"]\n
# @lcpr case=end

#
