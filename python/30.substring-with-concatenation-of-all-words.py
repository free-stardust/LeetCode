#
# @lc app=leetcode.cn id=30 lang=python3
# @lcpr version=30204
#
# [30] 串联所有单词的子串
#
# https://leetcode.cn/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (38.71%)
# Likes:    1134
# Dislikes: 0
# Total Accepted:    216.3K
# Total Submissions: 559.3K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# 给定一个字符串 s 和一个字符串数组 words。 words 中所有字符串 长度相同。
#
# s 中的 串联子串 是指一个包含  words 中所有字符串以任意顺序排列连接起来的子串。
#
#
# 例如，如果 words = ["ab","cd","ef"]， 那么 "abcdef"， "abefcd"，"cdabef"，
# "cdefab"，"efabcd"， 和 "efcdab" 都是串联子串。 "acdbef" 不是串联子串，因为他不是任何 words 排列的连接。
#
#
# 返回所有串联子串在 s 中的开始索引。你可以以 任意顺序 返回答案。
#
#
#
# 示例 1：
#
# 输入：s = "barfoothefoobarman", words = ["foo","bar"]
# 输出：[0,9]
# 解释：因为 words.length == 2 同时 words[i].length == 3，连接的子字符串的长度必须为 6。
# 子串 "barfoo" 开始位置是 0。它是 words 中以 ["bar","foo"] 顺序排列的连接。
# 子串 "foobar" 开始位置是 9。它是 words 中以 ["foo","bar"] 顺序排列的连接。
# 输出顺序无关紧要。返回 [9,0] 也是可以的。
#
#
# 示例 2：
#
# 输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# 输出：[]
# 解释：因为 words.length == 4 并且 words[i].length == 4，所以串联子串的长度必须为 16。
# s 中没有子串长度为 16 并且等于 words 的任何顺序排列的连接。
# 所以我们返回一个空数组。
#
#
# 示例 3：
#
# 输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# 输出：[6,9,12]
# 解释：因为 words.length == 3 并且 words[i].length == 3，所以串联子串的长度必须为 9。
# 子串 "foobarthe" 开始位置是 6。它是 words 中以 ["foo","bar","the"] 顺序排列的连接。
# 子串 "barthefoo" 开始位置是 9。它是 words 中以 ["bar","the","foo"] 顺序排列的连接。
# 子串 "thefoobar" 开始位置是 12。它是 words 中以 ["the","foo","bar"] 顺序排列的连接。
#
#
#
# 提示：
#
#
# 1 <= s.length <= 10^4
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# words[i] 和 s 由小写英文字母组成
#
#
#

# @lcpr-template-start
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush


# @lcpr-template-end
# @lc code=start
class Solution:

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        s_len, word_len, words_len = len(s), len(words[0]),  len(words)
        window = word_len * words_len
        if s_len < window:
            return []
        
        cnt = {word:0 for word in words}
        word_cnt = cnt.copy()
        for word in words:
            word_cnt[word] += 1
    
        ans = []
        start = 0
        while start < s_len - window + 1:
            tmp_cnt = cnt.copy()
            for i in range(start, start + window, word_len):
                tmp_word = s[i:i+word_len]
                if tmp_word in tmp_cnt:
                    tmp_cnt[tmp_word] += 1
                else:
                    break
            if tmp_cnt == word_cnt:
                ans .append(start)
            start += 1
        
        return ans


# @lc code=end

tests = [["barfoothefoobarman", ["foo", "bar"]],
         ["wordgoodgoodgoodbestword", ["word", "good", "best", "word"]],
         ["barfoofoobarthefoobarman", ["bar", "foo", "the"]],
         ["wordgoodgoodgoodbestword", ["word","good","best","good"]]]
ans = [[0, 9], [], [6, 9, 12], [8]]
for i,(t,a) in enumerate(zip(tests, ans)):
    res = Solution().findSubstring(t[0], t[1])
    print(f"test case {i+1}:\n"
          f"\ttest = '{t[0]}', {t[1]};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res}.")


#
# @lcpr case=start
# "barfoothefoobarman"\n["foo","bar"]\n
# @lcpr case=end

# @lcpr case=start
# "wordgoodgoodgoodbestword"\n["word","good","best","word"]\n
# @lcpr case=end

# @lcpr case=start
# "barfoofoobarthefoobarman"\n["bar","foo","the"]\n
# @lcpr case=end

#
