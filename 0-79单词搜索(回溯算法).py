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