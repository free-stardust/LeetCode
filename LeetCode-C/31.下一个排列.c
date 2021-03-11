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

int partition(int *nums, int start, int end)
{
    if (start == end)
        return start;
    else
    {
        int index = (rand() % (end + 1 - start)) + start;
        int low = start, high = end, num = nums[index];
        int temp = nums[start];
        nums[start] = nums[index];
        nums[index] = temp;
        while (low < high)
        {
            while (high > low && nums[high] >= num)
                high--;
            if (low < high)
                nums[low] = nums[high];
            while (low < high && nums[low] <= num)
                low++;
            if (low < high)
                nums[high] = nums[low];
        }
        nums[low] = num;
        return low;
    }
}

void quickSort(int *nums, int start, int end)
{
    if (nums == NULL || start >= end || start < 0 || end < 0)
        return;
    else
    {
        int position = partition(nums, start, end);
        quickSort(nums, start, position);
        quickSort(nums, position + 1, end);
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
                    quickSort(nums, nonDcendingIndex + 1, numsSize - 1);
                    return;
                }
            }
        }
        else
        {
            for (int i = 0; i < numsSize / 2; i++)
            {
                int temp = nums[i];
                nums[i] = nums[numsSize - i - 1];
                nums[numsSize - i - 1] = temp;
            }
            return;
        }
    }
}
// @lc code=end
