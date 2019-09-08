#时间 5 空间 6
import copy
class Solution:
    start = 0
    def subsets(self, nums):
        ans = []
        length = len(nums)
        #step记录步数，步数达到length可以加入结果集
        def traceback(save, step, num):
            if step == length:
            #如果步长等于nums，将结果加入结果集
                ans.append(save)
                return
            for i in range(num, length):
                temp1 = copy.deepcopy(save)
                temp1.append(nums[i])
                traceback(temp1, step + 1, i + 1)
                temp2 = copy.deepcopy(temp1[:-1])
                traceback(temp2, step + 1, i + 1)
        traceback([], 0, 0)
        print(ans)
        return ans
if __name__ == '__main__':
    s = Solution()
    s.subsets([1,3,9])

#大神题解
class Solution:
    start = 0
    def subsets(self, nums ):
        ans = []
        length = len(nums)
        #step记录步数，步数达到length可以加入结果集
        def traceback(save, step, num):
            if step == length:
            #如果步长等于nums，将结果加入结果集
                ans.append(save)
            else:
                # temp = copy.deepcopy(save)
                # traceback(temp, step + 1)
                # if len(save) == 0:
                #     self.start = 0
                # else:
                #     self.start = save[-1] + 1
                for i in range(num, length):
                    temp1 = copy.deepcopy(save)
                    temp1.append(nums[i])
                    traceback(temp1, step + 1, nums[i])
                    temp2 = copy.deepcopy(temp1[:-1])
                    traceback(temp2, step + 1, nums[i])
        traceback([], 0, 0)
        print(ans)
        return ans