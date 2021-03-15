/*
 * @lc app=leetcode.cn id=28 lang=c
 *
 * [28] 实现 strStr()
 *
 * https://leetcode-cn.com/problems/implement-strstr/description/
 *
 * algorithms
 * Easy (39.73%)
 * Likes:    718
 * Dislikes: 0
 * Total Accepted:    299.3K
 * Total Submissions: 752.9K
 * Testcase Example:  '"hello"\n"ll"'
 *
 * 实现 strStr() 函数。
 * 
 * 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置
 * (从0开始)。如果不存在，则返回  -1。
 * 
 * 示例 1:
 * 
 * 输入: haystack = "hello", needle = "ll"
 * 输出: 2
 * 
 * 
 * 示例 2:
 * 
 * 输入: haystack = "aaaaa", needle = "bba"
 * 输出: -1
 * 
 * 
 * 说明:
 * 
 * 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
 * 
 * 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
 * 
 */

// @lc code=start

// 借此题学习下kmp算法，但是这题其实暴力就可以，而且时间上和kmp差不多，空间消耗还少

int* buildNext(char* needle) {
    int j = 0;
    int patternStrLen = strlen(needle);
    int* next = (int*)malloc(sizeof(int) * patternStrLen);
    int t = next[0] = -1;
    while (j < patternStrLen - 1) {
        if (t < 0 || needle[j] == needle[t]) {
            j++;
            t++;
            next[j] = (needle[j] != needle[t]) ? t : next[t];
        } else {
            t = next[t];
        }
    }
    return next;
}

int strStr(char * haystack, char * needle){
    if (haystack == NULL || needle == NULL) {
        return -1;
    } else if (needle[0] == '\0') {
        return 0;
    } else {
        int* next = buildNext(needle);
        int strlen1 = strlen(haystack);
        int strlen2 = strlen(needle);
        int i = 0, j = 0;
        while (i < strlen1 && j < strlen2) {
            if (j < 0 || haystack[i] == needle[j]) {
                i++;
                j++;
            } else {
                j = next[j];
            }
        }

        free(next);

        if (j >= strlen2)
            return i - j;
        else 
            return -1;
    }
}
// @lc code=end

