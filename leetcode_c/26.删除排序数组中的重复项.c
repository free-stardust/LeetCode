/*
 * @lc app=leetcode.cn id=26 lang=c
 *
 * [26] 删除排序数组中的重复项
 */

// @lc code=start


int removeDuplicates(int* nums, int numsSize){
    if (numsSize < 2) {
        return numsSize;
    } else {
        int index = 0;
            for (int i = 1; i < numsSize; i++) {
                if(nums[index] != nums[i]) {
                    nums[++index] = nums[i];
                }
        }
        return index + 1;
    }
}
// @lc code=end

