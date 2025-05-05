/*
 * @lc app=leetcode.cn id=51 lang=cpp
 * @lcpr version=30204
 *
 * [51] N 皇后
 *
 * https://leetcode.cn/problems/n-queens/description/
 *
 * algorithms
 * Hard (74.20%)
 * Likes:    2110
 * Dislikes: 0
 * Total Accepted:    425.5K
 * Total Submissions: 573.1K
 * Testcase Example:  '4'
 *
 * 按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
 *
 * n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
 *
 * 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
 *
 *
 *
 * 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
 *
 *
 *
 * 示例 1：
 *
 * 输入：n = 4
 * 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
 * 解释：如上图所示，4 皇后问题存在两个不同的解法。
 *
 *
 * 示例 2：
 *
 * 输入：n = 1
 * 输出：[["Q"]]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= n <= 9
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
    vector<vector<string>> zerox3f(int n) {
        vector<vector<string>> res;
        vector<int> rows(n);
        vector<int> cols(n), diag1(2 * n - 1), diag2(2 * n - 1);

        auto dfs = [&](auto &&self, int row) {
            if (row == n) {
                vector<string> board(n);
                for (int i = 0; i < n; i++) {
                    board[i] = string(rows[i], '.') + 'Q' + string(n - 1 - rows[i], '.');
                }
                res.push_back(board);
                return;
            }

            for (int col = 0; col < n; col++) {
                int row_col = row - col + n - 1;
                if (!cols[col] && !diag1[row + col] && !diag2[row_col]) {
                    rows[row] = col;
                    cols[col] = diag1[row + col] = diag2[row_col] = true;
                    self(self, row + 1);
                    cols[col] = diag1[row + col] = diag2[row_col] = false;
                }
            }
        };

        dfs(dfs, 0);

        return res;
    }

    vector<vector<string>> solveNQueens(int n) {
        return zerox3f(n);
    }
};
// @lc code=end

/*
// @lcpr case=start
// 4\n
// @lcpr case=end

// @lcpr case=start
// 1\n
// @lcpr case=end

 */
