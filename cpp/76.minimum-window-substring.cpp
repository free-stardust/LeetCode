/*
 * @lc app=leetcode.cn id=76 lang=cpp
 * @lcpr version=30204
 *
 * [76] 最小覆盖子串
 *
 * https://leetcode.cn/problems/minimum-window-substring/description/
 *
 * algorithms
 * Hard (46.02%)
 * Likes:    2965
 * Dislikes: 0
 * Total Accepted:    617.6K
 * Total Submissions: 1.3M
 * Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
 *
 * 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 ""
 * 。
 *
 *
 *
 * 注意：
 *
 *
 * 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
 * 如果 s 中存在这样的子串，我们保证它是唯一的答案。
 *
 *
 *
 *
 * 示例 1：
 *
 * 输入：s = "ADOBECODEBANC", t = "ABC"
 * 输出："BANC"
 * 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
 *
 *
 * 示例 2：
 *
 * 输入：s = "a", t = "a"
 * 输出："a"
 * 解释：整个字符串 s 是最小覆盖子串。
 *
 *
 * 示例 3:
 *
 * 输入: s = "a", t = "aa"
 * 输出: ""
 * 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
 * 因此没有符合条件的子字符串，返回空字符串。
 *
 *
 *
 * 提示：
 *
 *
 * ^m == s.length
 * ^n == t.length
 * 1 <= m, n <= 10^5
 * s 和 t 由英文字母组成
 *
 *
 *
 * 进阶：你能设计一个在 o(m+n) 时间内解决此问题的算法吗？
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
    bool isCovered(int cnt_s[], int cnt_t[]) {
        for (int i = 'A'; i <= 'Z'; i++) {
            if (cnt_s[i] < cnt_t[i])
                return false;
        }

        for (int i = 'a'; i <= 'z'; i++) {
            if (cnt_s[i] < cnt_t[i])
                return false;
        }

        return true;
    }

    string zerox3f1(string s, string t) {
        int s_len = s.length();
        int res_left = -1, res_right = s_len;
        int cnt_s[128]{}, cnt_t[128]{};

        for (auto c : t)
            cnt_t[c]++;

        int left = 0;
        for (int right = 0; right < s_len; right++) {
            cnt_s[s[right]]++;
            while (isCovered(cnt_s, cnt_t)) {
                if (right - left < res_right - res_left) {
                    res_left = left;
                    res_right = right;
                }
                cnt_s[s[left]]--;
                left++;
            }
        }

        return res_left < 0 ? "" : s.substr(res_left, res_right - res_left + 1);
    }

    string zerox3f2(string s, string t) {
        int s_len = s.length(), less = 0;
        int res_left = -1, res_right = s_len;
        int cnt[128]{};

        for (auto c : t) {
            if (cnt[c] == 0) {
                less++;
            }
            cnt[c]++;
        }

        int left = 0;
        for (int right = 0; right < s_len; right++) {
            char c = s[right];
            cnt[c]--;

            if (cnt[c] == 0) less--;

            while (less == 0) {
                if (right - left < res_right - res_left) {
                    res_left = left;
                    res_right = right;
                }

                char x = s[left];
                if (cnt[x] == 0) less++;
                cnt[x]++;
                left++;
            }
        }

        return res_left < 0 ? "" : s.substr(res_left, res_right - res_left + 1);
    }

    string minWindow(string s, string t) {
        // return zerox3f1(s, t);
        return zerox3f2(s, t);
    }
};
// @lc code=end

int main() {
    cout << int('a') << ", " << int('A') << endl;
    return 0;
}

/*
// @lcpr case=start
// "ADOBECODEBANC"\n"ABC"\n
// @lcpr case=end

// @lcpr case=start
// "a"\n"a"\n
// @lcpr case=end

// @lcpr case=start
// "a"\n"aa"\n
// @lcpr case=end

 */
