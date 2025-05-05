/*
 * @lc app=leetcode.cn id=32 lang=cpp
 * @lcpr version=30204
 *
 * [32] 最长有效括号
 *
 * https://leetcode.cn/problems/longest-valid-parentheses/description/
 *
 * algorithms
 * Hard (38.25%)
 * Likes:    2541
 * Dislikes: 0
 * Total Accepted:    470.1K
 * Total Submissions: 1.2M
 * Testcase Example:  '"(()"'
 *
 * 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
 *
 *
 *
 *
 *
 * 示例 1：
 *
 * 输入：s = "(()"
 * 输出：2
 * 解释：最长有效括号子串是 "()"
 *
 *
 * 示例 2：
 *
 * 输入：s = ")()())"
 * 输出：4
 * 解释：最长有效括号子串是 "()()"
 *
 *
 * 示例 3：
 *
 * 输入：s = ""
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0 <= s.length <= 3 * 10^4
 * s[i] 为 '(' 或 ')'
 *
 *
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
    int dp(string s) {
        int size = s.length(), res = 0;
        vector<int> dp(size, 0);

        for (int i = 1; i < size; i++) {
            if (s[i] == ')') {
                if (s[i - 1] == '(') {
                    dp[i] = 2;
                    if (i - 2 >= 0)
                        dp[i] = dp[i] + dp[i - 2];
                } else if (dp[i - 1] > 0) {
                    if (i - dp[i - 1] - 1 >= 0 && s[i - dp[i - 1] - 1] == '(') {
                        dp[i] = dp[i - 1] + 2;
                        if (i - dp[i - 1] - 2 >= 0)
                            dp[i] = dp[i] + dp[i - dp[i - 1] - 2];
                    }
                }
            }
            res = max(res, dp[i]);
        }

        return res;
    }

    int noExtentSpace(string s) {
        int left = 0, right = 0, res = 0;

        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(')
                left++;
            else
                right++;

            if (left == right)
                res = max(res, left + right);
            else if (left < right)
                left = right = 0;
        }

        left = right = 0;

        for (int i = s.size() - 1; i >= 0; i--) {
            if (s[i] == '(')
                left++;
            else
                right++;

            if (left == right)
                res = max(res, left + right);
            else if (left > right)
                left = right = 0;
        }

        return res;
    }

    int useStack(string s) {
        int res = 0;
        stack<int> st;
        st.push(-1);

        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(')
                st.push(i);
            else {
                st.pop();
                if (st.empty())
                    st.push(i);
                else
                    res = max(res, i - st.top());
            }
        }

        return res;
    }

    int longestValidParentheses(string s) {
        // return useStack(s);
        return noExtentSpace(s);
        // return dp(s);
    }
};
// @lc code=end

/*
// @lcpr case=start
// "())()()(()"\n
// @lcpr case=end

// @lcpr case=start
// "(()"\n
// @lcpr case=end

// @lcpr case=start
// ")()())"\n
// @lcpr case=end

// @lcpr case=start
// ""\n
// @lcpr case=end

// @lcpr case=start
// "()(()"\n
// @lcpr case=end

 */
