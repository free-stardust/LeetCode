/*
 * @lc app=leetcode.cn id=23 lang=cpp
 * @lcpr version=30204
 *
 * [23] 合并 K 个升序链表
 *
 * https://leetcode.cn/problems/merge-k-sorted-lists/description/
 *
 * algorithms
 * Hard (60.04%)
 * Likes:    2859
 * Dislikes: 0
 * Total Accepted:    843.7K
 * Total Submissions: 1.4M
 * Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
 *
 * 给你一个链表数组，每个链表都已经按升序排列。
 *
 * 请你将所有链表合并到一个升序链表中，返回合并后的链表。
 *
 *
 *
 * 示例 1：
 *
 * 输入：lists = [[1,4,5],[1,3,4],[2,6]]
 * 输出：[1,1,2,3,4,4,5,6]
 * 解释：链表数组如下：
 * [
 * ⁠ 1->4->5,
 * ⁠ 1->3->4,
 * ⁠ 2->6
 * ]
 * 将它们合并到一个有序链表中得到。
 * 1->1->2->3->4->4->5->6
 *
 *
 * 示例 2：
 *
 * 输入：lists = []
 * 输出：[]
 *
 *
 * 示例 3：
 *
 * 输入：lists = [[]]
 * 输出：[]
 *
 *
 *
 *
 * 提示：
 *
 *
 * k == lists.length
 * 0 <= k <= 10^4
 * 0 <= lists[i].length <= 500
 * -10^4 <= lists[i][j] <= 10^4
 * lists[i] 按 升序 排列
 * lists[i].length 的总和不超过 10^4
 *
 *
 */

// @lcpr-template-start
#include <algorithm>
#include <array>
#include <bitset>
#include <climits>
#include <cstddef>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <new>
#include <queue>
#include <stack>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;
// @lcpr-template-end
struct ListNode {
    int val;
    ListNode *next;
    ListNode() :
        val(0), next(nullptr) {
    }
    ListNode(int x) :
        val(x), next(nullptr) {
    }
    ListNode(int x, ListNode *next) :
        val(x), next(next) {
    }
};
// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode *mergeTwoList(ListNode *l1, ListNode *l2) {
        if (l1 == nullptr) return l2;
        if (l2 == nullptr) return l1;

        ListNode *head;

        if (l1->val <= l2->val) {
            head = l1;
            l1->next = mergeTwoList(l1->next, l2);
        } else {
            head = l2;
            l2->next = mergeTwoList(l1, l2->next);
        }

        return head;
    }

    ListNode *mergeTwoPart(vector<ListNode *> &lists, int left, int right) {
        int size = right - left + 1;

        if (size == 0) return nullptr;
        if (size == 1) return lists[left];
        if (size == 2) return mergeTwoList(lists[left], lists[right]);

        ListNode *l1 = mergeTwoPart(lists, left, left + size / 2);
        ListNode *l2 = mergeTwoPart(lists, left + size / 2 + 1, right);

        return mergeTwoList(l1, l2);
    }

    ListNode *divide_and_conquer(vector<ListNode *> &lists) {
        return mergeTwoPart(lists, 0, lists.size() - 1);
    }

    ListNode *mergeKLists(vector<ListNode *> &lists) {
        return divide_and_conquer(lists);
    }
};
// @lc code=end
int main() {
    auto add = [](int a, int b) {
        return a + b;
    };
    cout << add(1, 2) << endl;
    return 0;
}
/*
// @lcpr case=start
// [[1,4,5],[1,3,4],[2,6]]\n
// @lcpr case=end

// @lcpr case=start
// []\n
// @lcpr case=end

// @lcpr case=start
// [[]]\n
// @lcpr case=end

 */
