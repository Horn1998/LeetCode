#hard
#time 76 room 15
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #构造字典集合
        dicts = {}
        for i in range(len(t)):
            dicts.setdefault(t[i], 0)
            dicts[t[i]] += 1
        #定义结果
        res = 100000000
        answer = (-1, -1)
        start, end = 0, len(s)
        #开始寻找最小子串
        for i in range(len(s)):
            #当前字母在要查找的子串中
            if s[i] in dicts.keys():
                dicts[s[i]] -= 1
                judge = 1
                #判断当前所取子串是否包含目标字串
                for j in dicts.keys():
                    if dicts[j] > 0:
                        judge = 0
                        break

                if judge:
                    #更新目标字串范围
                    end = i
                    #当前区间缩小
                    for k in range(start, end + 1):
                        if s[k] in dicts.keys():
                            dicts[s[k]] += 1
                            #缩小后的区间不能够包含子串所有字母
                            if dicts[s[k]] > 0:
                                start = k + 1
                                #判断当前区间是否为最小区间
                                if end - k + 1 < res :
                                    answer = (k, end)
                                    res = end - k + 1
                                break
        if answer == (-1, -1):
            return ""
        return s[answer[0]: answer[1] + 1]