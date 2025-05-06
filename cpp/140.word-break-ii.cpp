/*
 * @lc app=leetcode.cn id=140 lang=cpp
 * @lcpr version=30204
 *
 * [140] 单词拆分 II
 *
 * https://leetcode.cn/problems/word-break-ii/description/
 *
 * algorithms
 * Hard (60.20%)
 * Likes:    783
 * Dislikes: 0
 * Total Accepted:    109.8K
 * Total Submissions: 182.1K
 * Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
 *
 * 给定一个字符串 s 和一个字符串字典 wordDict ，在字符串 s 中增加空格来构建一个句子，使得句子中所有的单词都在词典中。以任意顺序
 * 返回所有这些可能的句子。
 *
 * 注意：词典中的同一个单词可能在分段中被重复使用多次。
 *
 *
 *
 * 示例 1：
 *
 * 输入:s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
 * 输出:["cats and dog","cat sand dog"]
 *
 *
 * 示例 2：
 *
 * 输入:s = "pineapplepenapple", wordDict =
 * ["apple","pen","applepen","pine","pineapple"]
 * 输出:["pine apple pen apple","pineapple pen apple","pine applepen apple"]
 * 解释: 注意你可以重复使用字典中的单词。
 *
 *
 * 示例 3：
 *
 * 输入:s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
 * 输出:[]
 *
 *
 *
 *
 * 提示：
 *
 *
 *
 *
 * 1 <= s.length <= 20
 * 1 <= wordDict.length <= 1000
 * 1 <= wordDict[i].length <= 10
 * s 和 wordDict[i] 仅有小写英文字母组成
 * wordDict 中所有字符串都 不同
 *
 *
 */

// @lcpr-template-start
#include <algorithm>
#include <array>
#include <bitset>
#include <climits>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <queue>
#include <stack>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<string> backTrace(string s, vector<string> &wordDict) {
        int s_len = s.length();
        vector<string> ans;
        unordered_map<string, int> wordMap;

        for (int i = 0; i < wordDict.size(); i++) {
            wordMap.emplace(wordDict[i], i);
        }

        auto dfs = [&](auto &&self, string res, int start) {
            if (start == s_len) {
                if (res.length() > 0)
                    res = res.substr(0, res.length() - 1);
                ans.emplace_back(res);
                return;
            }

            string word = "";
            for (int i = start; i < s_len; i++) {
                word += s[i];
                if (wordMap.contains(word)) {
                    self(self, res + word + " ", i + 1);
                }
            }
        };

        dfs(dfs, "", 0);

        return ans;
    }
    vector<string> wordBreak(string s, vector<string> &wordDict) {
        return backTrace(s, wordDict);
    }
};
// @lc code=end

/*
// @lcpr case=start
// "catsanddog"\n["cat","cats","and","sand","dog"]\n
// @lcpr case=end

// @lcpr case=start
// "pineapplepenapple"\n["apple","pen","applepen","pine","pineapple"]\n
// @lcpr case=end

// @lcpr case=start
// "catsandog"\n["cats","dog","sand","and","cat"]\n
// @lcpr case=end

 */
