#time:71.48 room:5.21
class Solution:
    def numDecodings(self, s):
        if int(s[0]) == 0 or "00" in s:
            return 0
        for i in range(len(s)):
            if int(s[i]) == 0 and int(s[i - 1]) > 2:
                return 0

        def digui(num):
            if num == 1:
                return 1
            elif num == 2:
                return 2
            else:
                return digui(num - 1) + digui(num - 2)

        count = 0
        pos = []
        for i in range(len(s)):
            if int(s[i]) < 3 and int(s[i]) > 0:
                count += 1
            elif int(s[i]) == 0:
                pos.append(count - 1)
                count = 0
            elif int(s[i - 1]) == 2 and int(s[i]) > 6:
                pos.append(count)
                count = 0
            else:
                pos.append(count + 1)
                count = 0
        if int(s[-1]) < 3:
            pos.append(count)
        temp = 1
        for j in range(len(pos)):
            if pos[j] != 0:
                temp *= digui(pos[j])
        return temp


