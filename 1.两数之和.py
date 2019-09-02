#简单题
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for ind, num in enumerate(nums):
            hashmap[num] = ind
        for ind, num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and j != ind:
                return [ind, j]
        return  []

if __name__ == '__main__':
    ans = Solution()
    print(ans.twoSum([3,2,4], 6))
