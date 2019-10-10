class Solution:
    def findRepeatedDnaSequences(self, s):
        visited = set()
        res = set()
        for i in range(len(s) - 9):
            if s[i:i+10] in visited:
                res.add(s[i:i+10])
            visited.add(s[i:i+10])
        return list(res)