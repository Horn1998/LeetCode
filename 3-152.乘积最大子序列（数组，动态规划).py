#TIME 31.77 ROOM 5.34
class Solution:
    def maxProduct(self, nums):
        #特殊情况处理
        if len(nums) == 0:
            return 0
        move_one, Max = [], nums[0]
        #除去1与-1减少动态规划难度
        for i in nums:
            if Max < i:
                Max = i
            if i == 1 or (i == -1 and len(move_one) > 2 and move_one[-1] == -1 and move_one[-2] == -1):
                continue
            else:
                move_one.append(i)
        #特殊情况处理
        if Max == 1:
            move_one.append(1)
        #开始动态规划
        nums = move_one
        print(nums)
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        col, row = len(nums), len(nums)
        matrix = [[nums[i] for _ in range(col)] for i in range(row)]
        for step in range(1, len(nums)):
            for i in range(len(nums) - step):
                matrix[i][i+step] = matrix[i][i+step - 1] * nums[i + step]
                if Max < matrix[i][i+step]:
                    Max = matrix[i][i+step]
        return Max