#75.33 5.14
def uniquePaths(m, n):
    def factorial(num):
        if num == 1:
            return 1
        return num * factorial(num - 1)
    return int(factorial(n + m)/(factorial(m)*factorial(n)))
if __name__ == '__main__':
    print(uniquePaths(3,4))