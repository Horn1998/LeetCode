#8:中等 正则表达式
import re
class Solution:
    def myAtoi(self, s):
        for key, i in enumerate(s):
            if i != " ":
                s = s[key:]
                break
        ans = ""
        rev = s.split(" ")[0]
        judge = 0
        if rev == "":
            return 0
        if rev[0] in ['-', '+'] or rev[0] in [str(j) for j in range(0, 10)]:
            ans += rev[0]
            judge = 1

        for i in rev[1:]:
            if i not in [str(j) for j in range(0, 10)] or judge == 0:
                break
            else:
                ans += i
        if ans == "" or ans == "+" or ans == "-":
            ans = 0
        else:
            ans = int(ans)
        if ans < (-1) * pow(2, 31):
            return -2147483648
        elif ans >= 2147483648:
            return 2147483647
        else:
            return ans

#大神解答
#正则表达式
#lstrip()去除开头空格
class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 1<<31 - 1), -2**31)
