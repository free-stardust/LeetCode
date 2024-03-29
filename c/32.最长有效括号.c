/*
 * @lc app=leetcode.cn id=32 lang=c
 *
 * [32] 最长有效括号
 *
 * https://leetcode-cn.com/problems/longest-valid-parentheses/description/
 *
 * algorithms
 * Hard (34.56%)
 * Likes:    1208
 * Dislikes: 0
 * Total Accepted:    131.4K
 * Total Submissions: 379.2K
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
 * 
 * 输入：s = "(()"
 * 输出：2
 * 解释：最长有效括号子串是 "()"
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：s = ")()())"
 * 输出：4
 * 解释：最长有效括号子串是 "()()"
 * 
 * 
 * 示例 3：
 * 
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
 * 0 
 * s[i] 为 '(' 或 ')'
 * 
 * 
 * 
 * 
 */

// @lc code=start

int max(int a, int b)
{
    if (a >= b)
        return a;
    else
        return b;
}

int longestValidParentheses(char *s)
{
    if (s == NULL)
        return 0;
    else
    {
        int left = 0, right = 0, maxLength = 0;
        int strLength = strlen(s);
        for (int i = 0; i < strLength; i++)
        {
            if (*(s + i) == '(')
                left++;
            else
                right++;
            if (left == right)
            {
                maxLength = max(maxLength, 2 * left);
            }
            else if (left < right)
            {
                left = 0;
                right = 0;
            }
        }
        left = right = 0;
        for (int i = strLength - 1; i >= 0; i--) 
        {
            if (*(s + i) == '(')
                left++;
            else
                right++;
            if (left == right)
            {
                maxLength = max(maxLength, 2 * left);
            }
            else if (left > right)
            {
                left = 0;
                right = 0;
            }
        }
        return maxLength;
    }
}
// @lc code=end
