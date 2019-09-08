class Solution:
    min = pow(2, 31)
    def uniquePathsWithObstacles(self, obstacleGrid):
        len_x = len(obstacleGrid)
        len_y = len(obstacleGrid[0])
        def tracktrace(x, y, save):
            if x >= len_x or y >= len_y or save >= self.min:
                return
            elif x == len_x - 1 and y == len_y- 1:
                if self.min > save:
                    self.min = save
                return
            else:
                s1, s2 = 0, 0
                if x + 1 <= len_x - 1:
                    s1 = save + obstacleGrid[x+1][y]
                tracktrace(x + 1, y, s1)
                if y + 1 <= len(obstacleGrid[0]) - 1:
                    s2 = save + obstacleGrid[x][y + 1]
                tracktrace(x, y + 1, s2)
        tracktrace(0, 0, obstacleGrid[0][0])
        print(self.min)
        return self.min
if __name__ == '__main__':
    s = Solution()
    s.uniquePathsWithObstacles([[5,0,1,1,2,1,0,1,3,6,3,0,7,3,3,3,1],[1,4,1,8,5,5,5,6,8,7,0,4,3,9,9,6,0],[2,8,3,3,1,6,1,4,9,0,9,2,3,3,3,8,4],[3,5,1,9,3,0,8,3,4,3,4,6,9,6,8,9,9],[3,0,7,4,6,6,4,6,8,8,9,3,8,3,9,3,4],[8,8,6,8,3,3,1,7,9,3,3,9,2,4,3,5,1],[7,1,0,4,7,8,4,6,4,2,1,3,7,8,3,5,4],[3,0,9,6,7,8,9,2,0,4,6,3,9,7,2,0,7],[8,0,8,2,6,4,4,0,9,3,8,4,0,4,7,0,4],[3,7,4,5,9,4,9,7,9,8,7,4,0,4,2,0,4],[5,9,0,1,9,1,5,9,5,5,3,4,6,9,8,5,6],[5,7,2,4,4,4,2,1,8,4,8,0,5,4,7,4,7],[9,5,8,6,4,4,3,9,8,1,1,8,7,7,3,6,9],[7,2,3,1,6,3,6,6,6,3,2,3,9,9,4,4,8]])

#动态规划 用时：55% 内存：5%
def secondAnswer(obstacleGrid):
    for i in range(1, len(obstacleGrid)):
        obstacleGrid[i][0] = obstacleGrid[i - 1][0] + obstacleGrid[i][0]
    for j in range(1, len(obstacleGrid[0])):
        obstacleGrid[0][j] += obstacleGrid[0][j - 1]

    for i in range(1, len(obstacleGrid)):
        for j in range(1, len(obstacleGrid[0])):
            obstacleGrid[i][j] += min(obstacleGrid[i - 1][j], obstacleGrid[i][j - 1])

    return obstacleGrid[-1][-1]
secondAnswer([
  [1,3,1],
  [1,5,1],
  [4,2,1]
])