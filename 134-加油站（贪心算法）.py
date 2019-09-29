#time 84.76 room5 .39
class Solution:
    reverse = 0
    def canCompleteCircuit(self, gas, cost):
        length = len(gas)
        self.reverse = length -1
        total_dis,  total_fuel = 0, 0
        for turn in range(length):
            total_dis += gas[turn]
            total_fuel += cost[turn]
            while total_dis < total_fuel and self.reverse > turn:
                total_dis += gas[self.reverse]
                total_fuel += cost[self.reverse]
                self.reverse -= 1
            if self.reverse == turn and total_dis >= total_fuel:
                return (self.reverse + 1)%length
            elif self.reverse == turn and total_dis < total_fuel:
                return -1


class Solution:

    def reverse(self, x: int) -> int:
        sign = 1
        if x == -1 * abs(x):
            sign = -1
        x = abs(x)
        reverses = 0
        while x > 10:
            reverses *= 10
            reverses += x % 10
            x = int(x/10)
        return sign * (reverses + x)


