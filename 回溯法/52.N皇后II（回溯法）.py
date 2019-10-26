import copy
class Solution:
    ans = 0

    def totalNQueens(self, n: int) -> int:
        direction_x = [1, -1, 1, -1, 0, 0, 1, -1]
        direction_y = [1, 1, -1, -1, 1, -1, 0, 0]
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
                self.ans += 1
            for j in range(n):
                if x < n and put_Queen(matrix, x, j, n):
                    temp = copy.deepcopy(matrix)
                    temp[x][j] = 'Q'
                    digui(temp, x + 1, 0, n)

        digui(matrix, 0, 0, n)
        return self.ans