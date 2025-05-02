/*
 * @lc app=leetcode.cn id=5 lang=cpp
 * @lcpr version=30204
 *
 * [5] 最长回文子串
 *
 * https://leetcode.cn/problems/longest-palindromic-substring/description/
 *
 * algorithms
 * Medium (38.34%)
 * Likes:    7223
 * Dislikes: 0
 * Total Accepted:    1.7M
 * Total Submissions: 4.5M
 * Testcase Example:  '"babad"'
 *
 * 给你一个字符串 s，找到 s 中最长的 回文 子串。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 输入：s = "babad"
 * 输出："bab"
 * 解释："aba" 同样是符合题意的答案。
 * 
 * 
 * 示例 2：
 * 
 * 输入：s = "cbbd"
 * 输出："bb"
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= s.length <= 1000
 * s 仅由数字和英文字母组成
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
    pair<int, int> expand_around_center(const string &s, int left, int right) {
        while (left >= 0 && right < s.size() && s[left] == s[right]) {
            left--;
            right++;
        }
        return {left + 1, right - 1};
    }

    string expand_around_center_main(string s){
        int start = 0, end = 0;

        for (int i = 0; i < s.size(); ++i) {
            pair<int, int> p1 = expand_around_center(s, i, i);
            pair<int, int> p2 = expand_around_center(s, i, i + 1);

            if (p1.second - p1.first > end - start) {
                start = p1.first;
                end = p1.second;
            }

            if (p2.second - p2.first > end - start) {
                start = p2.first;
                end = p2.second;
            }
            
        }

        return s.substr(start, end - start + 1);
    }

    string dp(string s) {
        int s_len = s.size();
        if (s_len < 2)  return s;

        int max_len = 1, begin = 0;
        vector<vector<bool>> dp(s_len, vector<bool>(s_len));

        for (int i = 0; i < s_len; ++i) {
            dp[i][i] = true;
        }

        for (int L = 2; L <= s_len; ++L) {
            for (int i = 0; i < s_len; ++i) {
                int j = i + L - 1;
                if (j >= s_len) break;
                
                if (s[i] != s[j])
                    dp[i][j] = false;
                else {
                    if (j - i < 3) {
                        dp[i][j] = true;
                    } else {
                        dp[i][j] = dp[i+1][j-1];
                    }
                }

                if (dp[i][j] && j - i + 1 > max_len) {
                    max_len = j - i + 1;
                    begin = i;
                }

            }
        }

        return s.substr(begin, max_len);
    }
    string longestPalindrome(string s) {
        // return dp(s);
        return expand_around_center_main(s);
    }
};
// @lc code=end

int main() {
    return 0;
 }

/*
// @lcpr case=start
// "babad"\n
// @lcpr case=end

// @lcpr case=start
// "cbbd"\n
// @lcpr case=end

 */

