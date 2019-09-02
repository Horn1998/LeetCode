import copy
def permute(nums):
    ans, save = [], []
    def recursion(lists, save):
        if len(lists) == 0:
            temp = copy.deepcopy(save)
            ans.append(temp)
            return
        else:
            for i in range(len(lists)):
                temp = copy.deepcopy(save)
                temp.append(lists[i])
                if i != len(lists) - 1:
                    child_list = lists[:i] + lists[i+1:]
                else:
                    child_list = lists[:-1]
                recursion(child_list, temp)
    recursion(nums, save)
    print(ans)

if __name__ == '__main__':
    permute([0])




#大佬题解
class Solution:
    def permute(self, nums):
        #设置回溯法终止条件
        if len(nums) <= 1:
            return [nums]

        ans = []
        for i, num in enumerate(nums):
            sub_nums = nums[:i] + nums[i + 1:]
            for j in self.permute(sub_nums):
                j.append(num)
                ans.append(j)
                # print(ans)
        return ans
Highcoder = Solution()
Highcoder.permute([1,2,3])

# [[3, 2]]
# [[3, 2], [2, 3]]
# [[3, 2, 1]]
# [[3, 2, 1], [2, 3, 1]]
# [[3, 1]]
# [[3, 1], [1, 3]]
# [[3, 2, 1], [2, 3, 1], [3, 1, 2]]
# [[3, 2, 1], [2, 3, 1], [3, 1, 2], [1, 3, 2]]
# [[2, 1]]
# [[2, 1], [1, 2]]
# [[3, 2, 1], [2, 3, 1], [3, 1, 2], [1, 3, 2], [2, 1, 3]]
# [[3, 2, 1], [2, 3, 1], [3, 1, 2], [1, 3, 2], [2, 1, 3], [1, 2, 3]]


#官方题解
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(first=0):
            # if all integers are used up
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        output = []
        backtrack()
        return output

