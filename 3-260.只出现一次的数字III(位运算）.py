#time 10 room 5
class Solution:
    def singleNumber(self, nums):
        nums.sort()
        ans = []
        while nums:
            if len(nums) == 1:
                ans.append(nums[0])
                break
            if not ans and len(nums) == 2:
                ans = nums
                break
            if nums[0] == nums[1]:
                nums= nums[2:]
            else:
                ans.append(nums[0])
                nums = nums[1:]
        return ans
#位运算
#题目描述：给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。
#运算符 ^= 异或运算  &= 与或运算
def singleNumber(self, nums):
    #对所有数字进行异或运算，最终剩下的便是两个不同数字的异或结果
    diff = 0
    for num in nums:
        diff ^= num
    #找的一个二进制数用以区分两个不同的数
    #根据diff中第一个为1的位置，下面这个式子有点东西
    diff &= ~diff + 1
    #通过上方得到的数字对数组中的数字进行分类，每一类包含两个不同的数之一
    num1, num2 = 0, 0
    for num in nums:
        if diff & num:
            num1 ^= num
        else:
            nums ^= num
    return [num1, num2]