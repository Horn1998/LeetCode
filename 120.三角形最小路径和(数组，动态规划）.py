#time :79.42 room :5.04
class Solution:
    def minimumTotal(self, triangle) :
        if triangle == []:
            return 0
        depth = len(triangle)
        #动态规划
        matrix = [[0 for j in range(depth)] for i in range(depth)]
        matrix[0][0] = triangle[0][0]
        #step当前所在层数
        def deep(step):
            if step >= len(triangle):
                return
            for i in range(len(triangle[step])):
                if i== 0:
                    matrix[step][0] = triangle[step][0] + matrix[step-1][0]
                elif i == len(triangle[step]) - 1:
                    matrix[step][i] = triangle[step][i] + matrix[step-1][len(triangle[step-1])-1]
                elif matrix[step-1][i-1] > matrix[step-1][i]:
                    matrix[step][i] = triangle[step][i] + matrix[step-1][i]
                else:
                    matrix[step][i] = triangle[step][i] + matrix[step-1][i-1]
            deep(step + 1)
        deep(1)
        min = 100000000
        for i in range(len(matrix)):
            if min > matrix[depth - 1][i]:
                min = matrix[depth - 1][i]
        return min
    # def minimumTotal(self, triangle:List[List[int]]) -> int:
    #     if triangle == []:
    #         return 0
    #     depth = len(triangle)

