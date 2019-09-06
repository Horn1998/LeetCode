#递归+循环 时间：58 空间：5
def setZeroes(matrix):
    def setzero(x, y):
        for i in range(len(matrix)):
            matrix[i][y] = 0
        for j in range(len(matrix[0])):
            matrix[x][j] = 0
    def traceback(x, y):
        judge = 0
        if x == len(matrix) - 1 and y == len(matrix[0]) - 1:
            return
        for i in range(x,len(matrix)):
            for j in range(y, len(matrix[0])):
                if matrix[i][j] == 0:
                    if j + 1 <= len(matrix[0]) - 1:
                        traceback(i, j + 1)
                    else:
                        traceback(i + 1, 0)
                    setzero(i, j)
                    judge = 1
                    break
            y = 0
            if judge == 1:
                    break
    traceback(0, 0)
    print(matrix)
setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]])
