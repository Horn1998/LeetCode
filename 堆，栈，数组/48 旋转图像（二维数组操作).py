def rotate(matrix):
    for j in range(len(matrix),int(0.5 * len(matrix)),-1):

        ls = [matrix[len(matrix) - j  + i][j - 1] for i in range(- len(matrix) + 2 * j)]
        ls.reverse()

        for k in range(-len(matrix) + 2 * j - 1, -1 , -1):
            matrix[len(matrix) - j + k][j - 1] = matrix[len(matrix) - j][len(matrix) - j + k]

        for k in range(-len(matrix) + 2 * j - 1, -1, -1):
            matrix[len(matrix) - j][k + len(matrix) - j] = matrix[j - k -1][len(matrix) - j]

        for k in range(-len(matrix) + 2*j):
            matrix[len(matrix) - j + k][len(matrix) - j] = matrix[j - 1][len(matrix) - j + k]
            print(matrix[j - 1][len(matrix) - j + k])

        for k in range(2*j - len(matrix)):
            matrix[j - 1][len(matrix) - j + k]= ls[k]
    print(matrix)
    return matrix

if __name__ == '__main__':
    rotate(
        [
            [15, 13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7, 10, 11]
        ]
)
#官方题解
class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n):
            for j in range(n-i):
                matrix[i][i+j],matrix[i+j][i]=matrix[i+j][i],matrix[i][i+j]
        for i in range(n):
            matrix[i].reverse()