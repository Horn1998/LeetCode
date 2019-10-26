#time 96  room 5
class Solution:
    def hIndex(self, citations) -> int:
        citations.sort(reverse = True)
        count = 1
        for i in citations:
            if i >= count:
                count += 1
            else:
                break
        return count - 1