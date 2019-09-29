class Solution():
    ans = False
    def exist(self, board, word):
        self.words = word
        self.board = board
        def judge(x, y, w):
            len_x = len(board)
            len_y = len(board[0])
            if x >= 0 and y >= 0 and x < len_x and y < len_y and self.board[x][y] == w:
                self.board[x][y] += '0'
                return True
            return False
        def traceback(x, y, step):
            if self.ans == True:
                return
            if step == len(self.words):
                print("true")
                self.ans = True
                return
            elif judge(x, y, self.words[step]) == False:
                return
            else:
                traceback(x+1, y, step + 1)
                if x + 1 < len(self.board) and len(self.board[x+1][y]) == 2:
                    self.board[x+1][y] = self.board[x+1][y][0]
                traceback(x, y+1, step + 1)
                if y + 1 < len(self.board[0]) and len(self.board[x][y+1]) == 2:
                    self.board[x][y+1] = self.board[x][y+1][0]
                traceback(x, y - 1, step + 1)
                if y - 1 >= 0 and len(self.board[x][y - 1]) == 2:
                    self.board[x][y - 1] = self.board[x][y - 1][0]
                traceback(x-1, y,  step + 1)
                if x - 1 >= 0 and len(self.board[x-1][y]) == 2:
                    self.board[x-1][y] = self.board[x-1][y][0]

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.ans == True:
                    break
                elif self.board[i][j] == self.words[0]:
                    traceback(i, j, 0)
if __name__ == '__main__':
    s = Solution()
    s.exist([["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]],
"aaaaaaaaaaaa")
#二刷  time:88.11% room 17.67%
class Solution:
    directions = [(0, -1), (0,1), (1,0), (-1,0)]#记录方向
    def exist(self, board, word):
        row = len(board)
        if row == 0:
            return False
        col = len(board[0])

        #记录矩阵
        matrix = [[False for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and self._judge(i, j, word, matrix, row, col, 0, board):
                    return True
        return False
    def _judge(self, pos_x, pos_y, word, judge_matrix, row, col, step, board):
        #递归终止条件
        if step == len(word) - 1:
            return board[pos_x][pos_y] == word[step]

        #中间过程匹配
        #回溯过程先将当前位置标识为已经访问
        if board[pos_x][pos_y] == word[step]:
            judge_matrix[pos_x][pos_y] = True
            for direction in self.directions:
                new_x = pos_x + direction[0]
                new_y = pos_y + direction[1]
                if 0 <= new_x < row and 0<= new_y < col and not judge_matrix[new_x][new_y] and self._judge(new_x,new_y, word, judge_matrix, row, col, step + 1, board):
                    return True
            #回溯最后将状态还原
            judge_matrix[pos_x][pos_y] = False
