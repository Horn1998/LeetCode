#time 76.45 room 5.23
class Solution:
    def evalRPN(self, tokens):
        degree = {}
        degree['+'], degree['-'], degree['*'], degree['/'] = 1, 1, 2, 2
        stack_number, stack_sign = [], []
        for i in tokens:
            if i in degree.keys():
                num2 = stack_number.pop()
                num1 = stack_number.pop()
                if i == '+':
                    stack_number.append(num2 + num1)
                elif i == '-':
                    stack_number.append(num1 - num2)
                elif i == '*':
                    stack_number.append(num1 * num2)
                elif i == '/':
                    stack_number.append(int(num1 / num2))
            else:
                stack_number.append(int(i))
        return stack_number.pop()

