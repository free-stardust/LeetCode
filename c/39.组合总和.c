/*
 * @lc app=leetcode.cn id=39 lang=c
 *
 * [39] 组合总和
 *
 * https://leetcode-cn.com/problems/combination-sum/description/
 *
 * algorithms
 * Medium (72.13%)
 * Likes:    1224
 * Dislikes: 0
 * Total Accepted:    223.1K
 * Total Submissions: 309.2K
 * Testcase Example:  '[2,3,6,7]\n7'
 *
 * 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
 * 
 * candidates 中的数字可以无限制重复被选取。
 * 
 * 说明：
 * 
 * 
 * 所有数字（包括 target）都是正整数。
 * 解集不能包含重复的组合。 
 * 
 * 
 * 示例 1：
 * 
 * 输入：candidates = [2,3,6,7], target = 7,
 * 所求解集为：
 * [
 * ⁠ [7],
 * ⁠ [2,2,3]
 * ]
 * 
 * 
 * 示例 2：
 * 
 * 输入：candidates = [2,3,5], target = 8,
 * 所求解集为：
 * [
 * [2,2,2,2],
 * [2,3,3],
 * [3,5]
 * ]
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 <= candidates.length <= 30
 * 1 <= candidates[i] <= 200
 * candidate 中的每个元素都是独一无二的。
 * 1 <= target <= 500
 * 
 * 
 */

// @lc code=start

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

// 官方解法先抄为敬

int candidatesSize_tmp;
int ansSize;
int combineSize;
int *ansColumnSize;

void dfs(int *candidates, int target, int **ans, int *combine, int idx)
{
    if (idx == candidatesSize_tmp)
    {
        return;
    }
    if (target == 0)
    {
        int *tmp = (int *)malloc(sizeof(int) * combineSize);
        for (int i = 0; i < combineSize; i++)
        {
            tmp[i] = combine[i];
        }
        ans[ansSize] = tmp;
        ansColumnSize[ansSize++] = combineSize;
        return;
    }

    // 直接跳过
    dfs(candidates, target, ans, combine, idx + 1);

    // 选择当前数
    if (target - candidates[idx] >= 0)
    {
        combine[combineSize++] = candidates[idx];
        dfs(candidates, target - candidates[idx], ans, combine, idx);
        combineSize--;
    }
}

int **combinationSum(int *candidates, int candidatesSize, int target, int *returnSize, int **returnColumnSizes)
{
    candidatesSize_tmp = candidatesSize;
    ansSize = combineSize = 0;
    int **ans = malloc(sizeof(int *) * 1001);
    ansColumnSize = malloc(sizeof(int) * 1001);
    int combine[2001];
    dfs(candidates, target, ans, combine, 0);
    *returnSize = ansSize;
    *returnColumnSizes = ansColumnSize;
    return ans;
}
// @lc code=end
