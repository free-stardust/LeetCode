/*
 * @lc app=leetcode.cn id=31 lang=c
 *
 * [31] 下一个排列
 *
 * https://leetcode-cn.com/problems/next-permutation/description/
 *
 * algorithms
 * Medium (36.47%)
 * Likes:    990
 * Dislikes: 0
 * Total Accepted:    141.6K
 * Total Submissions: 387.7K
 * Testcase Example:  '[1,2,3]'
 *
 * 实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
 * 
 * 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
 * 
 * 必须 原地 修改，只允许使用额外常数空间。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：nums = [1,2,3]
 * 输出：[1,3,2]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：nums = [3,2,1]
 * 输出：[1,2,3]
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：nums = [1,1,5]
 * 输出：[1,5,1]
 * 
 * 
 * 示例 4：
 * 
 * 
 * 输入：nums = [1]
 * 输出：[1]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 
 * 0 
 * 
 * 
 */

// @lc code=start

void reverse(int* nums, int start, int end) {
    if (nums == NULL || start >= end || start < 0 || end < 0)
        return;
    else
    {
        int length = end - start + 1;
        for (int i = start; i < start + length / 2; i++) 
        {
            int temp = nums[i];
            nums[i] = nums[end - i + start];
            nums[end - i + start] = temp;
        }
    }
}

void nextPermutation(int *nums, int numsSize)
{
    if (nums == NULL || numsSize <= 1)
        return;
    else
    {
        int nonDcendingIndex = -1;
        for (int i = numsSize - 2; i >= 0; i--)
        {
            if (nums[i] < nums[i + 1])
            {
                nonDcendingIndex = i;
                break;
            }
        }
        if (nonDcendingIndex >= 0)
        {
            for (int i = numsSize - 1; i >= 0; i--)
            {
                if (nums[i] > nums[nonDcendingIndex])
                {
                    int temp = nums[nonDcendingIndex];
                    nums[nonDcendingIndex] = nums[i];
                    nums[i] = temp;
                    break;
                }
            }
        }
        reverse(nums, nonDcendingIndex + 1, numsSize - 1);
        return;
    }
}
// @lc code=end
