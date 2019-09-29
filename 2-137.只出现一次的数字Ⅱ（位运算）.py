#time 76.26 room 5.17
class Solution:

    def singleNumber(self, nums) -> int:
        nums.sort()
        if len(nums) == 1:
            return nums[0]
        i = 0
        while i < len(nums) - 2:
            if nums[i] == nums[i + 2]:
                i += 3
            else:
                return nums[i]
        return nums[-1]