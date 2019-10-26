#time 76.26 room 5.17
class Solution:

    def singleNumber(self, nums) -> int:
       left = 0
       for num in nums:
           left ^= num
       return left