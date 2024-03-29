/*
 * @lc app=leetcode.cn id=37 lang=c
 *
 * [37] 解数独
 *
 * https://leetcode-cn.com/problems/sudoku-solver/description/
 *
 * algorithms
 * Hard (67.06%)
 * Likes:    786
 * Dislikes: 0
 * Total Accepted:    73.5K
 * Total Submissions: 109.6K
 * Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
 *
 * 编写一个程序，通过填充空格来解决数独问题。
 * 
 * 一个数独的解法需遵循如下规则：
 * 
 * 
 * 数字 1-9 在每一行只能出现一次。
 * 数字 1-9 在每一列只能出现一次。
 * 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
 * 
 * 
 * 空白格用 '.' 表示。
 * 
 * 
 * 
 * 一个数独。
 * 
 * 
 * 
 * 答案被标成红色。
 * 
 * 提示：
 * 
 * 
 * 给定的数独序列只包含数字 1-9 和字符 '.' 。
 * 你可以假设给定的数独只有唯一解。
 * 给定数独永远是 9x9 形式的。
 * 
 * 
 */

// @lc code=start

bool line[9][9];    // 行数组
bool column[9][9];  // 列数组
bool block[3][3][9];    // 区块数组
bool valid; // 确定是否找到解
int *spaces[81];    // 空格数组
int spacesSize; // 空格数目

void dfs(char **board, int pos)
{
    if (pos == spacesSize)
    {
        valid = true;
        return;
    }

    int i = spaces[pos][0], j = spaces[pos][1];
    for (int digit = 0; digit < 9 && !valid; digit++)   // 对当前空格进行1-9回溯遍历
    {
        // 如果当前数字不未填入，进行迭代
        if (!line[i][digit] && !column[j][digit] && !block[i / 3][j / 3][digit])
        {
            line[i][digit] = column[j][digit] = block[ i / 3][j / 3][digit] = true;
            board[i][j] = digit + '0' + 1;
            dfs(board, pos + 1);

            // 迭代过后重置数字标记
            line[i][digit] = column[j][digit] = block[ i / 3][j / 3][digit] = false;
        }
    }
}

void solveSudoku(char **board, int boardSize, int *boardColSize)
{
    memset(line, false, sizeof(line));
    memset(column, false, sizeof(column));
    memset(block, false, sizeof(block));
    valid = false;
    spacesSize = 0;

    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            if (board[i][j] == '.')
            {
                spaces[spacesSize] = malloc(sizeof(int) * 2);
                spaces[spacesSize][0] = i;  // 记录空格的行号
                spaces[spacesSize++][1] = j;    // 记录空格的列号
            }
            else
            {
                int digit = board[i][j] - '0' - 1;
                // 标记已填入的数字
                line[i][digit] = column[j][digit] = block[i / 3][j / 3][digit] = true;
            }
        }
    }

    dfs(board, 0);  // 迭代求解
}
// @lc code=end
