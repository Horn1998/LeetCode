#time 5.71 room 5.37
class Solution:
    def wordBreak(self, s: str, wordDict):
        word_len = len(s)
        judge_matrix = [[0 for _ in range(word_len)] for _ in range(word_len)]
        #记录步长
        for step in range(word_len):
            for j in range(word_len - step):
                if s[j:j+step + 1] in wordDict:
                    judge_matrix[j][j + step] = 1
                for k in range(j, j+step):
                    if judge_matrix[j][k] == 1 and judge_matrix[k+1][j+step] == 1:
                        judge_matrix[j][j+step] = 1
        if judge_matrix[0][len(s) - 1] == 1:
            return True
        else:
            return False