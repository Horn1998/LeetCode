#time 92.86 room 17.65
#通过递归先计算加减再计算乘除
#在乘除运算中由于除法取整，所以需要严格按照从左向右计算方式
#由于字符串存在空格，可以用strip去除空格
#time 88 room 5
class Solution:
    def calculate(self, s):
        def child_calculate(s):
            if '-' in s:
                s_ans = child_calculate(s.split('-')[0].strip())

                for s_child in s.split('-')[1:]:
                    s_ans -= child_calculate(s_child.strip())
                return s_ans
            elif '*' in s or '/' in s:
                stack, anses = [], 1
                for s_child in s.split('*'):
                    ans = int(s_child.split('/')[0].strip()) * anses
                    for s_s_child in s_child.split('/')[1:]:
                        ans = int(ans / int(s_s_child.strip()))
                    anses = ans
                return anses
            else:
                return int(s.strip())

        def get_result(s):
            ans = []
            for s_child in s.split('+'):
                ans.append(child_calculate(s_child.strip()))
            return sum(ans)

        return get_result(s)
