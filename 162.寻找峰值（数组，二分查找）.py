#time 76,53 room 5
class Solution:
    def findPeakElement(self, nums):
        nums = [-1000000000000] + nums
        n = len(nums)
        nums.append(-1000000000000)

        def guibing(start, end):
            mid = int((start + end) / 2)
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid - 1
            elif nums[mid] > nums[mid + 1] and nums[mid] < nums[mid - 1]:
                return guibing(start, mid - 1)
            else:
                return guibing(mid + 1, end)

        return guibing(1, n)
