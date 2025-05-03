/*
 * @lc app=leetcode.cn id=22 lang=cpp
 * @lcpr version=30204
 *
 * [22] 括号生成
 *
 * https://leetcode.cn/problems/generate-parentheses/description/
 *
 * algorithms
 * Medium (77.91%)
 * Likes:    3649
 * Dislikes: 0
 * Total Accepted:    880.2K
 * Total Submissions: 1.1M
 * Testcase Example:  '3'
 *
 * 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
 *
 *
 *
 * 示例 1：
 *
 * 输入：n = 3
 * 输出：["((()))","(()())","(())()","()(())","()()()"]
 *
 *
 * 示例 2：
 *
 * 输入：n = 1
 * 输出：["()"]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= n <= 8
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
    vector<string> dp(int n) {
        if (n == 0)
            return {};

        vector<vector<string>> dp = {{""}, {"()"}};

        for (int i = 2; i < n + 1; i++) {
            vector<string> tmp;
            for (int j = 0; j < i; j++) {
                vector<string> left = dp[j];
                vector<string> right = dp[i - 1 - j];

                for (string s1 : left) {
                    for (string s2 : right) {
                        tmp.push_back("(" + s1 + ")" + s2);
                    }
                }
            }
            dp.push_back(tmp);
        }

        return dp[n];
    }

    vector<string> backtrace(int n) {
        int s_len = n * 2;
        vector<string> res;
        string path(s_len, 0);

        auto dfs = [&](auto &&self, int pos, int open) {
            if (pos == s_len) {
                res.emplace_back(path);
                return;
            }

            if (open < n) {
                path[pos] = '(';
                self(self, pos + 1, open + 1);
            }

            if (pos - open < open) {
                path[pos] = ')';
                self(self, pos + 1, open);
            }
        };

        dfs(dfs, 0, 0);

        return res;
    }

    vector<string> generateParenthesis(int n) {
        // return dp(n);
        return backtrace(n);
    }
};
// @lc code=end
int main() {
    vector<string> s = {};
    for (string s1 : s) {
        cout << "test" << endl;
        cout << s1 << endl;
    }
    return 0;
}
/*
// @lcpr case=start
// 3\n
// @lcpr case=end

// @lcpr case=start
// 1\n
// @lcpr case=end

 */
