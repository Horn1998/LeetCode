#time 75.81 room 5.02
class Solution:
    def reverseWords(self , s) :
        ans = ""
        temp, answer = [], [s]
        first = len(answer)
        second = 0
        while True:
            if first == second:
                break
            first = second
            for j in answer:
                for i in j.split(' '):
                    temp.append(i)
            second = len(temp)
            print(temp)
            answer = temp
            temp = []
        for i in answer:
            if '' != i:
                if ans == "":
                    ans = i
                    continue
                ans = i + " " + ans
        return ans