def nextPermutation(nums):

    if sorted(nums,reverse = True) == nums:
        nums.sort()
        print(nums)
        return nums
    #如果是降序则直接返回
    for i in range(len(nums) - 2, -1 ,-1):
        min = 10000
        tot = -1
        for j,value in enumerate(nums[i+1:]):
            if nums[i + 1 + j] - nums[i] > 0 and nums[i + 1 + j] - nums[i] < min:#从右向左找到右侧有最小值的数字，并将差值最小的两个数交换
                min = nums[i + 1 + j] - nums[i]
                tot = i + 1 + j

        if min != 10000:#找到符合条件的两个数进行交换
            temp = nums[tot]
            nums[tot] = nums[i]
            nums[i] = temp
            #对后面的数字进行降序排列
            # for m, value1 in enumerate(nums[i + 1:-1]):
            #     for n in range(len(nums[i+1:]) - m -1):
            #         if nums[i+1+n] > nums[i+2+n]:
            #             nums[i+1+n], nums[i+2+n] = nums[i+2+n] ,nums[i+1+n]
            print(nums)
            break

if __name__ == '__main__':
    nums = [3,2,1]
    nextPermutation(nums)