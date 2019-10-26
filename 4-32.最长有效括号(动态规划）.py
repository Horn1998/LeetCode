#time 80 room 10
'''
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
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