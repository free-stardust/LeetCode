/*
 * @lc app=leetcode.cn id=34 lang=c
 *
 * [34] 在排序数组中查找元素的第一个和最后一个位置
 *
 * https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
 *
 * algorithms
 * Medium (42.30%)
 * Likes:    892
 * Dislikes: 0
 * Total Accepted:    219.6K
 * Total Submissions: 519.2K
 * Testcase Example:  '[5,7,7,8,8,10]\n8'
 *
 * 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
 * 
 * 如果数组中不存在目标值 target，返回 [-1, -1]。
 * 
 * 进阶：
 * 
 * 
 * 你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
 * 
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：nums = [5,7,7,8,8,10], target = 8
 * 输出：[3,4]
 * 
 * 示例 2：
 * 
 * 
 * 输入：nums = [5,7,7,8,8,10], target = 6
 * 输出：[-1,-1]
 * 
 * 示例 3：
 * 
 * 
 * 输入：nums = [], target = 0
 * 输出：[-1,-1]
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 0 
 * -10^9 
 * nums 是一个非递减数组
 * -10^9 
 * 
 * 
 */

// @lc code=start

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

/*
 * 算法说明：该算法是通过二分法分别查找左边第一个符合要求的索引以及第一个大于目标值的索引，
 *  进而确定目标值所在的范围。
 */

int binarySearch(int *nums, int numsSize, int target, bool lower)
{
    // 如果lower为true，则为寻找数组中第一个等于target的索引；
    // 如果lower为false，则为寻找数组中第一个大于target的索引；
    if (nums == NULL || numsSize <= 0)
        return numsSize;
    else
    {
        int left = 0, right = numsSize - 1, index = numsSize;
        while (left <= right)
        {
            int mid = (left + right) / 2;
            if (nums[mid] > target || (lower && nums[mid] >= target))
            {
                right = mid - 1;
                index = mid;
            }
            else
            {
                left = mid + 1;
            }
        }
        return index;
    }
}

int *searchRange(int *nums, int numsSize, int target, int *returnSize)
{
    int *result = (int *)malloc(sizeof(int) * 2);
    result[0] = result[1] = -1;
    *returnSize = 2;
    if (nums == NULL || numsSize <= 0)
        return result;
    else
    {
        // 数组中第一个等于target值得索引
        int left = binarySearch(nums, numsSize, target, true);
        // 数组中第二个等于target值得索引，由于binarySearch返回的是第一个大于target值
        // 的索引，所以要减一
        int right = binarySearch(nums, numsSize, target, false) - 1;
        if (left <= right && nums[left] == target && nums[right] == target)
        {
            result[0] = left;
            result[1] = right;
        }
        return result;
    }
}
// @lc code=end
