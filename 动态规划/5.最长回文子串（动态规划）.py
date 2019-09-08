#中等-5 动态规划
def longestPalindrome(s):
    max = -1
    map = [[0 for i in range(len(s))] for i in range(len(s))]
    if len(s) == 1:
        return s
    elif len(s) == 0:
        return ""
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            map[i][i+1] = map[i+1][i] = 2
            max = 2
        else:
            map[i][i+1] = map[i+1][i] = 0
    for i in range(1,len(s) - 1):
        if s[i-1] == s[i+1]:
            map[i-1][i+1] = map[i+1][i-1] = 3
            max = 3
        else:
            map[i-1][i+1] = map[i+1][i-1] = 0

    for step in range(4,len(s)+1):
        for begin in range(len(s) - step + 1):
                if map[begin+1][begin + step -2] != 0 and s[begin]==s[begin+step-1]:
                    map[begin][begin + step -1] = step
                    if step > max:
                        max = step
                else:
                    map[begin][begin + step -1] = 0
    for i in range(len(map)):
        print(map[i])
    for i in range(len(map)):
        for j in range(len(map)):
            if max == map[i][j]:
                print(s[i:j+1])
                return s[i:j+1]
    return s[0]



        #     if s[begin] == s[begin + step]:
        #         map[begin][begin + step] = map[begin+step][begin] =1
        #     else:
        #         map[begin][begin+step] = map[begin +step][begin] = 0
if __name__ == '__main__':
    longestPalindrome("aaaa")

