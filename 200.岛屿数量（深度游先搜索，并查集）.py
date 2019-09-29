#time 80.83 room 14.32
class Solution:
    def numIslands(self, grid) :
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        if len(grid) == 0:
            return 0
        row, col = len(grid), len(grid[0])
        islands = 0
        def move(x, y, row, col):
            if  x < 0 or x >= row or y < 0 or y >= col or grid[x][y] == 0:
                return
            elif grid[x][y] == '1':
                grid[x][y] = '0'
                for direction in directions:
                    move(x + direction[0], y + direction[1], row, col)
        for x in range(row):
            for y in range(col):
                if grid[x][y] == '1':
                    move(x, y, row, col)
                    islands += 1
        return islands