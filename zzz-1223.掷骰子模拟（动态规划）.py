'''
有一个骰子模拟器会每次投掷的时候生成一个 1 到 6 的随机数。

不过我们在使用它时有个约束，就是使得投掷骰子时，连续 掷出数字 i 的次数不能超过 rollMax[i]（i 从 1 开始编号）。

现在，给你一个整数数组 rollMax 和一个整数 n，请你来计算掷 n 次骰子可得到的不同点数序列的数量。

假如两个序列中至少存在一个元素不同，就认为这两个序列是不同的。由于答案可能很大，所以请返回 模 10^9 + 7 之后的结果。

'''
#time 55 room 100
class Solution:
    def dieSimulator(self, n: int, rollMax) -> int:
        #数组由内到外分别是 重复次数， 骰子点数， 掷出次数
        dp = [[[0 for _ in range(16)] for _ in range(6)] for _ in range(n)]
        #动态规划
        MOD = 10 ** 9 + 7
        for i in range(6):
            dp[0][i][1] = 1
        for i in range(1,n):          #第i轮
            for j in range(6):      #第i次投出j点
                for k in range(6):  #第i - 1次投出k点
                    #当第i-1次与第i次不同时
                    if j != k:
                        dp[i][j][1] += sum(dp[i - 1][k])%MOD
                    else:
                        for m in range(2, rollMax[j - 1] + 1):
                            dp[i][j][m] = dp[i - 1][j][m - 1]
        Sum = [0 for _ in range(6)]
        for i in range(6):
            Sum[i]= sum(dp[n - 1][i]) % MOD
        return sum(Sum)  % MOD
