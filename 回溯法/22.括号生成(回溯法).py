#中等 回溯法 代码学习
def generateParenthesis(n):
    ans = []
    def backtrack(S = '',left = 0, right = 0):
        if len(S) == 2 * n:
            ans.append(S)
            return
        if left < n:
            backtrack(S + '(',left + 1, right)
        if left > right:
            backtrack(S + ')',left, right + 1)
    backtrack()
    print(ans)
if __name__ == '__main__':
    generateParenthesis(4)

