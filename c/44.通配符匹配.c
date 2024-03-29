/*
 * @lc app=leetcode.cn id=44 lang=c
 *
 * [44] 通配符匹配
 *
 * https://leetcode-cn.com/problems/wildcard-matching/description/
 *
 * algorithms
 * Hard (32.02%)
 * Likes:    646
 * Dislikes: 0
 * Total Accepted:    66.2K
 * Total Submissions: 206.1K
 * Testcase Example:  '"aa"\n"a"'
 *
 * 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
 * 
 * '?' 可以匹配任何单个字符。
 * '*' 可以匹配任意字符串（包括空字符串）。
 * 
 * 
 * 两个字符串完全匹配才算匹配成功。
 * 
 * 说明:
 * 
 * 
 * s 可能为空，且只包含从 a-z 的小写字母。
 * p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
 * 
 * 
 * 示例 1:
 * 
 * 输入:
 * s = "aa"
 * p = "a"
 * 输出: false
 * 解释: "a" 无法匹配 "aa" 整个字符串。
 * 
 * 示例 2:
 * 
 * 输入:
 * s = "aa"
 * p = "*"
 * 输出: true
 * 解释: '*' 可以匹配任意字符串。
 * 
 * 
 * 示例 3:
 * 
 * 输入:
 * s = "cb"
 * p = "?a"
 * 输出: false
 * 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
 * 
 * 
 * 示例 4:
 * 
 * 输入:
 * s = "adceb"
 * p = "*a*b"
 * 输出: true
 * 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
 * 
 * 
 * 示例 5:
 * 
 * 输入:
 * s = "acdcb"
 * p = "a*c?b"
 * 输出: false
 * 
 */

// @lc code=start

// 这题太难了，得抄答案

bool isMatch1(char *s, char *p)
{
    if (s == NULL || p == NULL)
        return false;

    int m = strlen(s), n = strlen(p);
    int dp[m + 1][n + 1];
    memset(dp, 0, sizeof(dp));
    dp[0][0] = true;

    for (int i = 1; i <= n; i++)
    {
        if (p[i - 1] == '*')
        {
            dp[0][i] = true;
        }
        else
        {
            break;
        }
    }

    for (int i = 1; i <= m; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            if (p[j - 1] == '*')
                dp[i][j] = dp[i][j - 1] | dp[i - 1][j];
            else if (p[j - 1] == '?' || s[i - 1] == p[j - 1])
                dp[i][j] = dp[i - 1][j - 1];
        }
    }

    return dp[m][n];
}

bool allStars(char *str, int left, int right)
{
    for (int i = left; i < right; ++i)
    {
        if (str[i] != '*')
        {
            return false;
        }
    }
    return true;
}
bool charMatch(char u, char v) { return u == v || v == '?'; }

bool isMatch2(char *s, char *p)
{
    int len_s = strlen(s), len_p = strlen(p);
    while (len_s && len_p && p[len_p - 1] != '*')
    {
        if (charMatch(s[len_s - 1], p[len_p - 1]))
        {
            len_s--;
            len_p--;
        }
        else
        {
            return false;
        }
    }
    if (len_p == 0)
    {
        return len_s == 0;
    }

    int sIndex = 0, pIndex = 0;
    int sRecord = -1, pRecord = -1;
    while (sIndex < len_s && pIndex < len_p)
    {
        if (p[pIndex] == '*')
        {
            ++pIndex;
            sRecord = sIndex;
            pRecord = pIndex;
        }
        else if (charMatch(s[sIndex], p[pIndex]))
        {
            ++sIndex;
            ++pIndex;
        }
        else if (sRecord != -1 && sRecord + 1 < len_s)
        {
            ++sRecord;
            sIndex = sRecord;
            pIndex = pRecord;
        }
        else
        {
            return false;
        }
    }
    return allStars(p, pIndex, len_p);
}

bool isMatch(char *s, char *p)
{
    // 动态规划
    // return isMatch1(s, p);

    // 贪心算法
    return isMatch2(s,p);
}
// @lc code=end
