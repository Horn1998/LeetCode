#time 97 room 6.6
class Solution:
    def summaryRanges(self, nums):
        if not nums: return []
        nums.sort()
        nums = [min(nums)] + nums
        tot1, tot2 = 0, 0
        ans = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                tot2 = nums[i]
            else:
                s = str(tot1)
                if tot2 != tot1:
                    s += '->'
                    s += str(tot2)
                ans.append(s)
                tot1 = nums[i]
                tot2 = tot1
        s = str(tot1)
        if tot2 != tot1:
            s += '->'
            s += str(tot2)

        ans.append(s)
        return ans[1:]