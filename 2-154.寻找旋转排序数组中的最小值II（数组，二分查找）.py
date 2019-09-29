#time 5 room 5
class Solution:
    def findMin(self, nums) -> int:
        def guibing(start, end):
            if temp[0] == nums[0]:
                return temp[0]
            mid = int((start + end) / 2)
            if temp[start] > temp[mid]:
                return guibing(start, mid)
            elif temp[mid + 1] > temp[end]:
                return guibing(mid + 1, end)
            else:
                return temp[mid + 1]

        temp = list(set(nums))
        temp.sort(key=nums.index)
        nums.sort()
        return guibing(0, len(temp) - 1)
