#难度 ：中等 考察知识 回溯
import copy
def permute(nums):
    nums.sort()
    ans, save = [], []
    def recursion(lists, save):
        if len(lists) == 0:
            temp = copy.deepcopy(save)
            if temp not in ans:
                ans.append(temp)
            return

        for i in range(len(lists)):
            if i != len(lists) - 1:
                if lists[i] == lists[i + 1]:
                    continue
                child_list = lists[:i] + lists[i+1:]
            else:
                child_list = lists[:-1]
            temp = copy.deepcopy(save)
            temp.append(lists[i])
            recursion(child_list, temp)
    recursion(nums, save)
    print(ans)

if __name__ == '__main__':

    permute([1,2,1])


#大神题解
class Solution:
    def permuteUnique(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        result = []
        nums.sort()
        self.backtrack(nums, [], result)
        return result

    def backtrack(self, nums, tmp, result):
        if not nums:
            result.append(tmp)
            return
        for i in range(len(nums)):
            if i >= 1 and i < len(nums):
                if nums[i - 1] == nums[i]:
                    continue
            self.backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]], result)
