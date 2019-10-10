class Solution:
    judge = False
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not len(matrix):
            return False
        col = len(matrix[0])
        row = len(matrix)
        J = [[False for _ in range(col)] for _ in range(row)]
        def digui(x, y, row, col):
            if x < 0 or y < 0 or x >= row or y >= col or self.judge == True or J[x][y] == True:
                return
            J[x][y] = True
            if matrix[x][y] == target:
                self.judge = True
            elif matrix[x][y] < target:
                digui(x + 1, y, row, col)
                digui(x, y + 1, row, col)
            elif matrix[x][y] > target:
                digui(x - 1, y, row, col)
                digui(x, y - 1, row, col)
        digui(0, 0, row, col)
        return self.judge