#困难
#法一：暴力动态规划
#time 14 room 5
'''
解题思路：
对于矩阵中每个点（i，j)求取以该点为矩形右下角点的最大矩形面积
先从第j行开始计算，然后依次向上增加行数，知道某一行a对应的宽度dp[a][j] 为0 时停止计算
'''
class Solution:
    def maximalRectangle(self, matrix) -> int:
        if not matrix: return 0
        row, col = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        tot, res = 0, 0
        #动态规划求最大面积，由于第一行第一列已知，所以从第二行第二列开始遍历
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1':
                    #从当前层向上遍历找最大矩形面积
                    temp = i - 1 #记录当前层数
                    start = dp[i][j - 1] + 1 #记录初始面积
                    Min_width = dp[i][j - 1] + 1
                    dp[i][j] = Min_width
                    while temp >= 0 and dp[temp][j] != 0:
                        Min_width = min(Min_width, dp[temp][j])
                        if start != dp[i][j] * (i - temp + 1) :
                            dp[i][j] =dp[i][j - 1] + 1
                        start = max(start, (i - temp + 1) * Min_width)
                        temp -= 1
                    res = max(res, start)
        return res


#法二，单调栈 time 40 room 5
'''
矩阵最大面积收到84题启发
采用单调栈求取最大面积，具体思路参考84题
'''
import copy
class Solution:
    def maximalRectangle(self, matrix) -> int:
        #逐行单调栈求取最大面积
        if not matrix: return 0
        row, col = len(matrix), len(matrix[0])
        temp = [0 for _ in range(col + 1)] #记录当前状态下的行高 col + 1保证最后栈中所有元素弹出
        res = 0 #存取结果
        #从最顶层开始计算
        for scale in range(row):
            #初始化栈的状态
            st = []#单调栈
            #获取当前状态下的行高 自上而下
            for i in range(col):
                if matrix[scale][i] == '1':
                    temp[i] += 1
                else:
                    temp[i] = 0
            heights = copy.deepcopy(temp)
            #单调栈求取最大面积
            for i in range(col + 1):
                #单调递增栈
                if st and heights[i] < heights[st[-1]] :
                    while st and heights[i] < heights[st[-1]]:
                        top = st.pop()
                        res = max(heights[top] * (i - top), res)
                    st.append(top)
                    heights[top] = heights[i]
                else:
                    st.append(i)
        return res