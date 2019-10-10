class Solution:
    def maximalSquare(self, matrix) -> int:
        Max = 0
        if not matrix: return 0
        row = len(matrix)
        col = len(matrix[0])
        if row * col * int(matrix[0][0]) == 1:
            return 1
        if row * col == 1 and int(matrix[0][0]) == 0:
            return 0
        judge = [[[False for _ in range(1, min(col, row) + 1)] for _ in range(col)] for _ in range(row)]
        for x in range(row):
            for y in range(col):
                if matrix[x][y] == '1':
                    judge[x][y][0] = True
                    Max = 1
        for step in range(1, min(col, row) + 1):
            for x in range(row - step):
                for y in range(col - step):
                    # 左上角（x, y) 右下角（x+step, y + step)
                    if judge[x][y][step - 1] == True and judge[x][y + 1][step - 1] == True and judge[x + 1][y][
                        step - 1] == True and judge[x + 1][y + 1][step - 1] == True:
                        judge[x][y][step] = True
                        if Max < step + 1:
                            Max = step + 1
        return pow(Max, 2)
#题解
def maximalSquare(matrix):
    """
        1. dp问题, dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            当matrix[i][j] == '1'的时候
    """
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    res = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            #dp[i][j]对应matrix[i - 1][j - 1]点
            if matrix[i - 1][j - 1] == '1':
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                res = max(res, dp[i][j])

    return res * res
