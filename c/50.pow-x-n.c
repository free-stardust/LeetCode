/*
 * @lc app=leetcode.cn id=50 lang=c
 *
 * [50] Pow(x, n)
 *
 * https://leetcode-cn.com/problems/powx-n/description/
 *
 * algorithms
 * Medium (37.35%)
 * Likes:    625
 * Dislikes: 0
 * Total Accepted:    172.3K
 * Total Submissions: 460.5K
 * Testcase Example:  '2.00000\n10'
 *
 * 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，x^n）。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：x = 2.00000, n = 10
 * 输出：1024.00000
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：x = 2.10000, n = 3
 * 输出：9.26100
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：x = 2.00000, n = -2
 * 输出：0.25000
 * 解释：2^-2 = 1/2^2 = 1/4 = 0.25
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * -100.0 
 * -2^31 
 * -10^4 
 * 
 * 
 */

// @lc code=start

double qiuckMul1(double x, long long N)
{
    if (N == 0)
        return 1.0;
    double y = qiuckMul1(x, N / 2);
    return N % 2 == 0 ? y * y : y * y * x;
}

double myPow1(double x, int n)
{
    long long N = n;
    return N >= 0 ? qiuckMul1(x, N) : 1.0 / qiuckMul1(x, -N);
}

double quickMul2(double x, long long N)
{
    double ans = 1.0;

    // 贡献的初始值为x
    double x_contribute = x;

    // 对N进行二进制拆分的同时计算答案
    while (N > 0)
    {
        if (N % 2 == 1)
        {
            // 如果N二进制表示的最低位位1，那么需要计入贡献
            ans *= x_contribute;
        }
            
        // 将贡献不断地平方
        x_contribute *= x_contribute;

        // 舍弃 N 二进制表示的最低为，这样我们每次只要判断最低为即可
        N /= 2;
    }
    return ans;
}

double myPow2(double x, int n)
{
    long long N = n;
    return N >= 0 ? quickMul2(x, N) : 1.0 / quickMul2(x, -N);
}

double myPow(double x, int n)
{
    // return myPow1(x, n);
    return myPow2(x, n);
}
// @lc code=end
