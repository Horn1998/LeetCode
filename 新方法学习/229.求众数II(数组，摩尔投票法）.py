#time 73.87 room 5.26
class Solution:
    def majorityElement(self, nums):
        dicts = {}
        ans = []
        length = len(nums)
        for i in nums:
            dicts.setdefault(i, 0)
            dicts[i] += 1
            if dicts[i] > int(length / 3) and i not in ans:
                ans.append(i)
        return ans
#官方题解（摩尔投票法）
#原理： 当一个数的重复次数超过数组长度的一半，每次将两个不相同的数删除，最终剩下的就是要找的数。
# 在长度为n的数组中找出重复次数超过n/3的数（不一定存在）。
# 容易知道，重复次数超过数组长度1/3的数最多有两个。用反证法容易证得。
# 同样的思路，使用两个虚拟数组，每次删除三个不同的数，最终虚拟数组中的两个数就是可能的答案，此时再遍历一遍数组，做一个验证即可。
class Solution2:
    def majorityElement(self, nums):
        length = len(nums)
        v1, v2, cv1, cv2 = float('inf'), float('inf'), 0, 0#两个虚拟数组
        #寻找出现次数最多的两个数
        for i in range(length):#判断条件的顺序不能调换
            if nums[i] == v1: cv1 += 1
            elif nums[i] == v2: cv2 += 1
            elif cv1 == 0:
                v1 = nums[i]
                cv1 += 1
            elif cv2 == 0:
                v2 = nums[i]
                cv2 += 1
            else:
                #当三个数不同时，同时删掉三个数
                cv1 -= 1
                cv2 -= 1
        #判断出现次数是否超过n/3
        cv1, cv2 = 0, 0
        for i in range(length):
            if nums[i] == v1: cv1 += 1
            if nums[i] == v2: cv2 += 1
        ans = []
        if cv1 > int(length / 3):
            ans.append(v1)
        if cv2 > int(length / 3):
            ans.append(v2)
        return ans