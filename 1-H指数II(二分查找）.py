#time 83 room 6
class Solution:
    def hIndex(self, citations) -> int:
        count = 1
        for i in range(len(citations) - 1, -1, -1):
            if citations[i] >= count:
                count += 1
            else:
                break
        return count - 1