#90%超越度 完美
def spiralOrder(matrix):
    #获取矩阵初始长度
    if matrix== []:
        return []
    lenx = len(matrix[0])
    leny = len(matrix)
    all = lenx * leny
    #记录结果值
    ans = []
    #位置标记
    row, col= -1, -1
    while True:
        #顶侧
        col += 1
        row += 1
        if all <= 0:
            break
        while col < lenx and matrix[row][col] != -1000000:
            ans.append(matrix[row][col])
            matrix[row][col] = -1000000
            col += 1
            all -= 1
        #右侧
        row += 1
        col -= 1
        while row < leny and matrix[row ][col] !=  -1000000:
            ans.append(matrix[row][col])
            matrix[row][col] = -1000000
            row += 1
            all -= 1
        #底侧
        col -= 1
        row -= 1
        while col >= 0 and matrix[row][col] != -1000000:
            ans.append(matrix[row][col])
            matrix[row][col] = -1000000
            col -= 1
            all -= 1
        #左侧
        row -= 1
        col += 1
        while row >= 0 and matrix[row][col] != -1000000:
            ans.append(matrix[row][col])
            matrix[row][col] = -1000000
            row -= 1
            all -= 1
    print(ans)
if __name__ == '__main__':
    spiralOrder(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
)