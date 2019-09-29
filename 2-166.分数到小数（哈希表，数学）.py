class Solution:
    def fractionToDecimal(self, numerator, denominator) :
        integer = int(numerator / denominator)
        ans = str(abs(integer))
        if numerator / denominator < 0:
            ans = '-' + ans
        remember_integer = []  # 用于记录商
        left = numerator - integer * denominator
        remember_left = [left]  # 用于记录余数
        # 下面开始求取余数
        while left != 0:  # 如果仍然有余数
            left *= 10
            remember_integer.append(int(left / denominator))
            left = left - int(left / denominator) * denominator
            if left in remember_left:
                pos = remember_left.index(left)
                count = 0
                ans += "."
                for i in remember_integer:
                    if count == pos:
                        ans += "("
                    count += 1
                    ans += str(abs(i))
                ans += ")"
                break
            remember_left.append(left)
        if left == 0 and len(remember_integer) > 0:
            ans += '.'
            for i in remember_integer:
                ans += str(abs(i))
        return ans


