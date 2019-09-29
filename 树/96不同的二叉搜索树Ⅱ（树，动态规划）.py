# Definition for a binary tree node.
#时间 69.45 空间 6.03
class Solution:
    def numTrees2(self, n):
       lists = [0 for i in range(0, n+1)]
       self.ans = 0
       for i in range(1, n+1):
           self.ans = 0
           if i == 1:
               lists[0] = 1
               lists[1] = 1
           else:
               for j in range(1,i+1):
                   self.ans += lists[j-1]*lists[i - j]
               lists[i] = self.ans
       print(lists[n])

if __name__ == '__main__':
    s = Solution()
    s.numTrees2(2)

