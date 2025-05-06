/*
 * @lc app=leetcode.cn id=321 lang=cpp
 * @lcpr version=30204
 *
 * [321] 拼接最大数
 *
 * https://leetcode.cn/problems/create-maximum-number/description/
 *
 * algorithms
 * Hard (42.37%)
 * Likes:    608
 * Dislikes: 0
 * Total Accepted:    45.8K
 * Total Submissions: 108K
 * Testcase Example:  '[3,4,6,5]\n[9,1,2,5,8,3]\n5'
 *
 * 给你两个整数数组 nums1 和 nums2，它们的长度分别为 m 和 n。数组 nums1 和 nums2
 * 分别代表两个数各位上的数字。同时你也会得到一个整数 k。
 *
 * 请你利用这两个数组中的数字创建一个长度为 k <= m + n 的最大数。同一数组中数字的相对顺序必须保持不变。
 *
 * 返回代表答案的长度为 k 的数组。
 *
 *
 *
 * 示例 1：
 *
 * 输入：nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5
 * 输出：[9,8,6,5,3]
 *
 *
 * 示例 2：
 *
 * 输入：nums1 = [6,7], nums2 = [6,0,4], k = 5
 * 输出：[6,7,6,0,4]
 *
 *
 * 示例 3：
 *
 * 输入：nums1 = [3,9], nums2 = [8,9], k = 3
 * 输出：[9,8,9]
 *
 *
 *
 *
 * 提示：
 *
 *
 * m == nums1.length
 * n == nums2.length
 * 1 <= m, n <= 500
 * 0 <= nums1[i], nums2[i] <= 9
 * 1 <= k <= m + n
 * nums1 和 nums2 没有前导 0。
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
    vector<int> dp(vector<int> &nums1, vector<int> &nums2, int k) {
        vector<int> res;
        int max_num = 0;
        int cnt1 = nums1.size(), cnt2 = nums2.size();

        return res;
    }
    vector<int> maxNumber(vector<int> &nums1, vector<int> &nums2, int k) {
        return dp(nums1, nums2, k);
    }
};
// @lc code=end

/*
// @lcpr case=start
// [3,4,6,5]\n[9,1,2,5,8,3]\n5\n
// @lcpr case=end

// @lcpr case=start
// [6,7]\n[6,0,4]\n5\n
// @lcpr case=end

// @lcpr case=start
// [3,9]\n[8,9]\n3\n
// @lcpr case=end

 */
