#time 80 room 10
'''
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
题目分析：
本题使用动态规划，讨论每次以新加入符号结尾的子串最大长度(动态规划，关联关系最难找）
A:以左括号结尾，不存在符合题意要求子串 dp[i] = 0
B:以右括号结尾
                B1：倒数第二个为左括号，正合适匹配，最长字串为 2(当前匹配括号） + dp[i - 2](当前匹配括号之前最长可拼接子串）
                B2: 倒数第二个为右括号（m)，以m结尾的最长子串已知为S，继续分情况讨论
                    B21:去掉以m结尾括号后还是右括号，此右括号一定多余，否则会合并到以m为结尾子串中，此情况不再影响最长子串问题
                    B22:去掉以m结尾括号后是左括号n，可以与新加入的右括号配对，目前最长字串长度为 S + 2，n左侧依然可能存在可拼接最长匹配子串T
                        T = dp[i - S - 2](dp[i - S - 1] 为 n)，故最长子串长度为 S + 2 + T
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        #动态规划
        #以i结尾的最长子串
        dp = [0 for _ in range(len(s) + 1)]
        s = ')' + s
        for i in range(1, len(s)):
            if s[i] == '(':
                dp[i] = 0
            elif s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                elif s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - dp[i - 1]  - 2]+ dp[i - 1] + 2
        return max(dp)