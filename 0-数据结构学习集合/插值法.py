#定义已知数据
#定义插值阶数为9
#定义样本集
x = [i for i in range(10)]
y = [i ** 2 for i in range(10)]
#动态规划求解均差表
dp = [[0 for _ in range(n + 1)] for n in range(10)]
for i in range(10):
    dp[i][0] = y[i]
#开始插值
#第n次插值
for n in range(1, 10):
    #遍历上一次插值结果
    for i in range(n, 10):
        #计算分子
        diff_zi = dp[i - 1][n - 1] - dp[i][n - 1]
        #计算分母
        diff_mu = x[i - n] - x[i]
        dp[i][n] = diff_zi / diff_mu
print(dp)

#求差值函数
def diff_func(args, i, n):
    if i == n - 1:
        return dp[i][i]
    return dp[i][i] + (args - x[i]) * diff_func(args, i + 1, n)

ans = diff_func(3, 0, 10)
print(ans)