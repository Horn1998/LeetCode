#time 89.62 room 7
#思路为以运算符为分界线，递归计算左侧与右侧运算结果数组，并将其作为返回值
class Solution:
    def diffWaysToCompute(self, input: str):
        sign = ['+', '-', '*', '/']

        def digui(input):
            results = []
            for i in range(len(input)):
                if input[i] in sign:
                    x = digui(input[:i])
                    y = digui(input[i + 1:])
                    if input[i] == '*':
                        for left in x:
                            for right in y:
                                results.append(right * left)
                    elif input[i] == '/':
                        for left in x:
                            for right in y:
                                results.append(int(left / right))
                    elif input[i] == '+':
                        for left in x:
                            for right in y:
                                results.append(right + left)
                    elif input[i] == '-':
                        for left in x:
                            for right in y:
                                results.append(left - right)
            if not results:
                return [int(input)]
            return results

        ans = digui(input)
        ans.sort()
        return ans










