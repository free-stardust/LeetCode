/*
 * @lc app=leetcode.cn id=4 lang=cpp
 * @lcpr version=30202
 *
 * [4] 寻找两个正序数组的中位数
 *
 * https://leetcode.cn/problems/median-of-two-sorted-arrays/description/
 *
 * algorithms
 * Hard (42.24%)
 * Likes:    7130
 * Dislikes: 0
 * Total Accepted:    1.1M
 * Total Submissions: 2.6M
 * Testcase Example:  '[1,3]\n[2]'
 *
 * 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
 *
 * 算法的时间复杂度应该为 O(log (m+n)) 。
 *
 *
 *
 * 示例 1：
 *
 * 输入：nums1 = [1,3], nums2 = [2]
 * 输出：2.00000
 * 解释：合并数组 = [1,2,3] ，中位数 2
 *
 *
 * 示例 2：
 *
 * 输入：nums1 = [1,2], nums2 = [3,4]
 * 输出：2.50000
 * 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
 *
 *
 *
 *
 *
 *
 * 提示：
 *
 *
 * nums1.length == m
 * nums2.length == n
 * 0 <= m <= 1000
 * 0 <= n <= 1000
 * 1 <= m + n <= 2000
 * -10^6 <= nums1[i], nums2[i] <= 10^6
 *
 *
 */

// @lcpr-template-start
#include <algorithm>
#include <array>
#include <bits/types/FILE.h>
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

    double official_solution1(vector<int> &nums1, vector<int> &nums2) {
        int totalLength = nums1.size() + nums2.size();
        if (totalLength % 2 == 1) {
            return getKthElement(nums1, nums2, (totalLength + 1) / 2);
        } else {
            return (getKthElement(nums1, nums2, totalLength / 2) + getKthElement(nums1, nums2, totalLength / 2 + 1)) / 2.0;
        }
    }

    int getKthElement(vector<int> &nums1, vector<int> &nums2, int k) {
        int m = nums1.size();
        int n = nums2.size();
        int index1 = 0, index2 = 0;

        while (true) {
            if (index1 == m) {
                return nums2[index2 + k - 1];
            }
            if (index2 == n) {
                return nums1[index1 + k - 1];
            }
            if (k == 1) {
                return min(nums1[index1], nums2[index2]);
            }

            int newIndex1 = min(index1 + k / 2 - 1, m - 1);
            int newIndex2 = min(index2 + k / 2 - 1, n - 1);
            int pivot1 = nums1[newIndex1];
            int pivot2 = nums2[newIndex2];
            if (pivot1 <= pivot2) {
                k -= newIndex1 - index1 + 1;
                index1 = newIndex1 + 1;
            } else {
                k -= newIndex2 - index2 + 1;
                index2 = newIndex2 + 1;
            }
        }
    }

    double official_solution2(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) 
            return official_solution2(nums2, nums1);
        
        int m = nums1.size();
        int n = nums2.size();
        int left = 0, right = m;
        int median1 = 0, median2 = 0;

        while (left <= right) {
            int i = (left + right) / 2;
            int j = (m + n + 1) / 2 - i;

            int nums_im1 = i == 0 ? INT_MIN : nums1[i-1];
            int nums_i = i == m ? INT_MAX : nums1[i];
            int nums_jm1 = j == 0 ? INT_MIN : nums2[j-1];
            int nums_j = j == n ? INT_MAX : nums2[j];

            if (nums_im1 <= nums_j) {
                median1 = max(nums_im1, nums_jm1);
                median2 = min(nums_i, nums_j);
                left = i + 1;
            } else {
                right = i - 1;
            }
        }
        return (m + n) % 2 == 0 ? (median1 + median2) / 2.0 : median1;
    }

    double zero_xf3_double_point(vector<int> &nums1, vector<int> &nums2) {
        if (nums1.size() > nums2.size()) swap(nums1, nums2);

        int len1 = nums1.size(), len2 = nums2.size();
        nums1.insert(nums1.begin(), INT_MIN);
        nums2.insert(nums2.begin(), INT_MIN);
        nums1.push_back(INT_MAX);
        nums2.push_back(INT_MAX);

        int i = 0, j = (len1 + len2 + 1) / 2;
        while (true) {
            if (nums1[i] <= nums2[j + 1] && nums1[i + 1] > nums2[j]) {
                int max1 = max(nums1[i], nums2[j]);
                int min2 = min(nums1[i + 1], nums2[j + 1]);
                return (len1 + len2) & 1 ? max1 : (max1 + min2) / 2.0;
            }
            i++;
            j--;
        }
    }

    double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2) {
        // return official_solution2(nums1, nums2);
        return zero_xf3_double_point(nums1, nums2);
    }
};
// @lc code=end

/*
// @lcpr case=start
// [1,3]\n[2]\n
// @lcpr case=end

// @lcpr case=start
// [1,2]\n[3,4]\n
// @lcpr case=end

 */
