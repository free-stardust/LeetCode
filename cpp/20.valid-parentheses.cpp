/*
 * @lc app=leetcode.cn id=20 lang=cpp
 * @lcpr version=30204
 *
 * [20] 有效的括号
 *
 * https://leetcode.cn/problems/valid-parentheses/description/
 *
 * algorithms
 * Easy (44.08%)
 * Likes:    4509
 * Dislikes: 0
 * Total Accepted:    1.9M
 * Total Submissions: 4.3M
 * Testcase Example:  '"()"'
 *
 * 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
 *
 * 有效字符串需满足：
 *
 *
 * 左括号必须用相同类型的右括号闭合。
 * 左括号必须以正确的顺序闭合。
 * 每个右括号都有一个对应的相同类型的左括号。
 *
 *
 *
 *
 * 示例 1：
 *
 * 输入：s = "()"
 * 输出：true
 *
 *
 * 示例 2：
 *
 * 输入：s = "()[]{}"
 * 输出：true
 *
 *
 * 示例 3：
 *
 * 输入：s = "(]"
 * 输出：false
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 10^4
 * s 仅由括号 '()[]{}' 组成
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
    bool isValid(string s) {
        if (s.size() % 2 != 0)
            return false;

        stack<char> st;
        unordered_map<char, char> mp = {
            {')', '('},
            {']', '['},
            {'}', '{'},
        };

        for (char c : s) {
            if (!mp.contains(c))
                st.push(c);
            else {
                if (st.empty() || st.top() != mp[c])
                    return false;
                st.pop();
            }
        }

        return st.empty();
    }
};
// @lc code=end

int main() {
    string s = "()";
    Solution *so = new Solution();
    bool res = so->isValid(s);
    cout << res << endl;
    return 0;
}

/*
// @lcpr case=start
// "()"\n
// @lcpr case=end

// @lcpr case=start
// "()[]{}"\n
// @lcpr case=end

// @lcpr case=start
// "(]"\n
// @lcpr case=end

// @lcpr case=start
// "]"\n
// @lcpr case=end

 */
