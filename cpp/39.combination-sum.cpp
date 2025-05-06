/*
 * @lc app=leetcode.cn id=39 lang=cpp
 * @lcpr version=30204
 *
 * [39] 组合总和
 *
 * https://leetcode.cn/problems/combination-sum/description/
 *
 * algorithms
 * Medium (72.93%)
 * Likes:    2855
 * Dislikes: 0
 * Total Accepted:    995.4K
 * Total Submissions: 1.4M
 * Testcase Example:  '[2,3,6,7]\n7'
 *
 * 给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target
 * 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
 *
 * candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 
 *
 * 对于给定的输入，保证和为 target 的不同组合数少于 150 个。
 *
 *
 *
 * 示例 1：
 *
 * 输入：candidates = [2,3,6,7], target = 7
 * 输出：[[2,2,3],[7]]
 * 解释：
 * 2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
 * 7 也是一个候选， 7 = 7 。
 * 仅有这两种组合。
 *
 * 示例 2：
 *
 * 输入: candidates = [2,3,5], target = 8
 * 输出: [[2,2,2,2],[2,3,3],[3,5]]
 *
 * 示例 3：
 *
 * 输入: candidates = [2], target = 1
 * 输出: []
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= candidates.length <= 30
 * 2 <= candidates[i] <= 40
 * candidates 的所有元素 互不相同
 * 1 <= target <= 40
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
#include <iterator>
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
    vector<vector<int>> backTrace(vector<int> &candidates, int target) {
        vector<vector<int>> ans;
        int n = candidates.size();

        sort(candidates.begin(), candidates.end());
        auto dfs = [&](auto &&self, vector<int> res, int sum, int start) -> void {
            for (int i = start; i < n; i++) {
                sum += candidates[i];
                res.push_back(candidates[i]);
                if (sum == target) {
                    ans.push_back(res);
                } else if (sum < target) {
                    self(self, res, sum, i);
                } else {
                    break;
                }
                sum -= candidates[i];
                res.pop_back();
            }
        };

        dfs(dfs, {}, 0, 0);

        return ans;
    }

    vector<vector<int>> combinationSum(vector<int> &candidates, int target) {
        return backTrace(candidates, target);
    }
};
// @lc code=end

/*
// @lcpr case=start
// [2,3,6,7]\n7\n
// @lcpr case=end

// @lcpr case=start
// [2,3,5]\n8\n
// @lcpr case=end

// @lcpr case=start
// [2]\n1\n
// @lcpr case=end

 */
