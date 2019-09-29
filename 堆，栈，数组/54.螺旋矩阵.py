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
#     spiralOrder(
#         [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# )
    pass


#二刷  time 96.69  room 5.66
def spiralOrder(matrix):
    if not matrix: return []
    R, C = len(matrix), len(matrix[0])
    seen = [[False] *C for _ in matrix]
    ans = []
    dr = [0, 1, 0 , -1]
    dc = [1, 0 , -1, 0]
    r = c = di = 0
    for _ in range(R*C):
        ans.append(matrix[r][c])
        seen[r][c] = True
        rr, cc = r + dr[di], c + dc[di]
        if 0<=cc< C and 0<=rr< R and seen[rr][cc] == False:
            c, r = cc, rr
        else:
            di = (di + 1)%4
            c, r = c + dc[di], r + dr[di]
    print(ans)
    return ans
spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])
