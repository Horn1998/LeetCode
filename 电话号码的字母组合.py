def letterCombinations( digits):

    dicts = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    answer = [i for i in dicts[digits[0]]]
    for i in range(1,len(digits)):#获取数字
        save = len(answer)
        for key, value in enumerate(dicts[digits[i]]):#获取数字对应的字母
            for k in range(save):
                if key != 0:
                     answer.append(answer[k][:-1] + value)
                elif key == 0:
                     answer[k] += value
    print(answer)
    return answer

if __name__ == '__main__':
    letterCombinations("32")

