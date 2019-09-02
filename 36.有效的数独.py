#中等 简单的二维数组操作
def isValidSudoku(board) -> bool:
    lists = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    def judge(m, n, y, x):  # m对应第几行 n对应第几列
        # 先判断相同行有没有一样的元素
        for i in range(len(board[m])):
            if board[m][i] == board[m][n] and i != n:
                return True
        # 判断相同列有没有一样的元素
        for j in range(len(board)):
            if board[j][n] == board[m][n] and m != j:
                return True
        # 判断一个九宫格内是否有相同的元素
        for i in range(3):
            for j in range(3):
                if (board[y[0] + i][x[0] + j] == board[m][n] and not (y[0] + i == m and x[0] + j == n)):
                    return True
        return False

    for y in lists:
        for x in lists:
            for m in y:
                for n in x:
                    if board[m][n] != '.' and judge(m, n, y, x):
                        return False

    return True
if __name__ == '__main__':
    isValidSudoku([
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],["6", ".", ".", "1", "9", "5", ".", ".", "."],[".", "9", "8", ".", ".", ".", ".", "6", "."],["8", ".", ".", ".", "6", ".", ".", ".", "3"],["4", ".", ".", "8", ".", "3", ".", ".", "1"],["7", ".", ".", ".", "2", ".", ".", ".", "6"],[".", "6", ".", ".", ".", ".", "2", "8", "."],[".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]


])

