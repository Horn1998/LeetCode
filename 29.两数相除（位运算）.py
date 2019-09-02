#29 中等
def divide(dividend, divisor):
    left = dividend
    ans = 0
    while(left > 0 and left > divisor):
        count = 0
        while (divisor << count) < left:
            count = count + 1
        ans += pow(2,count - 1)
        left = left - (divisor << (count -1))
        print(left)
    if left == divisor:
        ans += 1
    if ans > pow(2,31)-1 or ans < -pow(2,31):
        return pow(2,31) - 1
    print(ans)
    return ans
if __name__ == '__main__':
    divide(5,1)
    print(int(0/333))