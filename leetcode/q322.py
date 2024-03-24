# https://leetcode.cn/problems/coin-change
# 322. 零钱兑换
# 动态规划状态转移方程
# amount < 0, dp[amount] = -1
# amount = 0, dp[amount] = 0
# amount > 0, dp[amount] = min(dp[amount - coin] + 1), coin in coins

from typing import List

class Solution:


    def coinChange(self, coins: List[int], amount: int) -> int:
        # 初始化数据并填充
        dp = [amount+1] * (amount + 1)
        dp[0] = 0

        # 外层循环：自底向上求解
        for i in range(1, amount + 1):
            # 内层循环：遍历所有的硬币面值
            for coin in coins:
                # 当前金额小于硬币面值，跳过；即，子问题无解
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[amount] == amount + 1 else dp[amount]