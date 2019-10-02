#time = 97 room 5
class Solution:
    max_income = 0
    judge = False
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        dp1 = [0 for _ in range(len(nums))]
        dp2 = [0 for _ in range(len(nums))]
        #双动态规划
        #第一间房屋打劫，最后一间房不打劫 与 第一间房不打劫， 最后一间房打劫
        dp1[0], dp1[1], dp2[0], dp2[1] = nums[1],max(nums[1], nums[2]), nums[0],max(nums[0], nums[1])
        def dynamic_design(dp, start, end):
            count = 1
            for i in range(start, end):
                count += 1
                if nums[i] + dp[count - 2] > dp[count - 1]:
                    dp[count] = nums[i] + dp[count - 2]#打劫方式为当前房屋和前n-1间房屋的最大金额
                else:
                    dp[count] = dp[count - 1]
            return dp[count]
        ans1 =  dynamic_design(dp1, 3, len(nums))
        ans2 =  dynamic_design(dp2, 2, len(nums) - 1)
        return max(ans1, ans2)