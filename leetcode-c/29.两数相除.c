/*
 * @lc app=leetcode.cn id=29 lang=c
 *
 * [29] 两数相除
 *
 * https://leetcode-cn.com/problems/divide-two-integers/description/
 *
 * algorithms
 * Medium (20.42%)
 * Likes:    517
 * Dislikes: 0
 * Total Accepted:    80.2K
 * Total Submissions: 392.7K
 * Testcase Example:  '10\n3'
 *
 * 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
 * 
 * 返回被除数 dividend 除以除数 divisor 得到的商。
 * 
 * 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) =
 * -2
 * 
 * 
 * 
 * 示例 1:
 * 
 * 输入: dividend = 10, divisor = 3
 * 输出: 3
 * 解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
 * 
 * 示例 2:
 * 
 * 输入: dividend = 7, divisor = -3
 * 输出: -2
 * 解释: 7/-3 = truncate(-2.33333..) = -2
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 被除数和除数均为 32 位有符号整数。
 * 除数不为 0。
 * 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 2^31 − 1。
 * 
 * 
 */

// @lc code=start

int divideCore(long dividend, long divisor) {
    if (dividend < divisor) {
        return 0;
    } else {
        long result = 1;
        long divisorTmp = divisor;  // 记录除数，后面还要用
        while (dividend >= (divisorTmp << 1)){
            result = result << 1;
            divisorTmp = divisorTmp << 1;
        }
        return result + divideCore(dividend - divisorTmp, divisor);
    }
}

int divide(int dividend, int divisor){
    if (dividend == 0)  // 被除数为0直接返回0
        return 0;   
    else if (divisor == 1)  // 除数为1直接返回被除数
        return dividend;    
    else if (divisor == -1) // 除数为-1需要做溢出处理
        return (dividend == INT_MIN) ? INT_MAX : (-dividend);
    else {
        int resultSign = -1;
        if ((dividend > 0 ? 1 : -1) == (divisor > 0 ? 1 : -1))
            resultSign = 1;

        long dividendL = dividend;  // 用long存储，以防绝对值溢出
        long divisorL = divisor;    // 用long存储，以防绝对值溢出

        dividendL = dividendL > 0 ? dividendL : (-dividendL);
        divisorL = divisorL > 0 ? divisorL : (-divisorL);

        int result = divideCore(dividendL, divisorL);
        result = resultSign > 0 ? result : (-result);
        
        return result;
    }
}
// @lc code=end

