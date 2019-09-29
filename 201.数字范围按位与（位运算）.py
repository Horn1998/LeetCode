#time 38 room 5
class Solution:
    def rangeBitwiseAnd(self, m, n) :
        # 记录步长的二进制长度
        def get_Binary(num):
            binary = ""
            while (num > 1):
                binary = str(num % 2) + binary
                num = int(num / 2)
            binary = str(num) + binary
            return binary

        before = get_Binary(m)
        after = get_Binary(n)
        if len(before) < len(after):
            return 0

        for i in range(len(after)):
            if after[i] == before[i]:
                continue
            else:
                after = after[:i]
                for j in range(i, len(before)):
                    after += '0'
                break
        sum = 0
        for i in range(0, len(after)):
            sum = sum * 2 + int(after[i])
        return sum