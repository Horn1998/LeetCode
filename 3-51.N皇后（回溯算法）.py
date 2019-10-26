#time 5 room 5
import copy
class Solution:
    def solveNQueens(self, n: int):
        direction_x = [1, -1, 1, -1, 0, 0, 1, -1]
        direction_y = [1, 1, -1, -1, 1, -1, 0, 0]
        ans = []
        matrix = [['.' for _ in range(n)] for _ in range(n)]

        def move(matrix, x, y, pos_x, pos_y, n):
            if x < 0 or x >= n or y < 0 or y >= n:
                return True
            if matrix[x][y] == 'Q':
                return False
            return move(matrix, x + pos_x, y + pos_y, pos_x, pos_y, n)

        def put_Queen(matrix, x, y, n):
            count = 0
            for xs, ys in zip(direction_x, direction_y):
                if move(matrix, x, y, xs, ys, n):
                    count += 1
                else:
                    return False
            if count == 8:
                return True

        def digui(matrix, x, y, n):
            if x == n:
                save = []
                for i in range(n):
                    s = ""
                    for j in range(n):
                        s += matrix[i][j]
                    save.append(s)
                ans.append(save)
            for j in range(n):
                if x < n and put_Queen(matrix, x, j, n):
                    temp = copy.deepcopy(matrix)
                    temp[x][j] = 'Q'
                    digui(temp, x + 1, 0, n)

        digui(matrix, 0, 0, n)
        return ans

#官方题解一 time 95 room 5
class Solution:
    #回溯算法
    '''
    关键点:
    1.同一个主对角线，坐标和相同，同一个次对角线，坐标差相同, 且不同位置的点坐标的和与差一定与不在同一对角线上的点不同
    2.列表索引可以是负数，方便表示两坐标之间的差值
    3.回溯算法最后要恢复之前对已知条件的修改，实现回溯
    4.将二维矩阵通过队列和递归转化为一维列表问题
    '''
    def solveNQueens(self, n: int):
        #定义需要的参数
        queens = [] #设置一个位图
        place_sum, place_del = [True for _ in range(n * 2)], [True for _ in range(n * 2)]
        ans = [] #存储结果
        def backtrace(n):
            row = len(queens) - 1
            #终止条件，已经放置n个皇后
            if len(queens) == n:
                save = []
                for i in range(n):
                    s = '.' * (queens[i]) + 'Q' +'.' * (n - queens[i] - 1)
                    save.append(s)
                ans.append(save)
                return
            #查询当前列是否可以放置皇后
            for col in range(n):
                #fuck, the index can be negative，利用了python列表可表示负数的优势
                if col not in queens and place_sum[row + col] and place_del[col - row]:
                    queens.append(col)
                    place_sum[row + col], place_del[col - row] = False, False
                    #开始回溯
                    backtrace(n)
                    #回溯还原
                    queens.pop()
                    place_sum[row + col], place_del[col - row] = True, True
        backtrace(n)


#官方题解二
class Solution:
    #约束编程
    '''
    关键点： 目前还没有此方面题解
    '''
    def solveNQueens(self, n):
        pass
