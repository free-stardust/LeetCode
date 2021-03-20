/*
 * @lc app=leetcode.cn id=41 lang=c
 *
 * [41] 缺失的第一个正数
 *
 * https://leetcode-cn.com/problems/first-missing-positive/description/
 *
 * algorithms
 * Hard (40.69%)
 * Likes:    1011
 * Dislikes: 0
 * Total Accepted:    117.7K
 * Total Submissions: 289.1K
 * Testcase Example:  '[1,2,0]'
 *
 * 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
 * 
 * 
 * 
 * 进阶：你可以实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案吗？
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：nums = [1,2,0]
 * 输出：3
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：nums = [3,4,-1,1]
 * 输出：2
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：nums = [7,8,9,11,12]
 * 输出：1
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 0 
 * -2^31 
 * 
 * 
 */

// @lc code=start

int randomRange(int a, int b)
{
    if (a <= b)
        return rand() % (b - a) + a;
    else
        return rand() % (a - b) + b;
}

int partition(int *nums, int start, int end)
{
    if (nums == NULL || start >= end)
        return -1;

    int low = start, high = end, pivot;
    int randomIndex = randomRange(low, high);
    pivot = nums[randomIndex];
    nums[randomIndex] = nums[low];
    nums[low] = pivot;
    while (low < high)
    {
        while (low < high && nums[high] >= pivot)
            high--;
        if (low < high)
            nums[low] = nums[high];
        while (low < high && nums[low] <= pivot)
            low++;
        if (low < high)
            nums[high] = nums[low];
    }
    nums[low] = pivot;
    return low;
}

void quickSort(int *nums, int start, int end)
{
    if (nums == NULL || start >= end)
        return;

    int pos = partition(nums, start, end);
    quickSort(nums, start, pos - 1);
    quickSort(nums, pos + 1, end);
}

int firstMissingPositiveMine(int *nums, int numsSize)
{
    if (nums == NULL || numsSize <= 0)
        return 1;

    quickSort(nums, 0, numsSize - 1);

    int num = 1;
    for (int i = 0; i < numsSize; i++)
        if (nums[i] <= 0)
            continue;
        else if (nums[i] == num)
            num++;
        else if (nums[i] > num)
            return num;

    return num;
}

int firstMissingPositive(int *nums, int numsSize)
{
    if (nums == NULL || numsSize <= 0)
        return 1;

    // 自己的解法，不符合题意
    // firstMissingPositiveMine;

    // 官方的解法
    for (int i = 0; i < numsSize; i++)
        if (nums[i] <= 0)
            nums[i] = numsSize + 1;
    
    for (int i = 0; i < numsSize; i++)
    {
        int num = abs(nums[i]);
        if (num <= numsSize)
            nums[num - 1] = -abs(nums[num - 1]);
    }

    for (int i = 0; i < numsSize; i++)
        if (nums[i] > 0)
            return i + 1;
    
    return numsSize + 1;
}
// @lc code=end
