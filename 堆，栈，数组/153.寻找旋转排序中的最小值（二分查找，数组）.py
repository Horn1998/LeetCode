#time 85.92 room  5.08
class Solution:
    def findMin(self, nums) -> int:
        def guibing(start, end):
            temp = sorted(nums)
            if temp == nums:
                return nums[0]
            mid = int((start + end) / 2)
            if nums[start] > nums[mid]:
                return guibing(start, mid)
            elif nums[mid + 1] > nums[end]:
                return guibing(mid + 1, end)
            else:
                return nums[mid + 1]

        return guibing(0, len(nums) - 1)
