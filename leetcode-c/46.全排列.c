/*
 * @lc app=leetcode.cn id=46 lang=c
 *
 * [46] 全排列
 *
 * https://leetcode-cn.com/problems/permutations/description/
 *
 * algorithms
 * Medium (77.71%)
 * Likes:    1261
 * Dislikes: 0
 * Total Accepted:    291K
 * Total Submissions: 373.9K
 * Testcase Example:  '[1,2,3]'
 *
 * 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
 * 
 * 示例:
 * 
 * 输入: [1,2,3]
 * 输出:
 * [
 * ⁠ [1,2,3],
 * ⁠ [1,3,2],
 * ⁠ [2,1,3],
 * ⁠ [2,3,1],
 * ⁠ [3,1,2],
 * ⁠ [3,2,1]
 * ]
 * 
 */

// @lc code=start
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
// 明明没问题，不知道为啥leetcode跑不通，以后在研究
int count;

void dfs(int *nums, int numsSize, int depth, int *path, bool *used, int **res)
{
    if (depth == numsSize)
    {
        res[count] == (int *)malloc(sizeof(int) * numsSize);
        memcpy(res[count++], path, sizeof(int) * numsSize);
        return;
    }

    for (int i = 0; i < numsSize; i++)
    {
        if (used[i] == true)
            continue;
        path[depth] = nums[i];
        used[i] = true;
        dfs(nums, numsSize, depth + 1, path, used, res);
        used[i] = false;
    }
}

int **permute(int *nums, int numsSize, int *returnSize, int **returnColumnSizes)
{
    (*returnSize) = 1;
    for (int i = 1; i <= numsSize; i++)
        (*returnSize) *= i;

    returnColumnSizes = (int **)malloc(sizeof(int *) * (*returnSize));
    for (int i = 0; i < (*returnSize); i++)
    {
        returnColumnSizes[i] = (int *)malloc(sizeof(int));
        *(returnColumnSizes[i]) = numsSize;
    }

    int **res = (int **)malloc(sizeof(int *) * (*returnSize));
    int *path = (int *)malloc(sizeof(int) * numsSize);
    bool *used = (bool *)calloc(numsSize, sizeof(bool));

    count = 0;
    dfs(nums, numsSize, 0, path, used, res);
    return res;
}
// @lc code=end
