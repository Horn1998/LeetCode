#13 中等难度 自做
def remanToInt(num):
    roma = ['I','V','X','L','C','D','M','']
    specific = [['IV','IX'],['XL','XC'],['CD','CM'],['','']]
    ans = ""
    for i in range(3,-1,-1):
        left = int(num/pow(10,i))
        num = num % pow(10,i)
        if left == 9:
           ans += specific[i][1]
        elif left == 4:
            ans += specific[i][0]
        else:
            more = left % 5

            left = left - 5
            if left >= 0:
                ans += roma[2*i + 1]
            print(more)
            for k in range(more):
                ans += roma[2*i]
    print(ans)
if __name__ == '__main__':
    remanToInt(3456)

