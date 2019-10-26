'''
1230. 抛掷硬币  显示英文描述
有一些不规则的硬币。在这些硬币中，prob[i] 表示第 i 枚硬币正面朝上的概率。
请对每一枚硬币抛掷 一次，然后返回正面朝上的硬币数等于 target 的概率。
'''
class Solution:
    def probabilityOfHeads(self, prob, target: int) -> float:
        # dp 投掷前j枚骰子， i次朝上
        dp = [[0 for _ in range(i + 1)] for i in range(len(prob) + 2)]
        for i in range(1, len(prob) + 1):
            def digui1(i):
                if i == 0:
                    return 1 - prob[0]
                return digui1(i - 1) * (1 - prob[i])

            def digui2(i):
                if i == 0:
                    return prob[0]
                return digui1(i - 1) * prob[i]

            dp[i][0] = digui1(i - 1)
            dp[i][1] = digui2(i - 1)
        for j in range(2, len(prob) + 1):
            for i in range(1, min(j + 1, target + 1)):
                if j - 1 >= i:
                    dp[j][i] = dp[j - 1][i] * (1 - prob[j - 1]) + dp[j - 1][i - 1] * prob[j - 1]
                else:
                    dp[j][i] = dp[j - 1][i - 1] * prob[j - 1]
                if j == len(prob) and i == target:
                    return dp[len(prob)][target]
        return dp[len(prob)][target]
