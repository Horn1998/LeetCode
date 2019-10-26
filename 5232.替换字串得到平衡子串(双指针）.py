'''
5232. 替换子串得到平衡字符串  显示英文描述
有一个只含有 'Q', 'W', 'E', 'R' 四种字符，且长度为 n 的字符串。
假如在该字符串中，这四个字符都恰好出现 n/4 次，那么它就是一个「平衡字符串」。
给你一个这样的字符串 s，请通过「替换子串」的方式，使原字符串 s 变成一个「平衡字符串」。
你可以用和「待替换子串」长度相同的 任何 其他字符串来完成替换。
请返回待替换子串的最小可能长度。
如果原字符串自身就是一个平衡字符串，则返回 0。
'''
class  Solution:
    def balancedString(self, s):
        #初始化需要参数
        length = len(s)
        n = length // 4 #整除获取平衡状态下每个数字应该出现的次数
        counts = [0 for _ in range(4)]              #记录每个字母出现次数
        dicts = {'Q':0, 'W':1, 'E':2, 'R':3}       #确定字母与位置之间映射关系
        dp = [[0, 0, 0, 0] for _ in range(length)]
        need = [0 for _ in range(4)]
        #初始化
        for i in range(length):
            index = dicts[s[i]]
            counts[index] += 1
            dp[i] = [counts[j] for j in range(4)]

        #记录字母超出平均值的个数
        need = [counts[i] - n if counts[i] > n else 0 for i in range(4)]
        #如果全为0 直接输出平衡状态值0
        if sum(need) == 0:
            return 0

        #下方参考题解
        #采用双指针，求取含有所有超额字母的最小情况
        last = length - 1
        for i in range(length):
            if dp[i][0] >= need[0] and dp[i][1] >= need[1] and dp[i][2] >= need[2] and dp[i][3] >= need[3]:
                last = i
                break

        i, j = 0, last
        res = last + 1
        while i < length and j < length:
                if dp[j][0] - dp[i][0] < need[0] or dp[j][1] - dp[i][1] < need[1] or dp[j][2] - dp[i][2] < need[2] or dp[j][3] - dp[i][3] < need[3]:
                    j += 1
                else:
                    res = min(j - i, res)
                    i += 1
        return res



