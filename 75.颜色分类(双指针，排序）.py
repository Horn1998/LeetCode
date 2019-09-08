#时间：69.4 空间：5
def sortColors(nums):
    tot1, tot2, tot3 = 0, 0, len(nums)- 1
    while tot2 <= tot3:
        if nums[tot2] == 0:
            nums[tot1] = 0
            tot1 += 1
        elif nums[tot2] == 2:
            while nums[tot3] == 2 and tot2 != tot3:
                tot3 -= 1
                if tot3 == -1:
                    return nums
            if nums[tot3] == 0:
                nums[tot1] = 0
                tot1 += 1
            nums[tot3] = 2
            tot3 -= 1
        tot2 += 1
    for i in range(tot1, tot3 +1):
        nums[i] = 1
    return nums
if __name__ == '__main__':
    sortColors([2])




