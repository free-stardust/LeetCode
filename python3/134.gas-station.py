#
# @lc app=leetcode.cn id=134 lang=python3
# @lcpr version=30204
#
# [134] 加油站
#
# https://leetcode.cn/problems/gas-station/description/
#
# algorithms
# Medium (47.37%)
# Likes:    1669
# Dislikes: 0
# Total Accepted:    402.2K
# Total Submissions: 850.3K
# Testcase Example:  '[1,2,3,4,5]\n[3,4,5,1,2]'
#
# 在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
#
# 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
#
# 给定两个整数数组 gas 和 cost ，如果你可以按顺序绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。如果存在解，则 保证 它是 唯一
# 的。
#
#
#
# 示例 1:
#
# 输入: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# 输出: 3
# 解释:
# 从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
# 开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
# 开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
# 开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
# 开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
# 开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
# 因此，3 可为起始索引。
#
# 示例 2:
#
# 输入: gas = [2,3,4], cost = [3,4,3]
# 输出: -1
# 解释:
# 你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
# 我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
# 开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
# 开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
# 你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
# 因此，无论怎样，你都不可能绕环路行驶一周。
#
#
#
# 提示:
#
#
# gas.length == n
# cost.length == n
# 1 <= n <= 10^5
# 0 <= gas[i], cost[i] <= 10^4
#
#
#

# @lcpr-template-start
import copy
import collections
import random
import math
from collections import namedtuple
from typing import List, Tuple
from typing import Optional
from heapq import heapify, heappop, heappush


# @lcpr-template-end
# @lc code=start
class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        len_gas = len(gas)
        i = 0

        while i < len_gas:
            cnt, sum_gas, sum_cost = 0, 0, 0
            while cnt < len_gas:
                j = (i + cnt) % len_gas
                sum_gas += gas[j]
                sum_cost += cost[j]
                if sum_gas < sum_cost:
                    break
                cnt += 1
            if cnt == len_gas:
                return i
            else:
                i = i + cnt + 1

        return -1


# @lc code=end

tests = [[[1, 2, 3, 4, 5], [3, 4, 5, 1, 2]], [[2, 3, 4], [3, 4, 3]]]
ans = [3, -1]
all_pass = True
for i, (t, a) in enumerate(zip(tests, ans)):
    res = Solution().canCompleteCircuit(t[0], t[1])
    all_pass &= a == res
    print(f"test case {i+1}:\n"
          f"\ttest = {t};\n"
          f"\tans = {a};\n"
          f"\tres = {res};\n"
          f"\t{a == res};")
print(f"all pass: {all_pass}.")

#
# @lcpr case=start
# \n
# @lcpr case=end

# @lcpr case=start
# [2,3,4]\n[3,4,3]\n
# @lcpr case=end

#
