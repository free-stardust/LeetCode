/*
 * @lc app=leetcode.cn id=42 lang=cpp
 * @lcpr version=30204
 *
 * [42] 接雨水
 *
 * https://leetcode.cn/problems/trapping-rain-water/description/
 *
 * algorithms
 * Hard (63.91%)
 * Likes:    5254
 * Dislikes: 0
 * Total Accepted:    1M
 * Total Submissions: 1.6M
 * Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
 *
 * 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
 *
 *
 *
 * 示例 1：
 *
 *
 *
 * 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
 * 输出：6
 * 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
 *
 *
 * 示例 2：
 *
 * 输入：height = [4,2,0,3,2,5]
 * 输出：9
 *
 *
 *
 *
 * 提示：
 *
 *
 * n == height.length
 * 1 <= n <= 2 * 10^4
 * 0 <= height[i] <= 10^5
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
    int doublePoint(vector<int> &height) {
        int res = 0;
        int left = 0, right = height.size() - 1;
        int left_max = 0, right_max = 0;

        while (left < right) {
            left_max = max(left_max, height[left]);
            right_max = max(right_max, height[right]);
            if (left_max < right_max)
                res += left_max - height[left++];
            else
                res += right_max - height[right--];
        }

        return res;
    }

    int bioDirection(vector<int> &height) {
        int n = height.size();

        vector<int> left_max(n);
        left_max[0] = height[0];
        for (int i = 1; i < n; i++) {
            left_max[i] = max(left_max[i - 1], height[i]);
        }

        vector<int> right_max(n);
        right_max[n - 1] = height[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            right_max[i] = max(right_max[i + 1], height[i]);
        }

        int res = 0;
        for (int i = 0; i < n; i++)
            res += min(left_max[i], right_max[i]) - height[i];

        return res;
    }

    int monotonicStack(vector<int> &height) {
        int res = 0;
        stack<int> st;

        for (int i = 0; i < height.size(); i++) {
            while (!st.empty() && height[i] >= height[st.top()]) {
                int bottom_h = height[st.top()];
                st.pop();

                if (st.empty())
                    break;

                int left = st.top();
                int dh = min(height[left], height[i]) - bottom_h;
                res += dh * (i - left - 1);
            }
            st.push(i);
        }

        return res;
    }

    int trap(vector<int> &height) {
        // return doublePoint(height);
        // return bioDirection(height);
        return monotonicStack(height);
    }
};
// @lc code=end

/*
// @lcpr case=start
// [0,1,0,2,1,0,1,3,2,1,2,1]\n
// @lcpr case=end

// @lcpr case=start
// [4,2,0,3,2,5]\n
// @lcpr case=end

 */
