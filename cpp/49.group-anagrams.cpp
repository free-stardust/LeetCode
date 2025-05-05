/*
 * @lc app=leetcode.cn id=49 lang=cpp
 * @lcpr version=30204
 *
 * [49] 字母异位词分组
 *
 * https://leetcode.cn/problems/group-anagrams/description/
 *
 * algorithms
 * Medium (68.48%)
 * Likes:    1961
 * Dislikes: 0
 * Total Accepted:    785.6K
 * Total Submissions: 1.1M
 * Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
 *
 * 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
 *
 * 字母异位词 是由重新排列源单词的所有字母得到的一个新单词。
 *
 *
 *
 * 示例 1:
 *
 * 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
 * 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
 *
 * 示例 2:
 *
 * 输入: strs = [""]
 * 输出: [[""]]
 *
 *
 * 示例 3:
 *
 * 输入: strs = ["a"]
 * 输出: [["a"]]
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= strs.length <= 10^4
 * 0 <= strs[i].length <= 100
 * strs[i] 仅包含小写字母
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
#include <string>
#include <tuple>
#include <typeinfo>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<vector<string>> harshMap(vector<string> &strs) {
        vector<vector<string>> res;
        unordered_map<string, vector<string>> dict;

        for (string &s : strs) {
            string tmp_s = s;
            sort(tmp_s.begin(), tmp_s.end());
            dict[tmp_s].push_back(s);
        }

        for (auto &d : dict) {
            res.push_back(d.second);
        }

        return res;
    }
    vector<vector<string>> groupAnagrams(vector<string> &strs) {
        return harshMap(strs);
    }
};
// @lc code=end

int main() {
    string s = "eat";
    string s1 = s;
    sort(s1.begin(), s1.end());
    cout << s << "," << s1 << endl;
    cout << ('a' < 'b') << endl;

    unordered_map<string, vector<string>> dict = {
        {"aet", {"tea", "eat"}},
        {"atn", {"nat", "tan"}},
    };
    for (auto d : dict) {
        cout << d.first << endl;
    }
    return 0;
}

/*
// @lcpr case=start
// ["eat", "tea", "tan", "ate", "nat", "bat"]\n
// @lcpr case=end

// @lcpr case=start
// [""]\n
// @lcpr case=end

// @lcpr case=start
// ["a"]\n
// @lcpr case=end

 */
