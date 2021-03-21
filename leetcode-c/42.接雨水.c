/*
 * @lc app=leetcode.cn id=42 lang=c
 *
 * [42] 接雨水
 *
 * https://leetcode-cn.com/problems/trapping-rain-water/description/
 *
 * algorithms
 * Hard (54.67%)
 * Likes:    2168
 * Dislikes: 0
 * Total Accepted:    212.3K
 * Total Submissions: 387.5K
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
 * 
 * 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
 * 输出：6
 * 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
 * 
 * 
 * 示例 2：
 * 
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
 * 0 
 * 0 
 * 
 * 
 */

// @lc code=start

int max(int a, int b)
{
    return a >= b ? a : b;
}

int min(int a, int b)
{
    return a <= b ? a : b;
}

int trap1(int *height, int heightSize)
{
    if (height == NULL || height <= 0)
        return 0;
    int ans = 0;
    for (int i = 1; i < heightSize - 1; i++)
    {
        int maxLeft = 0, maxRight = 0;
        for (int j = i; j >= 0; j--)
            maxLeft = max(maxLeft, height[j]);
        for (int j = i; j < heightSize; j++)
            maxRight = max(maxRight, height[j]);
        ans += min(maxLeft, maxRight) - height[i];
    }
    return ans;
}

int trap2(int *height, int heightSzie)
{
    if (height == NULL || heightSzie <= 0)
        return 0;

    int ans = 0;
    int maxLeft[heightSzie], maxRight[heightSzie];
    maxLeft[0] = height[0];
    for (int i = 1; i < heightSzie; i++)
        maxLeft[i] = max(height[i], maxLeft[i - 1]);
    maxRight[heightSzie - 1] = height[heightSzie - 1];
    for (int i = heightSzie - 2; i >= 0; i--)
        maxRight[i] = max(height[i], maxRight[i + 1]);
    for (int i = 1; i < heightSzie - 1; i++)
        ans += min(maxLeft[i], maxRight[i]) - height[i];
    return ans;
}

int trap3(int *height, int heightSize)
{
    if (height == NULL || heightSize <= 0)
        return 0;
    int ans = 0;
    int left = 0, right = heightSize - 1;
    int leftMax = 0, rightMax = 0;
    while (left < right)
    {
        if (height[left] < height[right])
        {
            if (height[left] >= leftMax)
                leftMax = height[left];
            else
                ans += leftMax - height[left];
            left++;
        }
        else
        {
            if (height[right] >= rightMax)
                rightMax = height[right];
            else
                ans += rightMax - height[right];
            right--;
        }
    }
    return ans;
}

int trap(int *height, int heightSize)
{
    if (height == NULL || height <= 0)
        return 0;

    // 方法1：暴力解法
    // return trap1(height, heightSize);

    // 方法2：动态规划
    // return trap2(height, heightSize);

    // 方法3：双指针
    return trap3(height, heightSize);
}
// @lc code=end
