#time 98.74 room 5.14
class Solution:
    less = float('inf')
    def minSubArrayLen(self, s: int, nums):
        if not nums: return 0
        left, right, sums = 0, 0, 0
        for right in range(len(nums)):
            sums += nums[right]
            if sums >= s:
                while sums - nums[left] >= s:
                    sums -= nums[left]
                    left += 1
                if self.less > right - left + 1:
                    self.less = right - left + 1
        if self.less == float('inf'):
            self.less = 0#官方题解
        return self.less




import bisect
class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        if not nums : return 0
        # 求前缀和
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        #print(nums)
        # 总和都小于 s 时候
        if nums[-1] < s: return 0
        res = float("inf")
        nums = [0] + nums
        for i in range(1, len(nums)):
            if nums[i] - s >= 0:
                # 二分查找
                loc = bisect.bisect_left(nums, nums[i] - s)
                if nums[i] - nums[loc] >= s:
                    res = min(res, i - loc)
                    continue
                if loc > 0:
                    res = min(res, i - loc + 1)
        return res


