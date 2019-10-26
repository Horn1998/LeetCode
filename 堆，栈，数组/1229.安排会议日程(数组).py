#time 1560ms
class Solution:
    def minAvailableDuration(self, slots1, slots2, duration: int):
        slots1.sort()
        slots2.sort()
        index = 0
        for section_x in slots1:
            for section_y in slots2[index:]:
                if section_x[0] >= section_y[1]:
                    index += 1
                    continue
                elif section_x[1] <= section_y[0]:
                    break
                judge = [section_x[1] - section_y[0], section_x[1] - section_x[0], section_y[1] - section_x[0], section_y[1] - section_y[0]]
                Min = min(judge)
                if Min >= duration:
                    for i in range(4):
                        if judge[i] == Min and (i == 3 or i == 0):
                            return [section_y[0], section_y[0] + duration]
                        elif judge[i] == Min and (i == 2 or i == 1):
                            return [section_x[0], section_x[0] + duration]

