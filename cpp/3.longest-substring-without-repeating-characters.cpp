/*
 * @lc app=leetcode.cn id=3 lang=cpp
 * @lcpr version=30202
 *
 * [3] 无重复字符的最长子串
 *
 * https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
 *
 * algorithms
 * Medium (39.79%)
 * Likes:    10154
 * Dislikes: 0
 * Total Accepted:    2.9M
 * Total Submissions: 7.2M
 * Testcase Example:  '"abcabcbb"'
 *
 * 给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
 * 
 * 
 * 
 * 示例 1:
 * 
 * 输入: s = "abcabcbb"
 * 输出: 3 
 * 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
 * 
 * 
 * 示例 2:
 * 
 * 输入: s = "bbbbb"
 * 输出: 1
 * 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
 * 
 * 
 * 示例 3:
 * 
 * 输入: s = "pwwkew"
 * 输出: 3
 * 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
 * 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 0 <= s.length <= 5 * 10^4
 * s 由英文字母、数字、符号和空格组成
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
    int lengthOfLongestSubstring(string s) {
        return dp_solution(s);
    }

    int official_solution(string s) {
        unordered_set<char> set;
        int s_len = s.size();
        int cur_pos = -1, max_len = 0;
        for (int i = 0; i < s_len; i++) {
            if (i != 0) {
                set.erase(s[i-1]);
            }
            while (cur_pos + 1 < s_len && !set.count(s[cur_pos + 1])) {
                set.insert(s[cur_pos + 1]);
                cur_pos++;
            }
            max_len = max(max_len, cur_pos - i + 1);
        }
        return max_len;
    }

    int optimized_solution(string s) {
        unordered_map<char, int> dic;
        int left = -1, max_len = 0, s_len = s.size();
        for (int i = 0; i < s_len; i++) {
            if(dic.find(s[i]) != dic.end()) {
                left = max(left, dic.find(s[i])->second);
            }
            dic[s[i]] = i;
            max_len = max(max_len, i - left);
        }
        return max_len;
    }

    int dp_solution(string s) {
        unordered_map<char, int> dic;
        int max_len = 0, tmp = 0, s_len = s.size(), same = 0;
        for (int i = 0; i < s_len; i++) {
            if(dic.find(s[i]) == dic.end())
                same = -1;
            else
                same = dic.find(s[i])->second;
            dic[s[i]] = i;
            tmp = tmp < i - same ? tmp + 1 : i - same;
            max_len = max(max_len, tmp);
        }
        return max_len;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "abcabcbb"\n
// @lcpr case=end

// @lcpr case=start
// "bbbbb"\n
// @lcpr case=end

// @lcpr case=start
// "pwwkew"\n
// @lcpr case=end

 */

