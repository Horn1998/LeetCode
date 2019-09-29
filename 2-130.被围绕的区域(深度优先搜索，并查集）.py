#time 27.51 room 5.30
class Solution:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def solve(self, board):
        row = len(board)
        if row == 0:
            return []
        col = len(board[0])
        save = [[board[x][y] for y in range(col)] for x in range(row)]
        for i in range(row):
            for j in range(col):
                if save[i][j] == "O":
                    if self._judge(i, j, save, row, col):
                        self._judge(i, j, board, row, col)

    def _judge(self, pos_x, pos_y, save, row, col):
        # 递归终止条件
        if pos_x < 0 or pos_x >= row or pos_y < 0 or pos_y >= col:
            return False
        elif save[pos_x][pos_y] == 'X':
            return True
        elif save[pos_x][pos_y] == 'O':
            save[pos_x][pos_y] = 'X'
            temp = 0  # 记录下一步是否成功
            for direction in self.directions:
                new_x = pos_x + direction[0]
                new_y = pos_y + direction[1]
                if self._judge(new_x, new_y, save, row, col):
                    temp += 1
            # 四个方向均没有到达边界
            if temp == 4:
                return True
            else:
                return False

