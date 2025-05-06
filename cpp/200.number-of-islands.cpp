/*
 * @lc app=leetcode.cn id=200 lang=cpp
 * @lcpr version=30204
 *
 * [200] 岛屿数量
 *
 * https://leetcode.cn/problems/number-of-islands/description/
 *
 * algorithms
 * Medium (60.95%)
 * Likes:    2572
 * Dislikes: 0
 * Total Accepted:    908.7K
 * Total Submissions: 1.5M
 * Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
 *
 * 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
 *
 * 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
 *
 * 此外，你可以假设该网格的四条边均被水包围。
 *
 *
 *
 * 示例 1：
 *
 * 输入：grid = [
 * ⁠ ["1","1","1","1","0"],
 * ⁠ ["1","1","0","1","0"],
 * ⁠ ["1","1","0","0","0"],
 * ⁠ ["0","0","0","0","0"]
 * ]
 * 输出：1
 *
 *
 * 示例 2：
 *
 * 输入：grid = [
 * ⁠ ["1","1","0","0","0"],
 * ⁠ ["1","1","0","0","0"],
 * ⁠ ["0","0","1","0","0"],
 * ⁠ ["0","0","0","1","1"]
 * ]
 * 输出：3
 *
 *
 *
 *
 * 提示：
 *
 *
 * m == grid.length
 * n == grid[i].length
 * 1 <= m, n <= 300
 * grid[i][j] 的值为 '0' 或 '1'
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
    int backTrace(vector<vector<char>> &grid) {
        if (grid.size() == 0)
            return 0;

        int res = 0;
        int rows = grid.size(), cols = grid[0].size();
        vector<int> visits(rows * cols, 0);

        auto dfs = [&](auto &&self, int row, int col, int mark) {
            if (row < 0 || row == rows || col < 0 || col == cols)
                return;

            if (grid[row][col] == '0' || visits[row * cols + col] != 0)
                return;
            else {
                visits[row * cols + col] = mark;
                self(self, row - 1, col, mark);
                self(self, row + 1, col, mark);
                self(self, row, col - 1, mark);
                self(self, row, col + 1, mark);
            }
        };

        int mark = 1;
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (grid[row][col] == '1' && visits[row * cols + col] == 0) {
                    dfs(dfs, row, col, mark);
                    for (auto visit : visits) {
                        if (visit == mark) {
                            res += 1;
                            break;
                        }
                    }
                    mark++;
                }
            }
        }

        return res;
    }

    int numIslands(vector<vector<char>> &grid) {
        return backTrace(grid);
    }
};
// @lc code=end

/*
// @lcpr case=start
// [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]\n
// @lcpr case=end

// @lcpr case=start
// [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]\n
// @lcpr case=end

 */
