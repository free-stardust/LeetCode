/*
 * @lc app=leetcode.cn id=43 lang=c
 *
 * [43] 字符串相乘
 *
 * https://leetcode-cn.com/problems/multiply-strings/description/
 *
 * algorithms
 * Medium (44.75%)
 * Likes:    586
 * Dislikes: 0
 * Total Accepted:    130.4K
 * Total Submissions: 291.6K
 * Testcase Example:  '"2"\n"3"'
 *
 * 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
 * 
 * 示例 1:
 * 
 * 输入: num1 = "2", num2 = "3"
 * 输出: "6"
 * 
 * 示例 2:
 * 
 * 输入: num1 = "123", num2 = "456"
 * 输出: "56088"
 * 
 * 说明：
 * 
 * 
 * num1 和 num2 的长度小于110。
 * num1 和 num2 只包含数字 0-9。
 * num1 和 num2 均不以零开头，除非是数字 0 本身。
 * 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
 * 
 * 
 */

// @lc code=start

// 日常抄答案之解法二
// 暂时消化不了，后面再看看

char *multiply(char *num1, char *num2)
{
    char *ans;
    if (num1 == NULL || num2 == NULL)
    {
        ans = (char *)malloc(sizeof(char) * 2);
        ans[0] = '0';
        ans[1] = '\0';
        return ans;
    }
    else
    {
        int m = strlen(num1), n = strlen(num2);
        ans = (char *)malloc(sizeof(char) * (m + n + 3));
        memset(ans, 0, sizeof(char) * (m + n + 3));
        if ((m == 1 && num1[0] == '0') || (n == 1 && num2[0] == '0'))
        {
            ans[0] = '0', ans[1] = 0;
            return ans;
        }
        int *ansArr = (int *)malloc(sizeof(int) * (m + n + 3));
        memset(ansArr, 0, sizeof(int) * (m + n + 3));
        for (int i = m - 1; i >= 0; i--)
        {
            int x = num1[i] - '0';
            for (int j = n - 1; j >= 0; j--)
            {
                int y = num2[j] - '0';
                ansArr[i + j + 1] += x * y;
            }
        }
        for (int i = m + n - 1; i > 0; i--)
        {
            ansArr[i - 1] += ansArr[i] / 10;
            ansArr[i] %= 10;
        }
        int index = ansArr[0] == 0 ? 1 : 0;
        int ansLen = 0;
        while (index < m + n)
        {
            ans[ansLen++] = ansArr[index];
            index++;
        }
        for (int i = 0; i < ansLen; i++)
            ans[i] += '0';
        return ans;
    }
}
// @lc code=end
