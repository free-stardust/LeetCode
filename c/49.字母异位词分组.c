/*
 * @lc app=leetcode.cn id=49 lang=c
 *
 * [49] 字母异位词分组
 *
 * https://leetcode-cn.com/problems/group-anagrams/description/
 *
 * algorithms
 * Medium (65.55%)
 * Likes:    707
 * Dislikes: 0
 * Total Accepted:    178.8K
 * Total Submissions: 272.2K
 * Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
 *
 * 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
 * 
 * 示例:
 * 
 * 输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
 * 输出:
 * [
 * ⁠ ["ate","eat","tea"],
 * ⁠ ["nat","tan"],
 * ⁠ ["bat"]
 * ]
 * 
 * 说明：
 * 
 * 
 * 所有输入均为小写字母。
 * 不考虑答案输出的顺序。
 * 
 * 
 */

// @lc code=start

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

// 日常抄答案，看一下大佬是如何C语言实现的，但是leetcode在内存分配那里还是出错，以后再说

#define STR_SIZE 100

typedef struct Node
{
    char str[STR_SIZE];
    int row;
    struct Node *next;
} HashNode;

int hash(char *str, int size)
{
    long h = 0;
    for (int i = 0; i < strlen(str); i++)
    {
        // 字符串的hashcode，权为26是英文小写字母，不限制时为128，这样能够让结点尽可能分布
        // 均匀，减少地址冲突；
        // 取模是为了防止int型溢出；
        h = (h * 26 % size + str[i] - 'a') % size;
    }
    return h % size;
}

bool contain(HashNode *hashtable, char *str, int size)
{
    HashNode *head = &hashtable[hash(str, size)];
    HashNode *tail = head->next;
    while (tail)
    {
        if (strcmp(tail->str, str) == 0)
            return true;
        tail = tail->next;
    }
    return false;
}

void add(HashNode *hashtable, char *str, int size, int row)
{
    if (contain(hashtable, str, size))
        return;
    HashNode *head = &hashtable[hash(str, size)];
    // 头插建表
    HashNode *q = (HashNode *)malloc(sizeof(HashNode));
    strcpy(q->str, str);
    q->row = row;
    q->next = head->next;
    head->next = q;
}

int getRows(HashNode *hashtable, char *str, int size)
{
    HashNode *head = &hashtable[hash(str, size)];
    HashNode *tail = head->next;
    while (tail)
    {
        if (strcmp(tail->str, str) == 0)
            return tail->row;
        tail = tail->next;
    }
    return -1;
}

int cmp(const void *a, const void *b)
{
    return *(char *)a - *(char *)b;
}

char ***groupAnagrams(char **strs, int strsSize, int *returnSize, int **returnColumnSizes)
{
    if (strsSize == 0 || strs == NULL)
    {
        *returnSize = 0;
        return NULL;
    }
    HashNode *hashtable = malloc(sizeof(HashNode) * strsSize);
    memset(hashtable, 0, sizeof(HashNode) * strsSize);
    char **ans = malloc(sizeof(char **) * strsSize);

    *returnSize = 0;
    *returnColumnSizes = malloc(sizeof(int) * strsSize);

    for (int i = 0; i < strsSize; i++)
    {
        char curStr[STR_SIZE] = "";
        strcpy(curStr, strs[i]);
        int lenStr = strlen(curStr);
        qsort(curStr, lenStr, sizeof(char), cmp);

        if (contain(hashtable, curStr, strsSize))
        {
            int row = getRows(hashtable, curStr, strsSize);
            int col = (*returnColumnSizes)[row];
            ans[row][col] = malloc(sizeof(char) * (lenStr + 1));
            strcpy(ans[row][col], strs[i]);
            (*returnColumnSizes)[row]++;
        }
        else
        {
            add(hashtable, curStr, strsSize, *returnSize);
            ans[*returnSize] = malloc(sizeof(char *) * strsSize);
            ans[*returnSize][0] = malloc(sizeof(char) * (lenStr + 1));
            strcpy(ans[*returnSize][0], strs[i]);
            (*returnColumnSizes)[*returnSize] = 1;
            (*returnSize)++;
        }
    }
    return ans;
}
// @lc code=end
