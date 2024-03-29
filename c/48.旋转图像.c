/*
 * @lc app=leetcode.cn id=48 lang=c
 *
 * [48] 旋转图像
 *
 * https://leetcode-cn.com/problems/rotate-image/description/
 *
 * algorithms
 * Medium (72.45%)
 * Likes:    848
 * Dislikes: 0
 * Total Accepted:    159.2K
 * Total Submissions: 219.4K
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
 *
 * 给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
 * 
 * 你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
 * 输出：[[7,4,1],[8,5,2],[9,6,3]]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
 * 输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 * 
 * 
 * 示例 3：
 * 
 * 
 * 输入：matrix = [[1]]
 * 输出：[[1]]
 * 
 * 
 * 示例 4：
 * 
 * 
 * 输入：matrix = [[1,2],[3,4]]
 * 输出：[[3,1],[4,2]]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * matrix.length == n
 * matrix[i].length == n
 * 1 
 * -1000 
 * 
 * 
 */

// @lc code=start
void swap(int *a, int *b)
{
    int t = *a;
    *a = *b, *b = t;
}

void rotate(int **matrix, int matrixSize, int *matrixColSize)
{
    // 水平翻转
    for (int i = 0; i < matrixSize / 2; i++)
    {
        for (int j = 0; j < matrixSize; j++)
        {
            swap(&matrix[i][j], &matrix[matrixSize - i - 1][j]);
        }
    }

    // 主对角线翻转
    for (int i = 0; i < matrixSize; i++)
    {
        for (int j = 0; j < i; j++)
        {
            swap(&matrix[i][j], &matrix[j][i]);
        }
    }

    *matrixColSize = matrixSize;
}
// @lc code=end
