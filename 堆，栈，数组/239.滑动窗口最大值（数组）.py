#time 91 room 5
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        ans = []
        if not nums: return []
        length = len(nums)
        i = 0
        while i < length - k + 1:
            Max = -1 * float('inf')
            tot = i
            for j in range(k):
                if nums[i + j] > Max:
                    Max = nums[i + j]
                    tot = j
            ans.append(Max)
            for m in range(0, tot):
                i += 1
                if k + i - 1 == len(nums):
                    break
                if nums[i + k - 1] > Max:
                    Max = nums[i + k - 1]
                ans.append(Max)
            i += 1
        return ans
