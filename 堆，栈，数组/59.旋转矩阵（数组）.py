#时间 34% 空间 5%
def generateMatrix(n):
    matrix = [[0 for i in range(n)] for j in range(n)]
    count = n*n
    x, y = -1, -1
    while count > 0:
        #x方向
        x += 1
        y += 1
        while  y < n and matrix[x][y] == 0 and count > 0:
            matrix[x][y] = n*n - count + 1
            count -= 1
            y += 1
        #右侧
        y -= 1
        x += 1
        while x < n and matrix[x][y] == 0 and count > 0:
            matrix[x][y] = n*n - count + 1
            count -= 1
            x += 1
        #底侧
        x -= 1
        y -= 1
        while y >= 0 and matrix[x][y] == 0 and count > 0:
            matrix[x][y] = n*n -count + 1
            count-=1
            y -= 1
        #左侧
        y += 1
        x -= 1
        while x >= 0 and matrix[x][y]== 0 and count > 0:
            matrix[x][y] = n*n -count + 1
            count -= 1
            x -= 1

if __name__ == '__main__':
    generateMatrix(4)
